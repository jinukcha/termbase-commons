# Contributing

## Accepted sources

A source must be one of the following:

1. Official terminology distribution
2. Government or standards-body publication
3. Clearly licensed open terminology dataset
4. Project-owned curated termbase with documented provenance

## Not accepted

- Machine translated glossaries without source proof
- LLM-generated missing terms
- Scraped pages without redistribution permission
- Directional source/target translation-memory exports as the canonical termbase
- Data with ambiguous license status

## Required CSV shape

Use wide multilingual columns:

```text
term_en_us
term_ko_kr
term_zh_cn
term_fr_fr
term_es_mx
```

Do not use canonical directional fields:

```text
source_term
target_term
source_locale
target_locale
```

## Review checklist

- Source is documented
- License is documented
- No generated translations were introduced
- Locale columns are explicit
- Empty values are left empty, not guessed
- Duplicate rows are removed using a documented rule
