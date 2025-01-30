import sys
from .ccwc import ccwc_file, ccwc_content
from .utils import parse_file_input, parse_standard_input


def main():
    if not sys.stdin.isatty():
        input_content = ''

        for line in sys.stdin:
            input_content += line

        tool_function = parse_standard_input(sys.argv)
        ccwc_content(tool_function, input_content)
    else:
        file_path, tool_function = parse_file_input(sys.argv)
        ccwc_file(tool_function, file_path)


if __name__ == "__main__":
    main()