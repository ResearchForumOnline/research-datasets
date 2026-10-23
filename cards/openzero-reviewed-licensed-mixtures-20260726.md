# OpenZero reviewed licensed mixtures, July 2026 source variants

This derivative preserves reviewed records from two historical custom SFT blends. See PROVENANCE.json for exact counts, hashes, transformations and per-source licensing. These are two overlapping formatting/curriculum variants, not independent train/test splits. Do not concatenate blindly or treat one as held-out validation for the other.

Each variant has one training file and aligned row provenance. Original row numbers remain in original_row. Selected imported code has exact-commit license evidence. Flagged rows are excluded whole; original files on disk remain untouched. This is a composite dataset: third-party material retains its source licenses; original contributions are CC BY 4.0. There is no blanket relicensing to MIT or CC BY.

## Evaluation and quality limits

Both historical blends already merged all 413 July research SFT examples, including that earlier corpus's 52 validation examples. Those earlier 52 examples are therefore not independent validation after training on these blends. The two variants share source lineages and must not be split against each other.

The v2 variant retains a historical function-calling slice with known quality issues, including some answers that narrate unobserved tool outcomes. The Gemma variant originally removed that entire slice. Presence here documents the historical licensed corpus and does not endorse every response as correct agent behavior. Review and rebuild before training.

No model training, inference, quality improvement, factual correctness, privacy guarantee, or biological/clinical validity is established by this release. No canceled training run was resumed. Pattern checks and bounded rights review cannot establish the absence of every private fact or every file-specific licensing exception.
