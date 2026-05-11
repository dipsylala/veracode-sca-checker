# Veracode SCA Catalog Checker

A GitHub Actions workflow that monitors the total number of entries in the [Veracode SCA (SourceClear) catalog](https://api.sourceclear.com/catalog/search?q=) and opens an issue on every run.

## How it works

1. Every day at 9am GMT, the workflow calls `https://api.sourceclear.com/catalog/search?q=` and reads `metadata.hits` — the total number of library entries in the catalog.
2. It prepends a new history row to `last-catalog-count.txt` in `timestamp_utc,total` format (most recent first).
3. It compares the current total to the previous top history row.
4. It opens a GitHub issue on every run, showing whether the value changed, stayed the same, or established a baseline.

## Repository structure

```
.github/
  workflows/
    sca-catalog-check.yml   # The daily workflow
last-catalog-count.txt      # Auto-committed history (newest row first)
scripts/
  explore_catalog_api.py    # One-off script to inspect the full API response structure
```

## Triggering manually

The workflow includes a `workflow_dispatch` trigger, so you can run it on demand from the **Actions** tab in GitHub.

## Permissions

The workflow uses the built-in `GITHUB_TOKEN` with the following permissions:

| Permission | Reason |
|------------|--------|
| `contents: write` | Commit the updated history file |
| `issues: write` | Open an issue on each run |

No additional secrets are required.
