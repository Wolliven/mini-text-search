#Takes the path to a json file containing search index and a query string, returns list of file paths matching the query
import sys
from engine import search

def main(query):
    search(query)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        folder = sys.argv[1:]
        main(folder)
    else:
        print("Program usage: python search.py <query>")
        sys.exit(1)