# indexer.py: Find every occurence of a word in a text.
# Usage: python indexer.py <text-file>
# Displays all line numbers where the word occurs.

import sys, string

def read_stopwords():
    """
    Read all the stopwords from the file "stopwords.txt".
    Returns the collection of stopwords; each stopword should be stripped
    of whitespace.
    """

def convert_word(s):
    """
    Strips a word from all puncuation, whitespace, and digits. Then converts
    the word into all lower case.
    """
    return s.strip(string.punctuation + \
                   string.whitespace + \
                   string.digits).lower()

def create_index(filename, stopwords):
    """
    Reads `filename` and returns an index.
    * For each word in the file, the index contains a record of all line numbers where this word occurs.
    * Words are converted to lowercase and stripped of punctuation, whitespace and digits.
    * Empty strings and stopwords are ignored and not indexed.
    """

def search_index(word, book_index):
    """
    Find the word in book_index. Returns all the lines where word occurs.
    """

def show_search_results(line_numbers):
    """
    Displays the search results (line_numbers) nicely.
    """

def user_input_search(book_index):
    """
    User input loop. For every line provided as input, convert it, find the line
    numbers, and show results.
    """
    line = input("\nEnter search term: ")
    while line not in ["q", "Q", "quit", ""]:
        searched_word = convert_word(line)
        line_numbers = search_index(searched_word, book_index)
        show_search_results(line_numbers)
        line = input("\nEnter search term: ")

if __name__ == "__main__":

    # Read the stopwords from the stopwords file
    stopwords = read_stopwords()

    if len(sys.argv) < 2:
        print("No arguments provided.", \
              "Please specifiy the file you want to search.")
        sys.exit()

    # Uses first command line argument as infile to build an index of words
    book_index = create_index(sys.argv[1], stopwords)

    print("Index built for", sys.argv[1]+".",
            "Type the word you want to look up.")

    # Start the user input loop
    user_input_search(book_index)
