# MusicFoldersChecker.py

import os

def folder_contents(path, gen=True, get_root=True):
	lst = [ ]
	for root, dirs, files in os.walk(path):
		for file in files:
			if gen: yield [root, file]
			else: lst.append([root, file])
	if not gen:
		return lst


def main():
	internal_dir = 'C:\\Users\\jeffv\\Music'
	external_dir = 'W:\\Music'

	internal_files = sorted(folder_contents(internal_dir))
	external_files = sorted(folder_contents(external_dir))

	print('Missing from internal:')
	for x in list(set([x[1] for x in external_files]) - set([x[1] for x in internal_files])): 
		for i in external_files:
			if x in i: print(i)

	print('\nMissing from external:')
	for x in list(set([x[1] for x in internal_files]) - set([x[1] for x in external_files])): 
		for i in internal_files:
			if x in i: print(i)

	# file_formats = [ ]
	# files = internal_files + external_files
	# for x in files:
	# 	end = x.split('.')[-1].lower()
	# 	if end not in file_formats: 
	# 		file_formats.append(end)
	# print(file_formats)

if __name__ == '__main__':
	main()