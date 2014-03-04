#!/usr/bin/env python

import sys
import dropbox
import json
from time import sleep

# Get your app key and secret from the Dropbox developer website
CONFIG_FILE = 'config.json'
COOKIE_FILE = 'cookie.json'
RATE_LIMITING_DELAY = 0.01

def get_token():
	config = open(CONFIG_FILE, 'r')
	config_data = json.load(config)
	app_key = config_data['app_key']
	app_secret = config_data['app_secret']
	
	flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
	authorize_url = flow.start()

	# Have the user sign in and authorize this token
	authorize_url = flow.start()
	print '1. Go to: ' + authorize_url
	print '2. Click "Allow" (you might have to log in first)'
	print '3. Copy the authorization code.'
	code = raw_input("Enter the authorization code here: ").strip()

	# This will fail if the user enters an invalid authorization code
	access_token, user_id = flow.finish(code)
	return access_token

def create_client():
	try:
		cookie_content = open(COOKIE_FILE, 'r').read()
		access_token = json.loads(cookie_content)
		client = dropbox.client.DropboxClient(access_token)
	except Exception:
		access_token = get_token()
		client = dropbox.client.DropboxClient(access_token)
		cookie_content = json.dumps(access_token)
		open(COOKIE_FILE, 'w').write(cookie_content)
	
	# print 'linked account: ', client.account_info()
	return client

def find_files(c, path, include_deleted=False, filter_func=None):
	meta = c.metadata(path, include_deleted=include_deleted)
	files = [f for f in meta['contents'] if not f['is_dir']]
	if filter_func:
		files = filter_func(files)
	dirs  = [d['path'] for d in meta['contents'] if d['is_dir']]
	for f in files:
		print f['path']
	for d in dirs:
		try:
			files.extend(find_files(c, d, include_deleted, filter_func))
			sleep(RATE_LIMITING_DELAY)
		except Exception, e:
			print >> sys.stderr, 'Failed processing', d
			print >> sys.stderr, e
	return files

def main():
	c = create_client()

if __name__ == '__main__':
	main()
