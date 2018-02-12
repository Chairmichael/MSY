#!/usr/bin/env 
# TeamCoverage.py


def type_effect(type1, type2):
	typing_chart = [
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

class Team(object):
    """A Team of Pokemon"""
    # mons - a list of Pokemon objects
    def __init__(self, mons):
        self.mons = mons
        self.type_coverage = _get_type_coverage()

    def _get_type_coverage(self):
    	pass	

    def from_pkmnsd_file(self, file):
        with open(f, 'r') as file:
            self.mons.append(file.readline().split(' ')[0]) # get first poke
            for line in file:
                if line.strip() == '':
                    self.mons.append(next(file).split(' ')[0])
        return self.mons

class Pokemon(object):
    """A Pokemon"""
    def __init__(self, dex_num, stats=None):
        self.dex_num = dex_num
        self.stats = stats
        self.typing = typing
        if stats is None:
            self._get_stats()

    def (self):
    	pass

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

    debug = True
    if not debug:
	    desc = 'A pokemon type coverage script'
	    parser = argparse.ArgumentParser(description=desc)
	    helpstr = 'The file for the smogon pokemon team'
	    parser.add_argument('file', metavar='F', type=str, help=helpstr)
	    args = parser.parse_args()
	    main(args)
	else:
		dbg_file = open('debug_file', 'w')