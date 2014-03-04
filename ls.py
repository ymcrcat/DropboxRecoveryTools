#!/usr/bin/env python

import client
import sys

def filter_by_date(files, date=None):
	if date:
		files = [f for f in deleted_files if f['modified'].find(date) >= 0]
	return files

def main():
	search_root = sys.argv[1]
	if len(sys.argv) > 2:
		date = sys.argv[2]
		# print 'Filtering by date:', date
	else:
		date = None
	c = client.create_client()
	filter_func = lambda files: filter_by_date(files, date)
	files = client.find_files(c, search_root, False, filter_func)

if __name__ == '__main__':
	main()
