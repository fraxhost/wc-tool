from pathlib import Path
import utils


def parse_input():
    prompt = input('')  # Read user input
    words = prompt.split()

    if len(words) == 2:
        return words[0], '', words[1]

    if len(words) == 3:
        return words[0], words[1], words[2]

    exit()


def validate_input(tool_name, tool_function, file_name):
    if tool_name != 'ccwc':
        print('invalid tool name')
        exit()
    if tool_name == 'exit':
        print('ccwc terminated')
        exit()


def get_path(file_name):
    return Path(f"{utils.get_project_root()}/data/{file_name}")


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


def main():
    while True:
        tool_name, tool_function, file_name = parse_input()
        validate_input(tool_name, tool_function, file_name)
        path = get_path(file_name)

        try:
            if tool_function == '-c':
                counts = [get_total_bytes(path)]
                print_result(counts, file_name)
            elif tool_function == '-l':
                counts = [get_total_lines(path)]
                print_result(counts, file_name)
            elif tool_function == '-w':
                counts = [get_total_words(path)]
                print_result(counts, file_name)
            elif tool_function == '-m':
                counts = [get_total_characters(path)]
                print_result(counts, file_name)
            elif tool_function == '':
                counts = [get_total_lines(path), get_total_words(path), get_total_bytes(path)]
                print_result(counts, file_name)

        except FileNotFoundError:
            print("Error: The file does not exist.")
            # exit()

        except PermissionError:
            print("Error: Permission denied when trying to read the file.")
            # exit()

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            # exit()


if __name__ == "__main__":
    main()