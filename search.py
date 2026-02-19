"""
Searches the index using one or more query words.
Default mode is AND. Use --mode or to match any word.
"""
import sys
from engine import search
import argparse

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Search files using the index.",
        usage="python search.py QUERY [QUERY ...] [--mode and|or]",
        epilog="Example: python search.py ramen tokyo --mode or",
    )
    parser.add_argument("query", nargs="+", metavar="QUERY", help="One or more query words")
    parser.add_argument("--mode", metavar="MODE", choices=["and", "or"], default="and", help="Search mode: 'and' (default) or 'or'")

    args = parser.parse_args()
    try:
        print(f"Searching for: {args.query} with mode: {args.mode}")
        matching_files = search(args.query, mode=args.mode)
    except (FileNotFoundError, ValueError) as e:
        print(e)
        sys.exit(1)
    
    if matching_files:
        print("Files matching the query:")
        for file in sorted(matching_files):
            print(file)
    else:
        print("No files match the query.")



if __name__ == "__main__":
    main()