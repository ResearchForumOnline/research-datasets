# AI curricula, licensed mixtures and evaluation boundaries

The [dated release](https://github.com/ResearchForumOnline/research-datasets/releases/tag/datasets-2026.10.23) distributes explicitly reviewed packages. The [catalog](catalog.json) records exact asset sizes and SHA-256 values; publication/download status is shown on the release page. Dataset cards and per-pack license files govern reuse.

## Original authored datasets

| Package | Record types and counts | Data payload bytes |
| --- | --- | ---: |
| [OpenZero original research curriculum](cards/openzero-original-research-v1.md) | 413 SFT records: 361 train, 52 validation; 120 preference pairs; 39 frozen evaluation records | 907,100 |
| [Zero original agent curriculum](cards/zero-original-agent-curriculum-v1.md) | 69 original Zero examples and 96 original agent, observation and research examples | 125,623 |
| [Original October pilot](cards/zero-original-pilot-20261009.md) | 100 examples in 94 scenario groups: 60 train, 20 validation, 20 test; separate held-out checks and continuation probes | 48,454 for the three primary splits |

These are different record types. The research package's 572 total records are not 572 independent instruction examples. Original contributions are CC BY 4.0. The October package's standalone generator and validator are MIT. Base model weights are not included or relicensed.

The October pilot remains preparation for a canceled experiment. This release did not resume training or establish a completed model. Its portable validator passed the 100-record / 94-group structural check; that is a dataset check, not a model-quality result. Its source-copy guard contains hashes of normalized 16-word spans from two already-public original manuscripts, with their URLs and licenses. It does not ship private methodology-note text, paths or hashes.

## Reviewed licensed mixtures

The [July mixture package](cards/openzero-reviewed-licensed-mixtures-20260726.md) contains two overlapping historical variants:

| Variant | Original records | Retained records | Held records | Retained JSONL bytes |
| --- | ---: | ---: | ---: | ---: |
| Zero v2 reviewed | 1,986 | 1,870 | 116 | 5,297,632 |
| Gemma formatting variant reviewed | 2,033 | 1,921 | 112 | 5,147,378 |

These are composite datasets. Original authored records are CC BY 4.0; third-party content retains its source terms. The NVIDIA sources identify CC BY 4.0. Only Smol-constraints, Smol-magpie-ultra, Smol-rewrite and Smol-summarize are used from SmolTalk under Apache 2.0. Imported code retains its exact source license, attribution and immutable source commit. A compilation label does not replace a code author's license.

All 400 imported code records were checked against official repository license files at their recorded source commits. License content was retrieved for 339; 61 were unavailable. Of the retrieved records, 42 had unresolved license identification and two contained GPL/MPL license text despite permissive original metadata. Those 105 records were held. Recognized permissive rights were established for 295 records; whole contact-review exclusions leave 289 code records in each derivative variant. Their original license files and eight discovered upstream NOTICE files are included.

Per variant, the held reasons include 61 unavailable licenses, 44 unresolved/copyleft licenses, seven email-review records and one path-review record; v2 also has one phone-review record and three additional credential-looking dialogue records identified by independent generic-key screening. Their inactive/fictional status was not established, so they were omitted whole without testing credentials. The final staged-AI generic-key scan returned zero findings. Reasons overlap, so these reason totals must not be added as distinct people or rows. Whole records were omitted; answers and code were not silently rewritten. Public copyright-attribution contacts in original license/NOTICE files remain intact for compliance with their terms.

Primary upstream license sources:

- [NVIDIA Nemotron-SFT-OpenCode-v1](https://huggingface.co/datasets/nvidia/Nemotron-SFT-OpenCode-v1)
- [NVIDIA Nemotron-RL-Agentic-Function-Calling-Pivot-v1](https://huggingface.co/datasets/nvidia/Nemotron-RL-Agentic-Function-Calling-Pivot-v1)
- [SmolTalk, with subset-specific licensing](https://huggingface.co/datasets/HuggingFaceTB/smoltalk)
- [CommitPackFT, with original repository licenses](https://huggingface.co/datasets/bigcode/commitpackft)

The v2 historical function-calling slice has known quality problems, including some answers that narrate tool outcomes without observations. The Gemma variant originally excluded that entire slice. Historical preservation is not endorsement of each answer or a recommendation to train without further curation.

## Overlap and evaluation limits

The four packages contain 4,680 normalized content/evaluation-support occurrences, reducing to 2,577 unique normalized records. The 2,103 repeated occurrences largely reflect component and formatting variants. These figures include 52 October held-out-check/continuation-probe payloads; those are evaluation support, not additional independent training examples. There are 4,628 primary dataset record occurrences across packages before deduplication.

Normalization compares Unicode word tokens from user and assistant turns, excluding repeated system policies and provenance. Preference records combine their prompt, chosen and rejected content. Each staged content file has zero within-file exact normalized conversation duplicates.

- Original research and mixture variants share 413 unique normalized records.
- Original agent and mixture variants share 165 unique normalized records.
- The October pilot shares zero exact normalized records with the other packages.
- The two mixture variants share 1,525 normalized prompts and 1,523 normalized assistant answers. They are not independent train/test splits.
- Checked original research train/validation and October train/validation/test pairs have zero exact normalized prompt overlap and zero exact normalized answer overlap.
- A bounded eight-word-shingle Jaccard check at similarity at least 0.8 found 192 distinct near pairs among the canonical records. This is lexical analysis, not an embedding-based semantic-independence proof.

Both historical mixtures already incorporated all 413 July SFT records, including the earlier 52 validation records. Those 52 records cannot independently validate a model trained on a mixture. Do not concatenate all packages blindly, advertise the sum as unique examples, or use one formatting variant to evaluate the other. Keep frozen evaluations, held-out answers and continuation probes out of training. No inference, copying-performance score or model-improvement result was produced by this publication review.

## Reviewed numeric simulation mirror

The [genetic-adaptation simulation pack](cards/genetic-adaptation-synthetic-simulation-v1.md)
contains the unchanged 55,368,388-byte JSON with **150,000 fictional agent/environment
episodes**. A full schema/type census, duplicate check and privacy-pattern review
were completed. Its SHA-256 matches the existing public source, whose MIT terms
and attribution are retained. A standalone validator is included. The historical
50,000-record card describes a different CSV classification view; it is not the
JSON record count. This numeric simulation is separate from the four curriculum
and mixture packages and their conversation-overlap figures above. It contains no
human genotype data. Generator/seed recovery and scientific/model validity remain
outside the evidence established by the structural checks.

## Previously public legacy datasets

The following repositories were verified in the public Hugging Face account listing on 23 October 2026. They were already public. The specifically reviewed numeric JSON above is mirrored here; the remaining upstream artifacts are not newly privacy-cleared by this catalog:

| Existing public dataset | Verified public artifact metadata |
| --- | --- |
| [shafire/SpectraMind](https://huggingface.co/datasets/shafire/SpectraMind) | Ten CSV files, approximately 132 MB total |
| [shafire/TalkToAiQ](https://huggingface.co/datasets/shafire/TalkToAiQ) | Multiple CSVs, including a 59,615,085-byte reflection file |
| [shafire/Spectra8](https://huggingface.co/datasets/shafire/Spectra8) | 251,565-byte CSV |
| [shafire/Unified_Genetic_MultiDimensional_Framework](https://huggingface.co/datasets/shafire/Unified_Genetic_MultiDimensional_Framework) | The 55,368,388-byte numeric simulation JSON is now reviewed and mirrored; other artifacts retain their separate upstream status |

Metadata and file-tree verification do not establish full privacy clearance, source rights, factual accuracy, training suitability or biological validity of those existing contents. Read their own source and license records before reuse.

Unstructured legacy corpora, alternate training-text fragments and material without adequate provenance or rights remain withheld. No private genetic records, client/account databases, credentials, private correspondence, restricted provider research, runtime environments or broad archival backups are included in these AI packages. Unresolved materials are not represented as complete or privacy-cleared merely because a pattern screen found no match.

## What review establishes

Publication review used explicit allowlists, source/provenance inspection, parsed-record checks, whole-record exclusions, license evidence and checksums. All staged files, including utilities, auxiliary manifests and notices, were reviewed. Pattern screens cannot prove the absence of every private fact, licensing exception or error. The artifacts support reproducible data and software experiments; they do not establish model training, generalization, new capabilities, scientific validity or clinical utility.
