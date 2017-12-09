#!/usr/bin/env python
"""
    Runs as a command line script
"""
import sys
import requests


def get_word(word):
    """
        Searches for word and gets a response from urbandictionary API
    """
    req = requests.get(
        'http://api.urbandictionary.com/v0/define?', {'term': word})
    return req.json()['list']


def print_definitions(word):
    """
        Loops through first 3 results and prints them out to console
    """
    definitions = get_word(word)
    for i in range(0, 3):
        obj = definitions[i]

        print(f'Word: {obj["word"]}')
        print(f'Definition: {obj["definition"]}')
        print(f'Score: {obj["thumbs_up"] - obj["thumbs_down"]}')
        print(f'Ayys: {obj["thumbs_up"]} | Nayys: {obj["thumbs_down"]}\n')


def get_input():
    """
        Parent function for this script.
        Gets input string from user and returns 3 definitions.
    """
    while True:
        words_to_lookup = input('')
        if not words_to_lookup:
            words_to_lookup = input(
                'You didn\'t enter anything.  Please enter a search string: ')
        elif words_to_lookup == 'exit':
            sys.exit()
        elif words_to_lookup:
            print(f'You entered "{words_to_lookup}" and these are the top 3 results:\n')
            print_definitions(words_to_lookup)
        else:
            print(f'Did not recognize command {words_to_lookup} \n')


get_input()
