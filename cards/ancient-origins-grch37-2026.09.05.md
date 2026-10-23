# ZeroThink verified ancient reference pack: GRCh37

The exact `ancient_origins.verified.sqlite` file is the corrected September5,2026
pack, SHA-256 `55dedcd44c68edda7ff6ee2f8d2b01ea8b60df0cc430c324a6757859a2f047cc`.
It contains six research groups,30,826 common loci and184,956 aggregate frequency
rows. It includes source metadata for37 published ancient individuals and no
individual genotype table. See NOTICE.txt, original source manifest and validation
receipt. CITATIONS.json supplies the verified citation for ten original source
records with a missing DOI placeholder; the SQLite bytes are unchanged. The earlier unverified pack is superseded and is not included.

The actual ZeroThink PHP application loads `web/data/packs/ancient_origins.sqlite`
relative to its source root. After checking checksums, install a COPY of the verified
SQLite under that exact filename. Keep this release's original filename and source
manifest for provenance; the installed filename change does not change its bytes.
The loader requires PHP SQLite3 and the aligned marker schema; this pack satisfies
the documented schema. Configure the web server so the data directory cannot be
served as a raw download endpoint. Customer/raw input storage is separate and
remains private under the application's existing policy.

This installs only the ancient reference dataset. Modern ancestry, archaic tags,
ClinVar/health, graves, lineage and composition are separate optional packs. Their
availability must be reported honestly; missing packs are not supplied by this file.
A metadata/schema/hash audit was completed, not a personal DNA analysis or a new
independent validation of ancestry accuracy.
