import sys
from stats import get_word_count
from stats import get_char_count
from stats import sorted_char_count

def get_book_text(filepath):
    text = ""
    with open(filepath) as file:
       text = file.read();
    return text 


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1] 
    text = get_book_text(filepath)
    char_count = get_char_count(text)

    word_count = get_word_count(text)
    list_count  = sorted_char_count(char_count)
    
    # printing the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for item in list_count:
        if not item["char"].isalpha(): continue
        print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")
main()
