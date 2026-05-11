"""
Explores the structure of https://api.sourceclear.com/catalog/search?q=
and prints key fields with their types and example values.
"""

import json
import urllib.request


API_URL = "https://api.sourceclear.com/catalog/search?q="


def fetch(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode())


def print_structure(obj, indent: int = 0, max_items: int = 2):
    pad = "  " * indent
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, (dict, list)):
                print(f"{pad}{key!r}: ({type(value).__name__})")
                print_structure(value, indent + 1, max_items)
            else:
                print(f"{pad}{key!r}: {type(value).__name__} = {value!r}")
    elif isinstance(obj, list):
        print(f"{pad}[list of {len(obj)} items]")
        for i, item in enumerate(obj[:max_items]):
            print(f"{pad}  [{i}]:")
            print_structure(item, indent + 2, max_items)
        if len(obj) > max_items:
            print(f"{pad}  ... ({len(obj) - max_items} more items)")


def main():
    print(f"Fetching: {API_URL}\n")
    data = fetch(API_URL)

    print("=" * 60)
    print("TOP-LEVEL KEYS:", list(data.keys()))
    print("=" * 60)
    print_structure(data)

    # Highlight the key tracking field
    hits = data.get("metadata", {}).get("hits")
    print("\n" + "=" * 60)
    print(f"TRACKING FIELD  →  metadata.hits = {hits:,}")
    print("=" * 60)


if __name__ == "__main__":
    main()
