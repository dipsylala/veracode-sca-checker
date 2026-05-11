# Veracode SCA Catalog Checker

A GitHub Actions workflow that monitors the total number of entries in the [Veracode SCA (SourceClear) catalog](https://api.sourceclear.com/catalog/search?q=) and opens an issue whenever the count changes.

## How it works

1. Every day at 9am GMT, the workflow calls `https://api.sourceclear.com/catalog/search?q=` and reads `metadata.hits` — the total number of library entries in the catalog.
2. It prepends a new history row to `.github/catalog-count-history.csv` in `timestamp_utc,total` format (most recent first).
3. It compares the current total to the previous top history row.
4. If the total changed (or no baseline exists yet), it opens a GitHub issue showing the previous value, current value, and the difference.

## Repository structure

```
.github/
  workflows/
    sca-catalog-check.yml   # The daily workflow
  catalog-count-history.csv # Auto-committed history (newest row first)
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
| `issues: write` | Open an issue when the count changes |

No additional secrets are required.
