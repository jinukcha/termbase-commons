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

## Data hub

Actual termbase payloads are distributed from one Hugging Face Dataset hub:

```text
Hugging Face Dataset: jinukcha/termbase-commons-data
```

Expected data hub URL:

```text
https://huggingface.co/datasets/jinukcha/termbase-commons-data
```

## First dataset

The starter dataset is:

```text
LOINC Multilingual Termbase
```

Recommended data file in the Hugging Face data hub:

```text
data/medicine/loinc/loinc_terms_multilingual_dedup.csv.gz
```

## Repository roles

```text
GitHub
= project home, policy, catalog, schemas, validation scripts, issue tracking

Hugging Face Dataset
= actual data distribution
```

Do not commit large termbase payloads directly to this GitHub repository. Use the Hugging Face Dataset data hub or GitHub Releases for binary/download assets.

## Upload guide

See [`HUGGINGFACE_UPLOAD.md`](HUGGINGFACE_UPLOAD.md) for the exact upload steps for the current data hub package.

## Korean summary

Termbase Commons는 공식 또는 명확하게 라이선스가 확인된 terminology source를 기반으로 만든 번역용 다국어 단어집 모음입니다.

기계번역, LLM 보충, 임베딩 유사도 기반 자동 정렬은 사용하지 않습니다.

실제 단어집 파일은 GitHub에 직접 넣지 않고 Hugging Face Dataset data hub에 `csv.gz` 파일로 배포합니다.
