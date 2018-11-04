# mathy.py
# Random math functions

from math import log

def is_prime(n):
	if n == 2 or n == 3: return True
	if n < 2 or not n%2: return False
	if n < 9: return True
	if not n%3: return False
	r = int(n**0.5)
	f = 5
	while f <= r:
		if not n%f: return False
		if not n%(f+2): return False
		f +=6
	return True

# reverse a number
def rev(n):
	r = 0
	while n > 0:
		r *= 10
		r += n % 10
		n //= 10
	return r
	# return int(str(n)[::-1])
	# string verison ~90% slower

# concatenate two ints
def cat(n, m):
	return n * 10**(int( log(m, 10) ) + 1) + m
	# return int(str(n) + str(m)[::-1]) string verison 20% slower
	# t = log(m, 10)
	# l = int( t ) + 1
	# x = 10**l
	# return n * x + m

def main():
	print(f'is_prime(455) = {is_prime(455)}')
	print(f'is_prime(377) = {is_prime(377)}')
	print(f'is_prime(203) = {is_prime(203)}')

if __name__ == '__main__':
	main()