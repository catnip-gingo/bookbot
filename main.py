import sys
from stats import get_num_words
from stats import get_num_letters
from stats import sort_on
from stats import insert_keys

if len(sys.argv) != 2:

    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters = get_num_letters(text)
    list_dict= insert_keys(letters)
    list_dict.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- WordCount ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in list_dict:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
    


def get_book_text(path):
    with open(path) as f:
        return f.read()




main()
print(sys.argv)