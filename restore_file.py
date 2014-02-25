#!/usr/bin/env python

import client
import sys

def main():
	if len(sys.argv) < 2:
		sys.exit('Usage: restore_file.py <path>')
	filepath = sys.argv[1]
	c = client.create_client()
	revisions = c.revisions(filepath)
	if not revisions[0]['is_deleted']:
		print 'File is not deleted'
		return

	rev = revisions[1]['rev']
	c.restore(filepath, rev)

if __name__ == '__main__':
	main()

