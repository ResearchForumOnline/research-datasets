# AADR v14 public reference mirror: HO and compatibility_HO

Release ID: `aadr-v14-reference-2026.10.23`.
Source: Swapan Mallick and David Reich, Allen Ancient DNA Resource (AADR),
Harvard Dataverse version 14.0 / v66.p1, released 8 June 2026.
Dataset DOI: https://doi.org/10.7910/DVN/FFIDCW

This is a selected mirror of **seven unchanged official PUB reference files**,
not a complete AADR download and not a new ZeroThink research cohort. It contains
individual-level published reference genotypes, research sample identifiers and
source annotations for ancient and present-day individuals. Official PUB files
are distinct from private owner/client DNA. Public reference status is not a
warranty of anonymity or permission to identify participants.

| Panel/file set | Original bytes | Contents |
| --- | ---: | --- |
| compatibility_HO `.geno` | 1,909,008,156 | Official reference genotype matrix |
| HO `.geno` | 4,029,634,650 | Official larger Human Origins genotype matrix |
| Five metadata files | 72,052,340 | Two `.ind`, two `.snp`, one compatibility_HO `.anno` |
| Total | 6,010,695,146 | Seven exact source files |

Every filename, byte count and MD5 matches the saved official version-14 file
metadata. SHA-256 was independently computed over every source file. Exact file
hashes, official datafile IDs and download URLs are in PROVENANCE.json. These
checks establish identity with the official published files, not genotype accuracy,
consent verification for a new study or an independent privacy assessment of the
source dataset. No genotype interpretation or personal DNA analysis was run.

## License, attribution and use

The official version-14 metadata marks these files unrestricted and identifies
**CC0-1.0**, with no additional termsOfUse, termsOfAccess or restrictions fields.
The CC0 legal text is retained. Cite the versioned AADR dataset and Mallick et al.
2024, The Allen Ancient DNA Resource (AADR) a curated compendium of ancient human
genomes, Scientific Data11:182, https://doi.org/10.1038/s41597-024-03031-7.
AADR asks users also to cite the original component studies in the annotation
records. The annotations are provenance, not credentials. Refer to the original
AADR README and source record for study-specific context and interpretation.

CC0 does not remove privacy, publicity or other rights outside its scope. Do not
attempt re-identification or treat the public reference as a source of information
about the project owner's DNA. This mirror excludes owner uploads, target-overlap
NPZ caches, personal results, personalized array masks, credentials and client DBs.

## Transport and reconstruction

The compatibility_HO genotype file fits under the release asset size limit as one
file. The 4,029,634,650-byte HO genotype file is transported as three contiguous binary
chunks: 1,600,000,000; 1,600,000,000; 829,634,650 bytes. Concatenate the chunks in
numbered order using a binary-safe tool, then verify the reconstructed original's
SHA-256 and MD5 against PROVENANCE.json. Never load a chunk as a complete TGENO.
The manifest.json file supplies the exact asset names, order, lengths and SHA-256
for every part. The catalog's download_reference.py tool verifies each part and
the reconstructed original before making the completed file available.

The five metadata files are individual release assets under their exact names. The
corresponding HO `.anno` file was not separately present locally; official
metadata gives it the same length and MD5 as the included compatibility_HO `.anno`.
A user needing that alternate annotation filename may make an exact copy, with
that mapping documented. It is not an additional independently acquired file.

These individual reference matrices are research source inputs. ZeroThink's
small runtime packs and composition assets are separate filtered aggregates.
Installing this mirror alone does not install an application model, reference
pack builder dependencies, a clinical product or a validated ancestry service.
