# Historical synthetic agent episodes (2025 source; reviewed 2026-10-23)

This is an exact mirror of the 55,368,388-byte `genetic_adaptation_dataset.json` previously published in the first-party shafire/Unified_Genetic_MultiDimensional_Framework repository. It contains **150,000 JSON episode records**, six declared fictional agent labels, six simulated environment labels, three numeric parameters and six numeric trait fields, with a generated timestamp per episode.

The original upstream card describes a 50,000-example CSV classification view. That is not the record count of this JSON artifact: the complete JSON was streamed and counted at 150,000. This release preserves the JSON unchanged, rather than silently treating the card's count as a census.

## Schema and origin

Every record has exactly `agent`, `environment`, `timestamp`, `x`, `y`, `Q`, `traits`. `traits` has exactly `neuro_adaptivity`, `entropy_resilience`, `quantum_flex`, `reaction_time`, `decision_depth`, `chaos_index`. Parameters and traits are finite numbers. Agents and environments must match the explicit fictional labels in SCHEMA.json. The complete scan found no additional fields, schema violations or exact duplicate records.

The historical card credits **Shaf Brady & Agent Zero**, identifies the material as synthetic and declares **MIT**. The mirror preserves that existing grant; it does not relicense third-party content. Exact source revision, original card hash, Git LFS content identity and mirror transformations are in PROVENANCE.json. The JSON's SHA-256 exactly matches the public source's LFS object identity.

No generator or random seed was present in the inspected JSON-only source archive. The standalone validator reproduces structural/integrity checks; it does not reproduce generation or validate the underlying formula. UPSTREAM_CARD.md is preserved as historical source documentation, including its dated terminology and claims.

## Privacy and scientific limits

All 150,000 records passed the strict field/type/fictional-label census. Token/private-key, email, rsID, genotype-row and user-path pattern screens found no matches. The source is a simulation dataset, not an individual or reference genome matrix, a participant cohort, customer data or provider experiment output. Pattern screens are bounded and do not prove the absence of every possible private fact; the schema and source declaration provide the additional publication basis here.

Names such as genetic adaptation, quantum, neuro-adaptivity or hyperdimensional simulation are historical synthetic labels. These numeric records do not establish physical quantum computation, biological adaptation, health traits, human cognition, model intelligence or a scientific advantage. No clinical/biological interpretation, training, inference or empirical capability test was performed in this publication review.

There is no train/validation/test assignment in this historical JSON. Exact record duplication is zero; semantic/scenario independence was not established. A future experiment must define grouped partitions and independent evaluations before training. Do not combine it with genomic records or treat simulation labels as clinical ground truth.
