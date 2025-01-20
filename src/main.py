from pathlib import Path
import utils


def parse_input():
    prompt = input('')  # Read user input
    words = prompt.split()

    if len(words) < 3:
        exit()

    return words[0], words[1], words[2]


def validate_input(tool_name, tool_function, file_name):
    if tool_name != 'ccwc':
        print('invalid tool name')
        exit()
    if tool_name == 'exit':
        print('ccwc terminated')
        exit()


def get_path(file_name):
    return Path(f"{utils.get_project_root()}/data/{file_name}")


def get_total_bytes(path, file_name):
    bytes_in_file = path.read_bytes()
    byte_count = len(bytes_in_file)
    return f"{byte_count} {file_name}"

def get_total_lines(path, file_name):
    line_count = sum(1 for line in path.open(encoding='utf-8'))
    return f"{line_count} {file_name}"


def main():
    while True:
        tool_name, tool_function, file_name = parse_input()
        validate_input(tool_name, tool_function, file_name)
        path = get_path(file_name)

        try:
            if tool_function == '-c':
                print(get_total_bytes(path, file_name))
            elif tool_function == '-l':
                print(get_total_lines(path, file_name))

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