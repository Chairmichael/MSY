#!/usr/bin/env 
# SteamLevel.py


# target, current = steam lvl
def get_xp(target, current=1):
    mult = 1
    total_xp = 0
    for l in range(1, target+1):
        if l >= current:
            total_xp += mult * 100
        if l % 10 == 0: mult += 1
    return total_xp

def get_lvl_cost(target, current=1, rate=20, key_rate=2, currency='MONEY'):
    xp = get_xp(target, current)
    if currency == 'MONEY':
        return xp / (rate * 100 / key_rate)
    elif currency == 'KEYS':
        return xp / (rate * 100)



def main():
    print(get_lvl_cost(target=100, current=74, currency='KEYS'))

if __name__ == '__main__':
    import os, sys
    main()
