#!/usr/bin/env python

import client
import sys
from time import sleep

RATE_LIMITING_DELAY = 0.05

def find_deleted_files(c, path, date=None):
	meta = c.metadata(path, include_deleted=True)
	files = [f for f in meta['contents'] if not f['is_dir']]
	deleted_files = [f for f in files if f.has_key('is_deleted')]
	if date:
		deleted_files = [f for f in deleted_files if f['modified'].find(date) >= 0]
	dirs  = [d['path'] for d in meta['contents'] if d['is_dir']]
	for f in deleted_files:
		print f['path']
	for d in dirs:
		deleted_files.extend(find_deleted_files(c, d, date))
		sleep(RATE_LIMITING_DELAY)
	return deleted_files

def main():
	search_root = sys.argv[1]
	if len(sys.argv) > 2:
		date = sys.argv[2]
		print 'Filtering by date:', date
	else:
		date = None
	c = client.create_client()
	deleted_files = find_deleted_files(c, search_root, date)

if __name__ == '__main__':
	main()
