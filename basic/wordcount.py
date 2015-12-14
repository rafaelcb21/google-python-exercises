#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import re

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.


def print_words(filename, *arg):
    dicionario = {}
    list = []
    with open(filename, 'r') as file:
        list_lines = file.readlines()
    line_unic = ' '.join(list_lines)
    word_list = re.sub(r'[^a-zA-Z]+',' ',line_unic).split(' ')
    word_list.pop()
    word_list_lower = [word.lower() for word in word_list]
    for word in word_list_lower:
        dicionario[word] = None
    for word in dicionario.keys():
        count = word_list_lower.count(word)
        dicionario[word] = (word, count)
    for values in dicionario.values():
        list.append(values)
    list_ord_letter = sorted(list)

    if arg[0] == '--count':
        for letter, count in list_ord_letter:
            print(letter, count)
    return list

def print_top(filename):
    list = print_words(filename, None)
    list_top = reversed(sorted(list, key = lambda x : x[-1]))
    counting = 1
    for letter, count in list_top:
        print(letter, count)
        if counting == 20:
            break
        counting += 1
    return

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename, '--count')
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
