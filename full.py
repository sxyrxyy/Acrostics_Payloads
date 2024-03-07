import argparse
import os
import random

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


def load_words_by_starting_letter(filepath):
    words_by_letter = {}
    with open(filepath, "r") as f:
        for word in f:
            word = word.strip().lower()
            if len(word) > 3:
                starting_letter = word[0]
                if starting_letter not in words_by_letter:
                    words_by_letter[starting_letter] = []
                words_by_letter[starting_letter].append(word.capitalize())
    return words_by_letter


words_by_starting_letter = load_words_by_starting_letter("words.txt")


def generate_random_word(starting_character, words_by_letter):
    words = words_by_letter.get(starting_character.lower(), [])
    if words:
        return random.choice(words)
    else:
        return starting_character


def replace_special_characters(text):
    replaced_text = text
    for char, replacement in special_characters.items():
        replaced_text = replaced_text.replace(char, replacement + " ")
    return replaced_text


def replace_special_with_characters(words):
    special_characters_reversed = {v: k for k, v in special_characters.items()}
    return [special_characters_reversed.get(word.lower(), word) for word in words]


def combine_first_characters(words):
    return ''.join(word[0] for word in words).lower()


def main():
    parser = argparse.ArgumentParser(description='Enter Command')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-cmd', type=str, help='Command (cmd.exe /c whoami)')

    args = parser.parse_args()

    if args.cmd:
        command = args.cmd
    else:
        main()
    encoded_list = []
    decoded_list = []
    for t in command:
        zzz = replace_special_with_characters(t)
        encoded_list.append(generate_random_word(zzz[0], words_by_starting_letter))
    encoded_list.reverse()

    for z in encoded_list:
        decoded_list.append(replace_special_characters(z))

    command = combine_first_characters(decoded_list)[::-1]
    print(f'Command: {command}\n\n')

    if os.path.exists('list.txt'):
        os.remove('list.txt')

    for word in encoded_list:
        print(word)
        with open('list.txt', 'a') as f:
            f.write(word + '\n')


if __name__ == "__main__":
    main()
