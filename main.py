from stats import get_word_count

def get_book_text(filepath):
    text = ""
    with open(filepath) as file:
       text = file.read();
    return text 


def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)

    word_count = get_word_count(text)
    print(f"Found {word_count} total words")

main()
