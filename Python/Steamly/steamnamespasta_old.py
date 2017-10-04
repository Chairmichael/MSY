from math import ceil

max_lines = 9
target_length = ceil(len(phrase) / max_lines) + 1
print(target_length)
lines = [ ]
line = ''
# done = False
# history = [target_length]

# while not done:
for i, word in enumerate(phrase.split()):
	try: 
		if len(phrase.split()[i+1]) + len(line) < target_length:
			line = line.strip() + ' ' + word
		else:
			lines.append(line)
			line = word
	except IndexError:
		line = line + ' ' + word
		lines.append(line)

	# if len(lines) > 9:
	# 	target_length += 1
	# elif len(lines) < 9:
	# 	target_length -= 1
	# else: done = True
	# history.append(target_length)
	# if :
	# 	pass

for x in lines:
	print(x)
print(len(lines))