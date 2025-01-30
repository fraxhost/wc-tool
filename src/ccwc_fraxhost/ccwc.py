from . import utils


def ccwc_file(tool_function, file_path):
    path = utils.get_path(file_path)
    file_name = path.name

    try:
        if tool_function == '-c':
            counts = [utils.get_total_bytes_from_path(path)]
            utils.print_result(counts, file_name)
        elif tool_function == '-l':
            counts = [utils.get_total_lines_from_path(path)]
            utils.print_result(counts, file_name)
        elif tool_function == '-w':
            counts = [utils.get_total_words_from_path(path)]
            utils.print_result(counts, file_name)
        elif tool_function == '-m':
            counts = [utils.get_total_characters_from_path(path)]
            utils.print_result(counts, file_name)
        elif tool_function == '':
            counts = [utils.get_total_lines_from_path(path), utils.get_total_words_from_path(path),
                      utils.get_total_bytes_from_path(path)]
            utils.print_result(counts, file_name)

    except FileNotFoundError:
        print("Error: The file does not exist.")
        # exit()

    except PermissionError:
        print("Error: Permission denied when trying to read the file.")
        # exit()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # exit()


def ccwc_content(tool_function, content):
    try:
        if tool_function == '-c':
            counts = [utils.get_total_bytes_from_content(content)]
            utils.print_result(counts, '')
        elif tool_function == '-l':
            counts = [utils.get_total_lines_from_content(content)]
            utils.print_result(counts, '')
        elif tool_function == '-w':
            counts = [utils.get_total_words_from_content(content)]
            utils.print_result(counts, '')
        elif tool_function == '-m':
            counts = [utils.get_total_characters_from_content(content)]
            utils.print_result(counts, '')
        elif tool_function == '':
            counts = [utils.get_total_lines_from_content(content), utils.get_total_words_from_content(content),
                      utils.get_total_bytes_from_content(content)]
            utils.print_result(counts, '')

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # exit()
