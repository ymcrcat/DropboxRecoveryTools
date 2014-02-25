#!/usr/bin/env python

import client
import sys
import fileinput

def restore_file(c, filepath):
	revisions = c.revisions(filepath)
	if not revisions[0].has_key('is_deleted') or not revisions[0]['is_deleted']:
		print 'File is not deleted'
		return

	rev = revisions[1]['rev']
	c.restore(filepath, rev)
	print 'Restored:', filepath, 'to revision', rev

def main():
	c = client.create_client()
	for line in fileinput.input():
		restore_file(c, line)

if __name__ == '__main__':
	main()

