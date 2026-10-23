# Open research datasets and ZeroThink reference packs

Reviewed datasets, aggregate reference/model packs and reproducibility metadata
published by **Shafaet Brady Hussain / ResearchForumOnline**.

This repository is the small source catalog. The actual datasets are downloadable
GitHub Release assets, with per-pack licenses, provenance, schemas and SHA-256
checksums. Downloading the catalog alone does not download those assets.

## Releases and use

See [the latest dataset release](https://github.com/ResearchForumOnline/research-datasets/releases/latest)
and [`catalog.json`](catalog.json) for exact files, sizes and hashes. Read each
dataset card before using a pack. Original datasets and upstream-derived material
have separate license terms; a repository-wide label does not override them.

```console
python tools/download.py --list
python tools/download.py --pack PACK_ID --destination /path/to/downloads
```

The downloader verifies the catalog's SHA-256 and refuses to replace an existing
file. It does not extract, execute or install a model. The pack README explains
installation and separate runtime requirements. DNA assets cover their stated
genome build only; unavailable builds or missing verification stay unavailable.

## Publication boundary

Each new release is assembled from explicit reviewed file lists. It excludes
private personal/client DNA, target-overlap
caches, private reports, customer/account databases, credentials, private
correspondence, provider-restricted research and installed virtual environments.
The original local collections are preserved.

The separate [AADR v14 reference mirror](https://github.com/ResearchForumOnline/research-datasets/releases/tag/aadr-v14-reference-2026.10.23)
contains **6,010,695,146 bytes across seven unchanged official public files**.
Every file matched the original v14 filename, size and MD5, and has a SHA-256
verification record. These are published individual-level third-party scientific
references, rather than custom author or customer DNA. The authoritative source
is [AADR at Harvard Dataverse](https://doi.org/10.7910/DVN/FFIDCW), released under
CC0 for these unrestricted files. This is a selected HO/compatibility-HO mirror,
not the complete 25-file AADR release. Read the
[reference card and notices](reference-mirrors/aadr-v14/DATASET_CARD.md).

```console
python tools/download_reference.py --list
python tools/download_reference.py --destination /path/to/reference
```

The reference downloader verifies each part and the reconstructed original file.
It refuses existing outputs. The approximately 4.03 GB HO genotype file is split
across release assets to fit the per-asset limit; manual concatenation must follow
manifest order. No private target-overlap caches or local analysis outputs are
included. A public scientific source designation is not an anonymity warranty.

Python environments are represented by dependency recipes rather than copies of
an existing machine's installed environment. The observed Windows recipe in
[`recipes/`](recipes/) is metadata from an older analysis environment, not a
freshly tested cross-platform lockfile or the composition worker runtime.

## Interpretation and evidence

Synthetic curricula and held-out files support software/training experiments;
publishing them does not establish that a model was trained, generalizes or has
novel capabilities. Cards report duplicates, split overlap, filtering and known
evaluation limits. Historical benchmark measurements are small diagnostic runs,
with account/endpoint/configuration/response/error fields excluded.

DNA packs support research and source-comparison software. They do not establish
clinical validity, consumer ancestry accuracy, religion/nationality/community
membership, genealogy or royal descent. Calibration and population coverage
remain separate questions from format and hash integrity.

Privacy review combines provenance, schema/array inspection, explicit allowlists,
pattern scanning and scoped content review. A pattern scan alone is not proof
that a dataset contains no private information. Data not adequately accounted for
is withheld or linked to its upstream source instead of republished.

## Related source

- [ZeroThink application and DNA Lab](https://github.com/ResearchForumOnline/ZeroThink)
- [OpenZero runtime](https://github.com/ResearchForumOnline/OpenZero)
- [Research manuscripts and reproducibility code](https://github.com/ResearchForumOnline/research)

See [LICENSE.md](LICENSE.md) and each pack's license/attribution files.

Read the [publication scope](cards/PUBLICATION_SCOPE.md) for held or excluded
material and the [AI dataset review](AI_DATASETS.md) for overlap, licensing
and legacy-publication details. Dataset cards copied into this catalog are reading
previews; the complete accompanying provenance, notices and referenced files are
inside each corresponding ZIP.

<!-- RELEASE-ASSETS -->

## Downloadable payloads

| Download | ZIP size | Contents |
| --- | ---: | --- |
| [ZeroThink ancient aggregate reference](https://github.com/ResearchForumOnline/research-datasets/releases/download/datasets-2026.10.23/ancient-origins-grch37-2026.09.05.zip) | 5.35 MB | 6 groups; 30,826 common loci; 184,956 aggregate frequency rows |
| [ZeroThink GRCh37 composition assets](https://github.com/ResearchForumOnline/research-datasets/releases/download/datasets-2026.10.23/composition-grch37-2026.09.05.zip) | 98.90 MB | 345,907 markers; 21 reference groups; 16 projection dimensions |
| [Pinned GrafAnc aggregate reference](https://github.com/ResearchForumOnline/research-datasets/releases/download/datasets-2026.10.23/grafanc-reference-aggregate-b5e51c78.zip) | 28.22 MB | 282,424 variant rows; 26 population-frequency columns; upstream sentinels preserved |
| [OpenZero original research curriculum](https://github.com/ResearchForumOnline/research-datasets/releases/download/datasets-2026.10.23/openzero-original-research-v1.zip) | 0.15 MB | 413 SFT; 120 preference; 39 frozen evaluation records |
| [OpenZero reviewed licensed mixtures](https://github.com/ResearchForumOnline/research-datasets/releases/download/datasets-2026.10.23/openzero-reviewed-licensed-mixtures-20260726.zip) | 3.69 MB | 1,870 and 1,921 overlapping variant records |
| [Historical application benchmark metrics](https://github.com/ResearchForumOnline/research-datasets/releases/download/datasets-2026.10.23/research-benchmark-metrics-20260709.zip) | 0.01 MB | 213 diagnostic measurement rows; four CSV files |
| [Synthetic DNA software fixtures](https://github.com/ResearchForumOnline/research-datasets/releases/download/datasets-2026.10.23/synthetic-dna-software-fixtures-2026.09.05.zip) | 5.98 MB | 4 constructed CSV/TXT fixtures; 4,400 / 43,598 / 282,049 / 297,707 rows |
| [ZERO original agent curriculum](https://github.com/ResearchForumOnline/research-datasets/releases/download/datasets-2026.10.23/zero-original-agent-curriculum-v1.zip) | 0.03 MB | 165 original records across two curricula |
| [ZERO original pilot dataset](https://github.com/ResearchForumOnline/research-datasets/releases/download/datasets-2026.10.23/zero-original-pilot-20261009.zip) | 0.24 MB | 100 records; 94 groups; 60/20/20 split |

Sizes use decimal MB. Exact byte lengths and SHA-256 hashes are in catalog.json. The nine packs total **212,515,646 uncompressed bytes** and **142,569,332 ZIP bytes**, in addition to the **6,010,695,146-byte** public AADR reference mirror above.
