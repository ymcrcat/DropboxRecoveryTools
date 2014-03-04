#!/usr/bin/env python

import client
import sys
import fileinput

def delete_file(c, filepath):
	c.file_delete(filepath)
	print 'Deleted:', filepath

def main():
	c = client.create_client()
	for line in fileinput.input():
		try:
			delete_file(c, line.strip())
		except Exception, e:
			print >> sys.stderr, e

if __name__ == '__main__':
	main()

