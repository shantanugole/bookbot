import sys
from stats import get_word_count, get_char_count, get_sorted_char_count

def main():
    # Check if the user provided a file path
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)     # Exit with error code 1



    # Define the file path
    filepath = sys.argv[1]

    try:
        # Get word and character counts
        num_words = get_word_count(filepath)
        char_count = get_char_count(filepath)
        sorted_char_count = get_sorted_char_count(char_count)

        # Print output in required format
        print("=" * 30 + " BOOKBOT " + "=" * 30)
        print(f"Analyzing book found at {filepath}...")
        print("-" * 30 + " Word Count " + "-" * 30)
        print(f"Found {num_words} total words")  # Corrected variable name
        print("-" * 29 + " Character Count " + "-" * 29)

        for item in sorted_char_count:
            print(f"{item['character']}: {item['count']}")

        print("=" * 30 + " END " + "=" * 30)

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        sys.exit(1)   # Exit with error

# Ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
