import unittest

from structural_transfer_benchmark.structural.generator import (
    NEAR_MISS_CATEGORIES,
    check_episode_leakage,
    episode_to_json,
    generate_structural_gate_episode,
)
from structural_transfer_benchmark.structural.models import (
    GateAdapterRun,
    GatePrediction,
    GateTrace,
)
from structural_transfer_benchmark.structural.manifest import build_locked_final_manifest
from structural_transfer_benchmark.structural.scorer import (
    aggregate_structural_gate_scores,
    evaluate_preregistered_pass_rule,
    score_structural_gate_episode,
)
from structural_transfer_benchmark.structural.topologies import generate_topology_episode


class PublicStructuralBenchmarkTests(unittest.TestCase):
    def test_generation_is_deterministic_and_leakage_checked(self):
        first = generate_structural_gate_episode(41)
        second = generate_structural_gate_episode(41)

        self.assertEqual(episode_to_json(first), episode_to_json(second))
        self.assertTrue(all(check.passed for check in check_episode_leakage(first)))
        self.assertEqual(
            {
                case.near_miss_category
                for case in first.evaluation
                if case.near_miss_category is not None
            },
            set(NEAR_MISS_CATEGORIES) - {"ambiguous", "contradictory"},
        )

    def test_public_topologies_are_deterministic(self):
        for topology in ("equivalence", "purpose"):
            first = generate_topology_episode(2000, topology)
            second = generate_topology_episode(2000, topology)
            self.assertEqual(episode_to_json(first), episode_to_json(second))
            self.assertTrue(all(check.passed for check in check_episode_leakage(first)))

    def test_manifest_fingerprint_matches_published_heldout_artifact(self):
        manifest = build_locked_final_manifest(
            generator_seeds=range(1000, 1050),
            topology_seeds=(
                (topology, seed)
                for topology in ("equivalence", "purpose")
                for seed in range(2000, 2025)
            ),
        )

        self.assertEqual(
            manifest.content_fingerprint,
            "efd287c8b1f81d5ee1b4a2bf88a314a1776e48dbd6ee28a21983d8824b5a3c36",
        )

    def test_public_scorer_scores_a_well_formed_run(self):
        episode = generate_structural_gate_episode(41)
        predictions = tuple(
            GatePrediction(
                case_id=case.case_id,
                predicted_status=case.expected_status,
                abstained=case.expected_status == "abstained",
            )
            for case in episode.evaluation
        )
        traces = tuple(
            GateTrace(
                case_id=case.case_id,
                selected_evidence=({"feature": "public-test"},),
                rejected_evidence=(),
                explanation={
                    "invariants": ["public-test"],
                    "irrelevancies": [],
                    "counterfactuals": ["public-test"],
                },
            )
            for case in episode.evaluation
        )
        score = score_structural_gate_episode(
            episode,
            GateAdapterRun(predictions=predictions, traces=traces),
        )
        aggregate = aggregate_structural_gate_scores(
            [score],
            bootstrap_resamples=20,
        )
        result = evaluate_preregistered_pass_rule(aggregate)

        self.assertEqual(score.case_count, len(episode.evaluation))
        self.assertEqual(score.positive_accuracy, 1.0)
        self.assertEqual(score.novel_vocabulary_accuracy, 1.0)
        self.assertEqual(result["status"], "PASS")


if __name__ == "__main__":
    unittest.main()
