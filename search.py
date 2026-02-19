'''
Takes the path to a json file containing search index and a query string, returns list of file paths matching the query
'''
import sys
from engine import search
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("words", nargs="+")
    parser.add_argument("--or", dest="mode", action="store_const", const="or")
    parser.add_argument("--and", dest="mode", action="store_const", const="and", default="and")

    args = parser.parse_args()

    if len(sys.argv) > 1:
        search(args.words, mode=args.mode)
    else:
        print("Program usage: python search.py <query1> <query2> ... [--and | --or] (Default is --and)")
        sys.exit(1)

if __name__ == "__main__":
    main()