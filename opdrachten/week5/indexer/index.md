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

In the distro ([download](dist/indexer.zip)) you'll find a file and a directory:

- `stopwords.txt` contains a list of words that can be ignored by the indexing system. (So, we don't have to index a gazillion occurrences of, for example, the word "the".)
- `texts` contains various text files for testing your implementation.

The code revolves around a **word index** that contains for each word in the text the position where the word occurs. A "dictionary" in Python is well-suited to store such an index. You can build your dictionary like so, linking each word to a *list* of line numbers:

    {
        "dinner": [ 258, 289, 1096, ... ],
        "guest": [ ... ],
        "table": [ ... ],
        ...
    }

This means that the **type** of your index can be declared like this:

    Index = dict[str, list[int]]

or if you use a somewhat older version of Python:

    from typing import List, Dict
    Index = Dict[str, List[int]]


## Code structure

    # indexer.py: Find every occurence of a word in a text.
    # Usage: python indexer.py <text-file>
    # Displays all line numbers where the word occurs.

    import sys, string

    def read_stopwords():
        """
        Read all the stopwords from the file "stopwords.txt". Returns the
        collection of stopwords in a list; each stopword should be stripped
        of whitespace.
        """

    def convert_word(word):
        """
        Strips a word from all puncuation, whitespace, and digits. Then
        converts the word into all lower case.
        """
        return word.strip(string.punctuation + \
                          string.whitespace + \
                          string.digits).lower()

    def create_index(filename, stopwords):
        """
        Reads `filename` and returns an index.
        * For each word in the file, the index contains a record of all line
          numbers where this word occurs.
        * Words are converted to lowercase and stripped of punctuation,
          whitespace and digits before adding to the index.
        * Empty strings and stopwords are ignored and not indexed.
        """

    def search_index(word, book_index):
        """
        Find the word in book_index. Returns a list of the line numbers where
        word occurs.
        """

    def show_search_results(line_numbers):
        """
        Displays the search results (line_numbers) nicely, like in the
        examples.
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


## Testing your program

- Test your code by running it on the example at the top of the page.

- Try some examples for yourself.

- What happens if you search a word that does not appear in the text?

- What happens if you search the word "the"?
