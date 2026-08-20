# Termbase Commons

Termbase Commons is an open collection of translation-ready multilingual termbases derived from official or clearly licensed terminology sources.

The project is intended for translators, localization engineers, CAT tool users, terminology researchers, and LLM/RAG builders who need clean multilingual term files.

## Principles

- Official or clearly licensed sources only
- No machine translation
- No LLM-generated term completion
- No embedding-based inferred alignment
- Wide multilingual CSV format
- Source license preserved per dataset
- One downloadable `csv.gz` per termbase whenever possible

## First dataset

The starter dataset is:

```text
LOINC Multilingual Termbase
```

Recommended data host:

```text
Hugging Face Dataset: termbase-commons/loinc-multilingual-termbase
```

Recommended data file:

```text
data/loinc_terms_multilingual_dedup.csv.gz
```

## Repository roles

```text
GitHub
= project home, policy, catalog, schemas, validation scripts, issue tracking

Hugging Face Dataset
= actual data distribution
```

Do not commit large termbase payloads directly to this GitHub repository. Use Hugging Face Dataset repos or GitHub Releases for binary/download assets.

## Korean summary

Termbase Commons는 공식 또는 명확하게 라이선스가 확인된 terminology source를 기반으로 만든 번역용 다국어 단어집 모음입니다.

기계번역, LLM 보충, 임베딩 유사도 기반 자동 정렬은 사용하지 않습니다.
