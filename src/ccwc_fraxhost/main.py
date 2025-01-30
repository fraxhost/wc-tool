import sys
from .ccwc import ccwc_file, ccwc_content
from .utils import parse_input


def main():
    if not sys.stdin.isatty():
        input_content = ''

        for line in sys.stdin:
            input_content += line

        tool_function, file_name = parse_input(sys.argv)
        ccwc_content(tool_function, input_content)
    else:
        tool_function, file_path = parse_input(sys.argv)
        ccwc_file(tool_function, file_path)


if __name__ == "__main__":
    main()