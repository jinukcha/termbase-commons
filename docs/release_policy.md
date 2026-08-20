# Release policy

## Data payloads

Preferred public payload:

```text
one csv.gz file per termbase
```

Do not commit large data files directly to the GitHub repository. Host data in a Hugging Face Dataset repository.

## Versioning

Use source release version in the dataset description.

## Regeneration rule

The derived CSV must be regenerated from the official or clearly licensed source, using documented scripts. Generated translations or inferred missing terms are not accepted.
