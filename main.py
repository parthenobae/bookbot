from stats import get_word_count
from stats import get_char_count

def get_book_text(filepath):
    text = ""
    with open(filepath) as file:
       text = file.read();
    return text 


def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    char_count = get_char_count(text)

    word_count = get_word_count(text)
    for key in char_count:
        print(f"'{key}': {char_count[key]}")

    # print(f"Found {word_count} total words")

main()
