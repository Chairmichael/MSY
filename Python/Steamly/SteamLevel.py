# steamlevel.py

total = 0
ceiling = 10
mult = 1
for x in range(1,ceiling+1):
	if x % 10 == 0: mult += 1
	total += mult * 100
print(total)
print(total/800)