#!/usr/bin/env python

import client
import sys

def filter_deleted_by_date(files, date=None):
	deleted_files = [f for f in files if f.has_key('is_deleted')]
	if date:
		deleted_files = [f for f in deleted_files if f['modified'].find(date) >= 0]
	return deleted_files

def main():
	search_root = sys.argv[1]
	if len(sys.argv) > 2:
		date = sys.argv[2]
		# print 'Filtering by date:', date
	else:
		date = None
	c = client.create_client()
	filter_func = lambda files: filter_deleted_by_date(files, date)
	deleted_files = client.find_files(c, search_root, True, filter_func)

if __name__ == '__main__':
	main()
