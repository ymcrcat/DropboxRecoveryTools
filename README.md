Dropbox Recovery Tools
======================
A set of utilities for recovering deleted Dropbox files.

Installation
============
Dropbox Python SDK can be installed using
$ pip install dropbox

Configuration
=============
For the utilities to be authorized to access you Dropbox
you need to create a Dropbox application and provide 
its APP_KEY and APP_SECRET in the config file
(you can grab them at the App Console).
Create a file named config.json with the content

{
	"app_key" : "YOUR_APP_KEY",
	"app_secret" : "YOUR_APP_SECRET"
}

Alternatively you can run
$ ./make_config.sh > config.json
