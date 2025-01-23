import sys
from ccwc import ccwc


def main():
    # Check if arguments are provided
    if len(sys.argv) > 1:
        # Handle specific arguments
        if sys.argv[1] == "--help":
            print("Usage: ccwc [options]")
            print("--help     Show this help message")
            print("--version  Show version information")
        elif sys.argv[1] == "--version":
            print("ccwc version 1.0")
        else:
            print("Welcome to ccwc!")
            print("You passed the following arguments:", sys.argv[1:])
    else:
        print("Welcome to ccwc! Use '--help' for usage information.")

    ccwc()


if __name__ == "__main__":
    main()