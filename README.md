# ccwc_fraxhost - A Custom Word Count Tool

## Overview

`ccwc_fraxhost` (Coding Challenges Word Count) is a custom implementation of the Unix `wc` command-line tool. It counts bytes, lines, words, and characters in a given text file or from standard input, following the Unix philosophy of simplicity and composability.

## Features

- Supports counting:
  - Bytes (`-c`)
  - Lines (`-l`)
  - Words (`-w`)
  - Characters (`-m`)
- Supports multiple options combined.
- Works without options (defaults to `-c -l -w`).
- Supports reading from standard input.

## Installation

You can install `ccwc_fraxhost` via `pip` from PyPI:

```sh
$ pip install ccwc_fraxhost
```

Ensure Python is installed (for Python implementation) or compile the code if using another language.

## Usage

Count bytes in a file

```sh
$ ccwc -c test.txt
342190 test.txt
```

Count lines in a file

```sh
$ ccwc -l test.txt
7145 test.txt
```

Count words in a file

```sh
$ ccwc -w test.txt
58164 test.txt
```

Count characters in a file

```sh
$ ccwc -m test.txt
339292 test.txt
```

Default usage (counts lines, words, and bytes)

```sh
$ ccwc test.txt
7145  58164  342190 test.txt
```

Read from standard input

```sh
$ cat test.txt | ccwc -l
7145
```

## Implementation
This project is implemented following best practices in software engineering. It efficiently reads files, processes input, and returns results in a format consistent with the Unix wc tool.

## Contributing
Contributions are not currently accepted. Feel free to use and modify the tool for personal use.

## License
This project is licensed under the MIT License.

## Acknowledgments
Inspired by Unix wc and Coding Challenges.