# Hugging Face Upload Guide

This GitHub repository is the project home for Termbase Commons. Large termbase data files should not be committed directly to this repository.

The actual LOINC termbase data file should be uploaded to a Hugging Face Dataset repository.

## Target dataset repository

```text
https://huggingface.co/datasets/jinukcha/loinc-multilingual-termbase
```

Create it here:

```text
https://huggingface.co/new-dataset
```

Recommended settings:

```text
Owner: jinukcha
Repository name: loinc-multilingual-termbase
Repository type: Dataset
Visibility: Private first, then Public after validation
License: Other / LOINC License
```

## Files to upload

From the starter pack, upload the contents of:

```text
huggingface_dataset_repos/loinc-multilingual-termbase/
```

The Hugging Face dataset repository should contain:

```text
README.md
LOINC_short_license.txt
LOINC_LICENSE_FULL.txt
data/loinc_terms_multilingual_dedup.csv.gz
metadata/loinc_deduplication_report.json
metadata/loinc_locale_columns.csv
metadata/loinc_official_field_coverage.csv
metadata/loinc_validation_report.json
```

The main downloadable termbase file is:

```text
data/loinc_terms_multilingual_dedup.csv.gz
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
