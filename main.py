from stats import count_words, count_chararacters_apparitions, sort_dicts
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
     
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    word_count = count_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_apparitions = count_chararacters_apparitions(book_text)
    sorted_dict = sort_dicts(char_apparitions)
    for item in sorted_dict:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["count"]}")

    print("============= END ===============")
main()
