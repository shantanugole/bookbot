def get_book_text(filepath):
    """Reads a file and returns its contents as a string."""
    with open(filepath, 'r', encoding='utf-8') as file:
        file_contents = file.read()
    return file_contents


def get_word_count(filepath):
    """Reads a text file and gets the number of words"""
    book_text = get_book_text(filepath)
    return len(book_text.split())

def get_char_count(filepath):
    chars = get_book_text(filepath).lower()

    chars_count = {}

    for char in chars:              # Iterate over lowercase text
        if char in chars_count:
            chars_count[char] += 1        # Increment count if exists
        else:
            chars_count[char] = 1         # Initialize count for new character

    return chars_count


def get_sorted_char_count(char_count_dict):
    """Takes a dictionary of character counts and returns a sorted list of dictionaries."""
    sorted_chars = [
        {"character": char, "count": count}
        for char, count in char_count_dict.items() if char.isalpha()
    ]
    
    sorted_chars.sort(key=lambda x: x["count"], reverse=True)  # Sort by count in descending order
    return sorted_chars
