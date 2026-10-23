# GrafAnc published aggregate reference dataset

Version: upstream revision `b5e51c78b5004a8388418ce56755bb2f71f24eb5`.
This release preserves the exact upstream compressed reference file. It is a
third-party aggregate reference distributed for use with the recovered research
software, not an original ZeroThink participant dataset or a newly trained model.

| Property | Value |
| --- | --- |
| File | `data/AncSnpPopAFs.txt.gz` |
| Compressed bytes | 28,216,400 |
| SHA-256 | `02f3594c0a674edf683907bb3e4296a4c4b8ed6467059b41237843e7446b9893` |
| Variant rows | 282,424 |
| Coordinate/allele columns | `chr`, `pos_37`, `pos_38`, `rs`, `ref`, `alt` |
| Population-frequency columns | 26 |
| Individual-level rows | None |
| Upstream Git blob SHA-1 | `ee2f5e8eefccd7c613bcc08f7e650d5ef1518cc9` |

The compressed bytes match the pinned source manifest retained during the original
source acquisition. The audit read the data header and every row's field count and
frequency range. No personal upload, owner result, test participant genotype file,
private array mask, executable or third-party runtime is included.

## Special values

The upstream file contains **123 values of `2.0` across 100 variant rows** in its
population columns. These are upstream special values outside the ordinary allele
frequency range. They are preserved exactly. Their semantic subtype was not
independently reconstructed during this audit; do not treat them as probabilities,
clip them to one, or silently normalize them. The pinned upstream
`SampleGenoAncestry.cpp` only includes frequency terms satisfying `0 < p < 1` in
the inspected scoring calculations. Compatible consumers must preserve that
upstream handling rather than assuming every field lies in [0,1].

## Source and license

Source: [GrafAnc](https://github.com/jimmy-penn/grafanc), pinned to the revision
above. The official README identifies this file as the required aggregate
reference. The pinned repository is MIT licensed; retain
`licenses/GrafAnc-MIT.txt`, including Copyright (c) 2025 University of Pennsylvania.
No new restriction or blanket ZeroThink software license replaces that notice.
This redistribution does not grant rights over unrelated participant-level UK
Biobank or other controlled datasets.

## Use and limits

Verify `SHA256SUMS.txt`, then decompress a copy of the file into the `data/`
directory expected by a separately acquired or built compatible GrafAnc program.
The official pinned source documentation explains the executable and HTSlib
requirements. This package does not contain the ZeroThink GrafAnc marker index,
model manifest, native executable or Python composition weights, so this file alone
does not install the complete application model integration.

This is reference data for research and software reproducibility. The audit does
not independently establish ancestry accuracy, consumer calibration, clinical
validity, nationality, religion, community membership or institutional endorsement.
No inference or training was run while staging it. Exact provenance and the
special-value audit are recorded in `PROVENANCE.json`.
