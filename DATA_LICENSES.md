# Data Licenses

Termbase Commons may index and distribute datasets derived from multiple terminology sources. Data files are not governed by one universal project license.

Each termbase payload keeps its own source-specific license, notice, and redistribution status.

## Current distributed dataset

### LOINC Multilingual Termbase

Applies to:

```text
data/medicine/loinc/loinc_terms_multilingual_dedup.csv.gz
```

License:

```text
LOINC License
```

License URL:

```text
https://loinc.org/license/
```

Source:

```text
https://loinc.org
https://loinc.org/downloads
```

Status:

```text
redistributable_with_notice
```

This dataset is derived from the official LOINC 2.82 distribution. It is not an official product of Regenstrief Institute, the LOINC Committee, or the LOINC organization.

## Rule for future datasets

When a new source is added, add its license and redistribution status to:

```text
metadata/license_manifest.csv
metadata/source_manifest.csv
metadata/termbase_catalog.csv
```

If a source is not redistributable, keep it as `metadata_only` and do not upload the data payload.
