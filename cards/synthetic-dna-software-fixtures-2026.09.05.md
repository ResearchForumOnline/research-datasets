# ZeroThink constructed DNA software fixtures

Version: `2026.09.05-public-synthetic.1`.
These four datasets contain deliberately constructed calls for parser, feature and
integration checks. They contain no person's DNA, donor genotype rows, owner
results or personalized array masks. Provider-style headers exercise file format
recognition; they are not provider results.

| File | Rows | Bytes | Construction |
| --- | ---: | ---: | --- |
| `synthetic-verification-v3-not-personal.txt` | 4,400 | 110,590 | Generated identifiers, systematic no-calls and constructed calls at reference positions |
| `SYNTHETIC-ancestry-all-features-not-personal.csv` | 43,598 | 1,290,456 | Coordinate union of explicitly constructed feature and regional fixtures |
| `SYNTHETIC-grafanc-reference-not-personal.csv` | 282,049 | 7,088,584 | Seeded independent binomial draws from published aggregate reference frequencies |
| `SYNTHETIC-customer-complete.csv` | 297,707 | 9,876,152 | Combined constructed input with fixed trait-control rows |

All files preserve their original bytes and explicit synthetic labels. Each row
contains a marker identifier, chromosome, coordinate and artificial diploid call;
no-call rows occur in the small TXT fixture. Identifiers may be canonical rsIDs,
explicit synthetic names or chromosome/position coordinates. They are marker
identifiers, not participant identifiers. Every file has one unique coordinate per
row, four fields, and no malformed call rows in the staging check.

## Provenance and verification

The small TXT matches the audited historical `make_synthetic_fixture.py` method:
identifiers `rs900000000 + row_index`, a no-call every seventeenth row and the
specified systematic homozygous/heterozygous pattern. All 4,400 generated
identifiers and relevant patterns were checked. The original reference pack was
not fetched or used to regenerate its locus selection during staging.

The feature union follows `merge_synthetic_ancestry_fixture.py`, which requires
explicit synthetic source labels and merges the locus fixtures by coordinate.
The GrafAnc fixture follows `create_grafanc_synthetic.py`, using seed 20260905 and
independent binomial/HWE draws from published aggregate frequencies. The generators
are available in the public ZeroThink reference-model tool directory; their
historical hashes and links are retained in `PROVENANCE.json`.

For the 297,707-row complete input, 297,700 calls exactly match the previously
constructed source fixtures. The remaining seven are confined to the fixed
trait-control loci in the regression source. Four match its literal default states;
three are other controlled allele states. The original deployment and integration
records explicitly describe this exact fixture as constructed. Its whole-file
constructor was not independently regenerated, and the three overrides are not
claimed to be reproduced from the default regression states. No unexplained loci
outside that fixed trait-control set or evidence of personal genotype input were
found. This limitation is part of the released provenance.

## License and attribution

The synthetic compilation, constructed software data and packaging are released
under **CC BY 4.0**: attribute the ZeroThink project contributors, identify this
release and indicate changes. The full text is in `licenses/CC-BY-4.0.txt`.
Reference-source rights are preserved separately: the published GrafAnc aggregate
reference is MIT licensed with the University of Pennsylvania notice retained;
AADR public reference locus metadata is CC0, and the CC0 text is included. Original
1000 Genomes Phase 3 reference coordinates and allele definitions retain their
source attribution and data reuse policy. Reference attribution and URLs are
recorded in `PROVENANCE.json` and `NOTICE.txt`. No general software license
relicenses these datasets or grants rights over unrelated controlled datasets.

## Intended uses and limits

Use these files to test local import, build/orientation gates, missing calls,
feature wiring, exports and software throughput. They are not an independent
consumer cohort, natural haplotypes, ancestry ground truth, clinical validation,
realistic inheritance simulation or trait-prediction evidence. Independent locus
draws do not reproduce linkage, family relationships or natural population
structure. A model result on these fixtures is a software behavior check.

Verify `SHA256SUMS.txt` before replaying a fixture. Keep the synthetic notices when
sharing modified versions. No personal data or remote APIs are needed to inspect
the files; running optional application features can require separately installed
reference packs and local dependencies. No model inference, training, personal
DNA processing or reference download was run during staging.
