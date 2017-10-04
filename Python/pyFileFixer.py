# py_file_labeler.py


def prepend_file(fd, text, count):
	path = '\\'.join(fd.name.split('\\')[:-1])
	with open(f'{path}\\temp{count}.py', 'w') as new_file:
		new_file.write(f'{text}\n\n')
		for line in fd:
			# todo: fix the writing of lines
			# todo: removes the contents of the old file
			new_file.write(line)

def main():
	top = 'C:\\Users\\jeffv\\Documents\\GitHub\\ProjectEuler\\Python\\Incomplete'
	count = 0
	for r, d, files in os.walk(top):
		for f in files:
			if f.endswith('.py'): 
				with open(f'{r}\\{f}', 'w+') as file:
					if f not in file.readline():
						prepend_file(file, f'# {f}', count)
						count += 1


if __name__ == '__main__':
	import os
	main()
