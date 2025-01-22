import sys
from pathlib import Path


def get_project_root():
    return Path(__file__).parent.parent


def get_path(file_name):
    return Path(f"{get_project_root()}/data/{file_name}")


def parse_input(arguments):
    # argument 0 represents script name

    if len(arguments) == 2:
        return '', arguments[1]

    elif len(arguments) == 3:
        return arguments[1], arguments[2]

    else:
        print("Invalid arguments!")
        sys.exit(1)


def get_total_bytes_from_path(path):
    bytes_in_file = path.read_bytes()
    byte_count = len(bytes_in_file)
    return byte_count


def get_total_lines_from_path(path):
    line_count = sum(1 for line in path.open(encoding='utf-8'))
    return line_count


def get_total_words_from_path(path):
    content = path.read_text(encoding='utf-8')
    words = content.split()
    word_count = len(words)
    return word_count


def get_total_characters_from_path(path):
    content = path.read_text(encoding='utf-8')
    char_count = len(content) + content.count('\n') # adding content count probably to count \n as 2 characters instead of 1
    return char_count


def get_total_bytes_from_content(content):
    byte_count = len(content.encode('utf-8'))  # Encoding content to get bytes
    return byte_count


def get_total_lines_from_content(content):
    line_count = content.splitlines()  # Splitting content by lines
    return len(line_count)


def get_total_words_from_content(content):
    words = content.split()  # Splitting content by spaces
    word_count = len(words)
    return word_count


def get_total_characters_from_content(content):
    char_count = len(content)  # Directly counting characters in content
    return char_count


def print_result(counts, filename):
    print(f'{' '.join(map(str, counts))} {filename}')