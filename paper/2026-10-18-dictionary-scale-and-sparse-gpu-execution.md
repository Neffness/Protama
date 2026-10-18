# Making the Full Dictionary Practical for Protama

## Abstract

This paper reports a hardware-capacity experiment using a real dictionary
corpus as a connected symbolic workload for Protama. The initial GPU
implementation appeared to scale poorly: as the graph grew from hundreds to
the full corpus, active VRAM rose into the multi-gigabyte range and the
feasibility of a complete run became uncertain. Rather than stop at a
convenient partial result, the experiment measured the scaling failure,
identified the dense activation representation responsible for it, and
redesigned the execution path around RAM-backed graph shards and sparse GPU
accumulation.

The final implementation processed the complete learned dictionary graph of
172,781 usable entries, 125,912 symbols, and 637,448 edges. GPU scoring
completed in 3.27 seconds with 19.4 MB of peak active VRAM, compared with
9.61 seconds and 3.63 GB for the original full-corpus implementation. The
result is not merely a smaller benchmark: it is the original experiment
carried through to its intended full-corpus execution.

## Research question

The experiment asked whether a real dictionary-sized connected symbolic
workload would overwhelm Protama's GPU substrate as graph size increased.
The dictionary was selected because it provides a large, naturally connected
source of symbols and transitions without requiring a synthetic graph
generator.

The goal was not to optimize dictionary lookup. Dictionary files remained an
external data source. The measured workload was the learned symbolic graph
produced from dictionary definition tokens and their transitions.

## Experimental method

Every official measurement ran the complete Protama curriculum first through all the
gates and training lessons. The graph was then constructed from bounded
definition token sequences, with up to 24 tokens retained per definition.
The workload used sparse directed symbol connections and scored batches of
symbolic observations using the Torch substrate.

The measurements were run on a Razer Blade 16 (RZ09-0528) laptop with:

* AMD Ryzen AI 9 365 processor (10 cores, 20 logical processors);
* 32 GB installed system RAM (29.6 GB reported available to the operating
  system);
* NVIDIA GeForce RTX 5070 Laptop GPU with 8 GB VRAM (8,151 MiB);
* Windows 11 Home, 64-bit;
* NVIDIA driver 616.56;
* Python 3.12.12;
* PyTorch 2.11.0 with CUDA 12.8.

The benchmark reports both allocated and reserved VRAM. Allocated memory is
memory actively held by live tensors; reserved memory also includes blocks
held by the framework's caching allocator for reuse. Reserved memory is
therefore the conservative runtime capacity requirement. Some of that cache
can be released between workloads or when the process exits, but it should
not be ignored when sizing a device for an uninterrupted run.

The experiment recorded graph size, GPU graph-construction time, scoring time,
active allocated VRAM, and reserved VRAM separately.

## Initial scaling curve

The trained workload was increased progressively rather than jumping directly
to the full corpus:

| Effective entries | Symbols |   Edges | GPU graph + score | Peak allocated VRAM |
| ----------------: | ------: | ------: | ----------------: | ------------------: |
|               200 |     848 |   1,602 |            9.6 ms |              3.4 MB |
|             1,000 |   3,410 |   7,815 |           15.4 ms |             68.4 MB |
|             5,000 |  11,172 |  32,963 |          116.8 ms |            322.7 MB |
|            10,000 |  17,217 |  59,521 |          273.7 ms |            498.0 MB |
|            20,000 |  27,410 | 106,839 |          826.9 ms |            791.9 MB |
| full `S` section |  21,502 |  28,814 |           1.730 s |            828.4 MB |

Here, `S` means the tagged S section of the dictionary source, not the full
dictionary. The curve initially looked manageable, then bent upward as graph
width and activation costs increased. This was the point at which a
full-corpus run appeared potentially impractical.

## Diagnosing the bottleneck

The graph was stored sparsely, but the original scoring path created dense
activation and output structures with dimensions proportional to:

```text
observation_batch_size × total_symbol_count
```

This meant that a sparse graph could still require large dense GPU tensors.
The full dictionary baseline contained 125,912 symbols and 637,448 edges.
Its original GPU measurement reached:

| Measurement         | Original full-dictionary backend |
| ------------------- | -------------------------------: |
| GPU graph build     |                           753 ms |
| GPU scoring         |                           9.61 s |
| Peak allocated VRAM |                          3.63 GB |
| Peak reserved VRAM  |                          4.89 GB |

The experiment had not reached a Protama knowledge limit. It had reached a
representation limit in the accelerator backend.

## Execution redesign

The execution path was changed in two stages.

First, the graph was kept in system RAM and streamed to the GPU in source
shards. Observation batches were bounded so the complete workload did not
require one enormous activation tensor.

Second, the dense batch-wide score matrix was removed. The final sparse
accumulator:

1. collects only nonzero source-to-destination contributions;
2. constructs a sparse score tensor for the current observation batch;
3. coalesces duplicate contributions on the GPU;
4. transfers only the nonzero results needed for deterministic top-k ranking.

The backend remained semantically compatible with the CPU reference. Focused
equivalence tests passed for single observations, batches, propagation, and
sparse-versus-dense scoring.

The intermediate dense-streaming implementation retained a bounded dense
score matrix while moving graph shards through system RAM:

| Measurement         | Intermediate dense streaming |
| ------------------- | ---------------------------: |
| GPU graph build     |                       680 ms |
| GPU scoring         |                      35.29 s |
| Peak allocated VRAM |                        47 MB |
| Peak reserved VRAM  |                       1.53 GB |

## Full-corpus result

The final run used the complete dictionary corpus:

* 172,781 usable entries;
* 125,912 symbols;
* 637,448 edges;
* 50,000 scoring observations;
* full curriculum completed before measurement.

Each observation was a deterministic one-symbol probe consisting of the first
token of a dictionary definition. The probes were repeated as needed to form
the fixed 50,000-observation scoring batch; they were not random walks or
synthetic graph edges.

The final sparse-streaming result was:

| Measurement           | Original backend | Final sparse-streaming backend |
| --------------------- | ---------------: | -----------------------------: |
| GPU graph build       |           753 ms |                         523 ms |
| GPU scoring           |           9.61 s |               **3.27 s** |
| Graph build + scoring |          10.37 s |               **3.80 s** |
| Peak allocated VRAM   |          3.63 GB |              **19.4 MB** |
| Peak reserved VRAM    |          4.89 GB |              **1.53 GB** |

The final path was approximately 10.8 times faster than the intermediate
dense-streaming implementation and approximately 2.9 times faster than the
original backend, while using approximately 99.5% less active VRAM than the
original backend. The intermediate implementation shows the cost of solving
the memory problem with sharding alone: it reduced active VRAM to 47 MB but
was approximately 3.7 times slower than the original backend. Sparse
accumulation provided the additional step that recovered the performance.

For practical hardware sizing, the final run's approximately 1.53 GB reserved
VRAM is the conservative figure, not 19.4 MB. The smaller allocated figure
describes the live sparse tensors; the larger reserved figure reflects the
framework allocator's reusable cache and temporary workspace. The cache is
reclaimable at process boundaries and can often be trimmed between workloads,
but the run should be planned against the reserved high-water mark.

## Interpretation

The experiment succeeded by following the problem to its full extent. The
initial measurements did not merely show that the graph was getting larger;
they showed why the original execution path was becoming expensive. That
evidence led to a RAM-backed and sparse GPU execution plan, which then
completed the entire dictionary workload.

The central result is therefore the end-to-end progression:

1. a partial workload exposed a rapidly increasing resource cost;
2. doubling the workload made a full run appear risky;
3. profiling isolated dense activation as the dominant representation cost;
4. graph storage and scoring were redesigned around sparsity;
5. the full dictionary completed quickly and within a small active VRAM
   budget.

This demonstrates that the initial multi-gigabyte behavior was not an
intrinsic limit imposed by the dictionary or by Protama's learned graph. It
was a correctable mismatch between a sparse workload and a dense scoring
representation.

This GPU result follows the earlier
[Structural Gate publication](2026-10-17-structural-gate-completion.md), whose
declared claim was CPU-only and explicitly excluded GPU parity. The two
results should be read as sequential evidence: the gate established the
declared CPU behavior first, and this experiment subsequently measured the
GPU-oriented substrate path.

## Limitations

This result does not establish that every future Protama workload will fit in
19.4 MB of active VRAM. The measured graph is a one-step transition graph
derived from bounded dictionary definitions. A future graph in which each
word participates in hundreds or thousands of relations may have different
locality and memory behavior.

The result also does not measure dictionary-file lookup latency, open-ended
language understanding, or general intelligence. It measures the capacity and
scaling behavior of a trained symbolic graph substrate under a reproducible
dictionary-derived workload.

## Reproducibility

The experiment retained machine-readable reports for the scaling curve, the
original full-corpus baseline, and the final sparse-streaming result. The
public paper intentionally omits private filesystem paths, timestamped
artifact identifiers, and environment fingerprints. The reported graph
dimensions, timings, memory measurements, workload construction, and backend
comparison are sufficient to reproduce the analysis without exposing internal
repository structure.
