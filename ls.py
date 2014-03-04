#!/usr/bin/env python

import client
import sys
from optparse import OptionParser

def filter_by_date(files, dirs_only=False, date=None):
	if dirs_only:
		files = [f for f in files if f['is_dir']]
	if date:
		files = [f for f in files if f['modified'].find(date) >= 0]
	return files

def main():
	parser = OptionParser()
	parser.add_option('-d', '--dirs', action='store_true', dest='dirs_only', default=False)
	parser.add_option('--date', dest='date', default=None)
	(options, args) = parser.parse_args()
	search_root = args[0]
	c = client.create_client()
	filter_func = lambda files: filter_by_date(files, options.dirs_only, options.date)
	files = client.find_files(c, search_root, False, filter_func)

if __name__ == '__main__':
	main()
