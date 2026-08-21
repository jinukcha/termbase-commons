# LOINC source notes

## Source

- Source name: LOINC
- Source release used by the initial dataset: LOINC 2.82
- Official website: https://loinc.org
- Official downloads: https://loinc.org/downloads
- License: https://loinc.org/license/

## Dataset produced in this collection

The first dataset in this collection is a wide multilingual termbase derived from the official LOINC 2.82 distribution.

Important wording:

- Correct: `official LOINC raw-derived multilingual termbase`
- Correct Korean wording: `공식 LOINC raw 기반 다국어 단어집`
- Avoid: `official LOINC dictionary`, `certified LOINC termbase`, or any wording that implies Regenstrief Institute or the LOINC Committee published this derived CSV.

## Transformation policy

The released CSV uses only source-supplied fields from the official LOINC distribution.

Not used:

- machine translation
- LLM completion
- embedding-based alignment
- automatic similarity mapping
- inferred missing locale values
- source/target directional pair tables

## Current public payload

Recommended Hugging Face data hub:

```text
jinukcha/termbase-commons-data
```

Recommended Hugging Face data file:

```text
data/medicine/loinc/loinc_terms_multilingual_dedup.csv.gz
```

Rows: `192310`
Locale term columns: `22`
