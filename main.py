import sys
from stats import get_num_words
from stats import get_num_characters
from stats import get_sorted_dict_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
def print_char_count(sorted_dicts):
    for dict in sorted_dicts:
        print(f"{dict["char"]}: {dict["num"]}")
def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    #book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    char_num_dict = get_num_characters(book_text)
    sorted_dicts_list = get_sorted_dict_list(char_num_dict)
    #print(f"{word_count} words found in the document")
    #print(char_num_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print_char_count(sorted_dicts_list)
main()