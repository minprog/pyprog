# Indexer

Implement an indexing system for text research.

    $ python indexer.py texts/birdman.txt
    Index built for texts/birdman.txt. Type the word you want to look up.

    Enter search term: dinner

    The word "dinner" can be found on lines: 549, 1542.
    
    Enter search term: quit

Such an indexing system is efficient to use because it builds an index of search terms. For each possible search term, some relevant data is stored in the index. So in a way, the index is a representation of the input file. In this assignment, we store the *line numbers* where the word occurs in the text.

       original text                        index                           searches
    |-----------------|              |-----------------|              |-----------------|
    |                 |              | written: 7, 502 |------------->| written?        |
    |   birdman.txt   |------------->| little: 27, 281 | search many  |-----------------|
    |  ~22000 words   |  build once  | slowly: 24, 303 |------------->| dump?           |
    |                 |              | dump: 34        |              |-----------------|
    |-----------------|              | twitch: 42      |------------->| embrace?        |
                                     |-----------------|              |-----------------|

When that index is loaded into memory, it allows us to quickly search the text without re-loading the text or literally searching it from beginning to end. As you might imagine, such a system is very efficient when the index can be loaded once, after which many searches will be run.

## Getting started

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

### Understanding

In the distro you'll find two files and a directory:

- `stopwords.txt` contains a list of words that can be ignored by the indexing system. (So, we don't have to index a gazillion occurrences of, for example, the word "the".)
- `texts` contains various text files for testing your implementation.
- `indexer.py` is your starting code.

The code in `indexer.py` revolves around a **word index** that contains for each word in the text the position where the word occurs. A "dictionary" in Python is well-suited to store such an index. You can build your dictionary like so, linking each word to a *list* of line numbers:

    {
        "dinner": [ 258, 289, 1096, ... ],
        "guest": [ ... ],
        "table": [ ... ],
        ...
    }

This means that the **type** of your index is:

    dict[str, list[int]]

or if you use a somewhat older version of Python:

    from typing import List, Dict
    Dict[str, List[int]]

### Implementation details

The code in `indexer.py` has several predefined functions:

* `read_stopwords()` is partially implemented: it already reads the stop words from the file `stopwords.txt` and stores these in a list. You can complete the function by `return`ing the collection of those stop words.

* `convert_word()` is already implemented for you. It strips a word from all punctuation, whitespace, and digits, and it converts the word to lowercase.

* `create_index()` is a `TODO`. It should create an index for all words in the input file.

    * For each word in the file, the index should contain a record of all line numbers where this word occurs.
    * Words should be cleaned by `convert_words()` before being entered into the index.
    * Empty strings and stop words should not be indexed.

* `search_index()` is a `TODO`. Search the index on a specific word. Return a list of all the lines where the word occurs.

    * The functions `create_index()` and `search_index()` depend on each other.

* `show_search_results()` is a `TODO`. Print the search results like in the example above. You will need to change the function parameters for this, and that's fine!

* `user_input_search()` is already implemented for you. This function takes care of the user interaction. It repeatedly asks the user for a word and calls `search_index()` to find it. This function stops as soon as the user enters an empty string or the text "q", "Q", or "quit"


## Testing your program

- Test your code by running it on the example at the top of the page.

- Try some examples for yourself.

- What happens if you search a word that does not appear in the text?

- What happens if you search the word "the"?
