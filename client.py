#!/usr/bin/env python

import sys
import dropbox
import json

# Get your app key and secret from the Dropbox developer website
CONFIG_FILE = 'config.json'
COOKIE_FILE = 'cookie.json'

def get_token(app_key, app_secret):
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
		access_token = get_token(APP_KEY, APP_SECRET)
		client = dropbox.client.DropboxClient(access_token)
		cookie_content = json.dumps(access_token)
		open(COOKIE_FILE, 'w').write(cookie_content)
	
	print 'linked account: ', client.account_info()
	return client

def main():
	c = create_client()

if __name__ == '__main__':
	main()
