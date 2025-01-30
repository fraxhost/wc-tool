import sys
from pathlib import Path


def get_path(file_path):
    return Path(file_path)


def parse_input(arguments):
    # argument 0 represents script name
    # argument 1 represents tool_name
    # argument 2 represents file_name
    if len(arguments) == 2:
        return arguments[1], ''
    elif len(arguments) == 3:
        return arguments[1], arguments[2]
    else:
        print("Invalid arguments!")
        sys.exit(1)


def get_total_bytes_from_path(path):
    bytes_in_file = path.read_bytes()
    byte_count = len(bytes_in_file)
    return byte_count


def get_total_bytes_from_content(content):
    byte_count = len(content.encode('utf-8'))  # Encoding content to get bytes
    return byte_count


def get_total_lines_from_path(path):
    content = Path(path).read_text(encoding='utf-8')
    get_total_lines_from_content(content)


def get_total_lines_from_content(content):
    lines = content.splitlines()  # Splitting content by lines
    line_count = len(lines)
    return line_count


def get_total_words_from_path(path):
    content = path.read_text(encoding='utf-8')
    get_total_words_from_content(content)


def get_total_words_from_content(content):
    words = content.split()  # Splitting content by spaces
    word_count = len(words)
    return word_count


def get_total_characters_from_path(path):
    content = path.read_text(encoding='utf-8')
    get_total_characters_from_content(content)


def get_total_characters_from_content(content):
    char_count = len(content)  # Directly counting characters in content
    return char_count


def print_result(counts, filename):
    print(f'{' '.join(map(str, counts))} {filename}')