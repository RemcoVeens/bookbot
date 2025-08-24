from stats import count_words, statistics
import sys

def get_book_text(file_path) -> str:
    with open(file_path, "r") as f:
        return f.read()

def main(book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_contents = get_book_text(book_path)
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_contents)} total words")
    print("--------- Character Count -------")
    stats = statistics(book_contents)
    for item in stats:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main(sys.argv[1])
