# PalindromeNumbers.py

from math import log


# mode='count': ceiling is a max amount of numbers to be generated
# mode='max'  : ceiling is a ceiling to stop generating number when reached
def palndr_nums(ceiling, base=10, mode='smart'):
	if mode == 'max':
		for x in range(ceiling):
			if is_palndr(x): 
				yield x
	elif mode == 'count':
		count = 0
		for x in range(int(1e20)):
			if count == ceiling: 
				break
			else:
				if is_palndr(x):
					count += 1
					yield x
	elif mode == 'smart':
		for x in range(1, ceiling+1):
			num = cat(x, rev(x))
			print(num)
			if num < ceiling:
				yield num
			else:
				break

# reverse a number
def rev(n):
	r = 0
	while n > 0:
		r *= 10
		r += n % 10
		n //= 10
	return r

# concatenate two ints
def cat(n, m):
	return n * 10**(int( log(m, 10) ) + 1) + m

def is_palndr(n):
	n = str(n)
	return n[::-1] == n

def main():
	print([x for x in palndr_nums(199)])

if __name__ == '__main__':
	main()
	# import timeit
	# print(timeit.timeit(
	# 	'[x for x in palndr_nums(199, mode="count")]', 
	# 	setup='from __main__ import palndr_nums'), number= 1000)