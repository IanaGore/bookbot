from stats import get_num_words, count_characters, sort_dictionary
import sys


args = sys.argv



def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def main(args):
    book_path = args[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_counts = count_characters(text)
    sorted_dictionary = sort_dictionary(character_counts)
    print("============== BOOKBOT ===========")
    print(f"Analyzing book found at {book_path}...")
    print("--------- Word Count ---------")
    print(f" Found {num_words} total words.")
    print("--------- Character Count ---------")
    for char in sorted_dictionary:
        print(f" {char['char']}: {char['num']}")
    

print(args)
if len(args) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(args)

    