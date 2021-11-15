import sys, string



def read_stopwords():
    with open("stopwords.txt") as f:
        stopwords = [s.strip() for s in f.readlines()]
        # Assignment 1A
        pass

def filter_word(word, stopwords):
    # Assignment 1B
    pass



def build_index(filename, stopwords):
    # Assignment 2A
    pass

def search_index(word, book_index):
    # Assignment 2B
    pass

def show_search_results(line_numbers):
    # Assignment 2C
    pass


###############
# Staring code
###############

def convert_word(s):
    """
    Strips a word from all puncuation, whitespace, and digits. Then converts
    the word into all lower case.
    """
    return s.strip(string.punctuation + string.whitespace + \
                   string.digits).lower()

def read_gutenberg_file(filename, stopwords):
    """
    Reads `filename` and returns a list of tuples.

    The list of tuples consists of words and the linenumber that that specific
    word was found on. Each word is first stripped from punctuation, whitespace,
    and digits, and is also converted to lower case and checked to not be in the
    list of `stopwords`.

    NOTE: Understanding this code is not essential to completing this exercise
    """
    processed_words = []

    with open(filename) as f:
        started = False

        # Read the lines in the file and give them a number
        for i, line in enumerate(f.readlines()):
            if line[:9] == "*** START":
                started = True
            elif line[:7] == "*** END":
                # Stop reading
                break

            elif started:
                # i starts at 0, while our line numbers should start at 1
                line_number = i+1

                # Split the line into a list of strings (splits on spaces)
                for s in line.split():
                    word = convert_word(s)

                    # Filter empty strings and stop words
                    if len(word) > 0 and not filter_word(word, stopwords):
                        processed_words.append((word, line_number))

    return processed_words

def user_input_search(book_index):
    """
    User input loop. For every line provided as input, convert it, find the line
    numbers, and show results.
    """
    for line in sys.stdin:
        searched_word = convert_word(line)
        line_numbers = search_index(searched_word, book_index)
        show_search_results(line_numbers)

if __name__ == "__main__":
    # Read the stopwords from the stopwords file
    stopwords = read_stopwords()

    try:
        if len(sys.argv) == 1:
            print("No arguments provided.", \
                    "Please specifiy the file you want to search.")
            raise KeyboardInterrupt

        # Uses first command line argument as infile to build an index of words
        book_index = build_index(sys.argv[1], stopwords)

        print("Index built for", sys.argv[1]+".",
                "Type the word you want to look up.")

        # Start the user input loop
        user_input_search(book_index)

    except KeyboardInterrupt:
        print("\nQuitting the program.")
        sys.exit()
