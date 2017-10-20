#!/usr/bin/env 
# TeamCoverage.py

class Pokemon(object):
    """A Pokemon"""
    def __init__(self, name, stats=None):
        self.name = name
        self.stats = stats
        if stats is None:
            _get_stats()

    def _get_stats(self):
        pass




def pokemon_from_file(f):
    pokemon = [ ]
    with open(f, 'r') as file:
        pokemon.append(file.readline().split(' ')[0]) # get first poke
        for line in file:
            if line.strip() == '':
                pokemon.append(next(file).split(' ')[0])
    return pokemon

def main(args):
    team = pokemon_from_file(args.file)


if __name__ == '__main__':
    import os, sys, argparse, textwrap
    from lxml import html
    import requests, webbrowser

    desc = 'A pokemon type coverage script'
    parser = argparse.ArgumentParser(description=desc)
    helpstr = 'The file for the smogon pokemon team'
    parser.add_argument('file', metavar='F', type=str, help=helpstr)

    args = parser.parse_args()
    main(args)
