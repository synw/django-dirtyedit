Django Dirty Edit
==============

[![Build Status](https://travis-ci.org/synw/django-dirtyedit.svg?branch=master)](https://travis-ci.org/synw/django-dirtyedit)

A Django application to edit files from the admin interface. This make it possible for example to let graphic 
designers edit some css files in the admin interface. 

Install
--------------

	pip install django-dirtyedit

Add these to INSTALLED_APPS:

	'dirtyedit',
	'ckeditor',
	'codemirror2',
	'reversion',

Note: `codemirror2` and `reversion` should be loaded after `dirtyedit`

Settings
--------------

Default values are:

- `DIRTYEDIT_EDIT_MODE = 'code'` : uses codemirror. To use ckeditor set it to `'html'`   
- `DIRTYEDIT_CODEMIRROR_KEYMAP = 'default'` : set it to what your like. Ex: `'vim'`, `'emacs'`
- `DIRTYEDIT_AUTHORIZED_PATHS = ('/media', '/static', '/templates')` : writing in theses directories and their subdirectories is authorized.
- `DIRTYEDIT_EXCLUDED_PATHS = ()` : to explicitly exclude some paths. Ex: `('/media/private')`
- `DIRTYEDIT_CAN_CREATE_FILES = False` : set it to `True` to allow file creation
- `DIRTYEDIT_USE_REVERSION = True` : set it to False to disable reversion

Warning
--------------

Handle with care: its pretty easy to break things with this module! Only give access to it to trusted admin users.

Todo
--------------

- Handle file types to auto setup codemirror highlighting mode