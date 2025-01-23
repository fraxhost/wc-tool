from pathlib import Path


def get_project_root():
    return Path(__file__).parent.parent


def get_path(file_name):
    return Path(f"{get_project_root()}/data/{file_name}")


def parse_input():
    prompt = input('')  # Read user input
    words = prompt.split()

    if len(words) == 2:
        return words[0], '', words[1]

    if len(words) == 3:
        return words[0], words[1], words[2]

    exit()


def validate_input(tool_name):
    if tool_name != 'ccwc':
        print('invalid tool name')
        exit()
    if tool_name == 'exit':
        print('ccwc terminated')
        exit()


def get_total_bytes(path):
    bytes_in_file = path.read_bytes()
    byte_count = len(bytes_in_file)
    return byte_count


def get_total_lines(path):
    line_count = sum(1 for line in path.open(encoding='utf-8'))
    return line_count


def get_total_words(path):
    content = path.read_text(encoding='utf-8')
    words = content.split()
    word_count = len(words)
    return word_count


def get_total_characters(path):
    content = path.read_text(encoding='utf-8')
    char_count = len(content) + content.count('\n') # adding content count probably to count \n as 2 characters instead of 1
    return char_count


def print_result(counts, filename):
    print(f'{' '.join(map(str, counts))} {filename}')