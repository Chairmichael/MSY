#!/usr/bin/env 
# getdex.py


def main():
    page = requests.get('https://pokemondb.net/pokedex/all')
    tree = html.fromstring(page.content)
    pkmn_list = tree.xpath('//a[@class="ent-name"]/text()')
    [print(x) for x in pkmn_list]



if __name__ == '__main__':
    import os, sys
    from lxml import html
    import requests
    main()
