#!/usr/bin/env 
# TeamCoverage.py

class Team(object):
    """A Team of Pokemon"""
    # mons - a list of Pokemon objects
    def __init__(self, mons):
        self.mons = mons

    def from_file(self, file):
        with open(f, 'r') as file:
            self.mons.append(file.readline().split(' ')[0]) # get first poke
            for line in file:
                if line.strip() == '':
                    self.mons.append(next(file).split(' ')[0])
        return self.mons


class Pokemon(object):
    """A Pokemon"""
    def __init__(self, name, stats=None, ):
        self.name = name
        self.stats = stats
        if stats is None:
            self._get_stats()

    def _get_stats(self):
        page = requests.get('https://pokemondb.net/pokedex/all')
        tree = html.fromstring(page.content)
        pkmn_list = tree.xpath('//a[@class="ent-name"]/text()')
        url = 'https://www.serebii.net/{}'

#C:\Users\jeffv\Documents\platteam.txt
def main(args):
    pkmn_team = Team()


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
