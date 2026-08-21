# Hugging Face Upload Guide

This GitHub repository is the project home for Termbase Commons. Large termbase data files should not be committed directly to this repository.

The actual termbase data files should be uploaded to one Hugging Face Dataset data hub.

## Target dataset repository

```text
https://huggingface.co/datasets/jinukcha/termbase-commons-data
```

Create it here:

```text
https://huggingface.co/new-dataset
```

Recommended settings:

```text
Owner: jinukcha
Repository name: termbase-commons-data
Repository type: Dataset
Visibility: Private first, then Public after validation
License: Other
License name: multiple-source-specific-licenses
License URL: https://raw.githubusercontent.com/jinukcha/termbase-commons/main/DATA_LICENSES.md
```

## Files to upload

Use the prepared upload package. After extracting it, upload the contents of:

```text
termbase-commons-data/
```

The Hugging Face dataset repository should contain:

```text
README.md
LICENSES.md
.gitattributes
data/medicine/loinc/loinc_terms_multilingual_dedup.csv.gz
licenses/loinc/LOINC_short_license.txt
licenses/loinc/LOINC_LICENSE_FULL.txt
metadata/termbase_catalog.csv
metadata/termbase_catalog.json
metadata/license_manifest.csv
metadata/license_manifest.json
metadata/source_manifest.csv
metadata/source_manifest.json
metadata/loinc_deduplication_report.json
metadata/loinc_locale_columns.csv
metadata/loinc_official_field_coverage.csv
metadata/loinc_validation_report.json
metadata/package_validation_report.json
```

The main downloadable LOINC termbase file is:

```text
data/medicine/loinc/loinc_terms_multilingual_dedup.csv.gz
```

## Important wording

Use:

```text
LOINC official raw-derived multilingual termbase
공식 LOINC raw 기반 다국어 단어집
```

Avoid:

```text
Official LOINC dictionary
Certified LOINC termbase
LOINC official multilingual dictionary
```

The source LOINC distribution is official, but the released CSV is a derived wide multilingual termbase generated from source-supplied fields.

## What not to upload here

Do not upload the large CSV or CSV.GZ file to this GitHub repository. GitHub should keep only project documents, catalog files, schemas, and validation scripts.
