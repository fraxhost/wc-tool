import sys
from ccwc import ccwc_file, ccwc_content
from utils import parse_input


def main():
    if not sys.stdin.isatty():
        input_content = ''
        for line in sys.stdin:
            input_content += line
        tool_function, file_name = parse_input(sys.argv)
        print('1', tool_function, file_name, sys.argv)
        ccwc_content(tool_function, input_content)
        print('3', tool_function, file_name)
    else:
        tool_function, file_name = parse_input(sys.argv)
        print('11', tool_function)
        ccwc_file(tool_function, file_name)
        print('13', tool_function)


if __name__ == "__main__":
    main()