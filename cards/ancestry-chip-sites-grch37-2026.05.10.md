# ZeroThink ancestry chip-sites frequency pack

This is the preserved historical ZeroThink 0.2.2-chip-sites aggregate reference, recorded on 10 May 2026. It contains **2,639,288 population-frequency rows across 535,138 variant loci** in GRCh37, for five broad public 1000 Genomes groups: AFR, AMR, EAS, EUR and SAS. This recovered pack is separate from the newer composition and ancient-origins packs.

The exact existing payload is `data/ancestry_core_chip_sites.sqlite.gz` (71,527,683 bytes). Decompression yields `ancestry_core_chip_sites.sqlite` (609,112,064 bytes). Both SHA-256 hashes are recorded in PROVENANCE.json. Streaming decompression was verified against the original SQLite; historical bytes were preserved unchanged.

## Contents and privacy review

There are three tables: `ancestry_reference_markers` (2,639,288 frequency records), `data_sources` (one public source record), and `pack_meta` (seven build entries). Marker fields are coordinate identifier, chromosome, position, reference/alternate nucleotide, build, population, frequency, marker weight and public source labels. The historical column named `rsid` actually contains `lowercase-chromosome:position` identifiers, not dbSNP rsIDs. Every identifier was checked against its chromosome and position. All alleles are single A/C/G/T bases; all population fields use the five listed groups. All text-column domains and all metadata values were reviewed. There are no individual sample IDs, genotype calls, per-person call-status/coverage masks, user/client/account identifiers, credentials or private filesystem paths. The `local_path` metadata field holds the public upstream URL.

The original locus-selection metadata describes a union of common MyHeritage/AncestryDNA chip positions. The data retain only deduplicated, unattributed public loci and population frequencies, without individual calls or individual missingness. Marker weights range from 1.72 to 4.0 and are identical across population rows for each variant. Original chip-selection inputs and the weighting formula were not recovered, so exact builder reproduction is not claimed. No proprietary chip manifest is included.

## Provenance and reuse

The recorded input is the [1000 Genomes Phase 3 all-genome sites VCF](https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.wgs.phase3_shapeit2_mvncall_integrated_v5c.20130502.sites.vcf.gz). Its source-checksum field reads `streamed-not-stored`; a source-file hash and fresh independent frequency comparison were not verified. The preserved local payload hashes are verified.

The [IGSR reuse policy](https://www.internationalgenome.org/IGSR_disclaimer/) states that 1000 Genomes Project data are available without embargo following final publication and requests appropriate citation. IGSR also notes that rights vary between collections; this pack identifies its original Phase 3 source. Cite [The 1000 Genomes Project Consortium, Nature 526, 68-74 (2015)](https://doi.org/10.1038/nature15393), the original source URL and this pack version, following [official citation guidance](https://www.internationalgenome.org/category/citation/). NOTICE.txt preserves attribution. CC0-1.0.txt applies to publisher-owned compilation/documentation rights only; upstream source terms and third-party rights remain applicable. Upstream data are not relabeled as explicitly CC0.

## Use and limitations

Decompress using a standard gzip tool, then verify the expanded SHA-256 `2ad576d26d6ed55277ac881d115fa53e359d8fc7c53ba1387f2f6f969aadf4f0`. This is an SQLite pack with the historical `ancestry_reference_markers` schema. To use it with a loader expecting `ancestry_core.sqlite`, back up any existing pack, confirm current schema/version/coordinate-lookup support, and place the decompressed file at the operator-configured ancestry-core pack path. This audit did not install it or execute inference and does not establish compatibility with every current loader.

SQLite quick_check returned `ok`, with zero freelist pages. Frequencies are within [0,1] (observed 0.0051 to 0.9949); all positions are positive. Actual rows include chromosomes 1-22, X and Y, although original `chromosomes` metadata says `1-22`; this inconsistency is disclosed rather than editing historical bytes. Some loci have fewer than five population rows. No fine-grained ancestry accuracy, medical validity, identity proof or benchmark outcome is established. Missing exact builder/source-checksum/selection inputs limit reproducibility.
