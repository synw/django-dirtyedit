Django Dirty Edit
==============

[![Build Status](https://travis-ci.org/synw/django-dirtyedit.svg?branch=master)](https://travis-ci.org/synw/django-dirtyedit)

A Django application to edit files from the admin interface. This make it possible for example to let graphic 
designers edit some css files in the admin interface. 

Install
--------------

	pip install codemirror2
	git clone https://github.com/synw/django-dirtyedit.git && cp -r django-dirtyedit/dirtyedit . && rm -rf django-dirtyedit

Option: django-reversion:

	pip install django-reversion

To enable django-reversion add the setting `USE_REVERSION = True`

Add these to INSTALLED_APPS:

	'codemirror2',
	'dirtyedit',
	'ckeditor', #optional
	'reversion', #optional

Settings
--------------

Default values are:

- `EDIT_MODE = 'code'` : uses codemirror. To use ckeditor set it to `'html'`   
- `CODEMIRROR_KEYMAP = 'default'` : set it to what your like. Ex: `'vim'`, `'emacs'`
- `AUTHORIZED_PATHS = ('/media', '/static', '/templates')` : writing in theses directories and their subdirectories is authorized.
- `EXCLUDED_PATHS = ()` : to explicitly exclude some paths. Ex: `('/media/private')`
- `CAN_CREATE_FILES = False` : set it to `True` to allow file creation
- `USE_REVERSION = False` : set it to True to use reversion

Warning
--------------

Handle with care: its pretty easy to break things with this module! Only give access to it to trusted admin users.

Todo
--------------

- Handle file types to auto setup codemirror highlighting mode