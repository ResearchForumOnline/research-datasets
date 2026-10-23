# ZeroThink composition reference assets: GRCh37

This package contains unchanged public-aggregate-derived model data and the GPL
worker, with a new scoped manifest. It contains 345,907 marker rows, frequency
columns for 21 reference groups and 16 projection dimensions. It has no individual
genotype rows, owner results, personal array masks, client database or credentials.
GRCh38 weights and index are not in this release. Historical `model.json` also
describes the larger original bundle; the scoped manifest is authoritative for the
builds included here. Read NOTICE.txt and the licenses directory.

The package does not include a Python runtime. The original runtime used Python
3.9, NumPy1.26.4 and quadprog0.1.13. Operators must prepare a supported local Python
with NumPy and quadprog separately, under their dependency licenses. Candidate dependency recipe (not freshly install-tested here): a Python 3.11
virtual environment with NumPy 1.26.4 and quadprog 0.1.13.
Installing dependencies can access package registries and is a separate operator step.

For the scoped-manifest-capable ZeroThink PHP loader, set these deployment variables:

```text
ZEROTHINK_COMPOSITION_BUNDLE=/absolute/path/to/composition-grch37-2026.09.05
ZEROTHINK_COMPOSITION_PYTHON=/absolute/path/to/your-venv/bin/python
```

The interpreter must be explicitly configured; it is not supplied by this package.
The integration retains Linux `/usr/bin/timeout`, `/usr/bin/prlimit`, PHP SQLite3
and proc_open requirements. Windows execution is not provided by that integration.
Private temporary request storage must already be configured by the application.

The scoped manifest SHA-256 is
`5330a197b6b0203cbb985ebfd50bf68ae1fbcd8f1dc190933329d27db33d2747`.
The legacy loader that pins `94a2a30e...` and every old runtime/GRCh38 file will
reject this scoped package. Use the separately reviewed scoped loader update;
do not bypass integrity checks or copy the historical full-runtime manifest here.

Before running any analysis, verify SHA256SUMS.txt and inspect the public reference
catalogue. Installation/source availability and an executable runtime are separate
states. GRCh38 input must be withheld before collecting model calls.

This staging performed hash/schema/numeric-range checks only. No participant data
or inference was processed. Model coefficients depend on the chosen references;
chromosome omission is sensitivity, not a confidence interval. The source input
coverage floor is 50,000 markers across at least15autosomes, not an accuracy claim.

The scoped loader contract and checks are documented at:
https://github.com/ResearchForumOnline/ZeroThink/blob/main/docs/COMPOSITION_BUNDLES.md
