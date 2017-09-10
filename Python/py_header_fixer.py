#!/usr/bin/env python
# py_header_fixer.py

import sys, os


def fix(file):
	header = '#!/usr/bin/env python\n# py_header_fixer.py'
	#check if file has header
	#if not write header
	with open(file, 'w') as data:
		pass

def main(dirs):
	header = '#!/usr/bin/env python\n# py_header_fixer.py'
	dirs = 'c:/'
	try:
		for starting_dir in dirs:
			for dir_list in os.walk(starting_dir):
				for file in dir_list[2]:
					if '.PY' in file.upper():
						fix(file)
	except Exception as e:
		raise e

if __name__ == '__main__':
	main(sys.argv)