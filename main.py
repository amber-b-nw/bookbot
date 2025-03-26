import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        sys.exit(1)

from stats import count_words

from stats import character_count

from stats import sort_char

def main():
    path = sys.argv[1]
    text = get_book_text(path)
    word_count = count_words(text)
    characters = character_count(text)
    sorted_characters = sort_char(characters)
    print("=" * 12, " Bookbot ", "=" * 12)
    print(f"Analyzing book found at {path}...")
    print("-" * 11, " Word Count ", "-" * 11)
    print(f"Found {word_count} total words")
    print("-" * 10, " Character Count ", "-" * 10)
    for entry in sorted_characters:
        print(f"{entry['char']}: {entry['count']}")
    print("=" * 12, " End ", "=" *12)

main()

