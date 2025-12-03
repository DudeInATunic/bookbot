import sys

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        content = file.read()
    return content

def main(book_path):
    book_text = get_book_text(book_path)
    
    from stats import get_num_words
    num_words = get_num_words(book_text)
    
    from stats import count_characters
    character_counts = count_characters(book_text)

    from stats import sorter
    sorted_character_counts = sorter(character_counts)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

#Iterate through your sorted list of character dictionaries. For each character, check if it's an alphabetical character. If it is, print it in the specified char: count format.

    for entry in sorted_character_counts:
        char = entry["char"]
        num = entry["num"]
        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]
    main(book_path)