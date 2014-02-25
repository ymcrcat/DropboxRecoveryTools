#!/usr/bin/env python

import client
import sys
from time import sleep

RATE_LIMITING_DELAY = 0.05

def find_deleted_files(c, path):
	meta = c.metadata(path, include_deleted=True)
	files = [f for f in meta['contents'] if not f['is_dir']]
	deleted_files = [f['path'] for f in files if f.has_key('is_deleted')]
	dirs  = [d['path'] for d in meta['contents'] if d['is_dir']]
	for d in dirs:
		deleted_files.extend(find_deleted_files(c, d))
		sleep(RATE_LIMITING_DELAY)
	return deleted_files

def main():
	search_root = sys.argv[1]
	c = client.create_client()
	deleted_files = find_deleted_files(c, search_root)
	print '\n'.join(deleted_files)

if __name__ == '__main__':
	main()
