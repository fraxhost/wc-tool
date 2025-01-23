from utils import parse_input, validate_input, get_path, print_result, get_total_bytes, get_total_lines, \
    get_total_words, get_total_characters


def ccwc():
    while True:
        tool_name, tool_function, file_name = parse_input()
        validate_input(tool_name)
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
