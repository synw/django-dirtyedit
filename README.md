Django Dirty Edit
==============

A Django application to edit files from the admin interface. This make it possible for example to let graphic designers edit some css files in the admin interface. 

Install
--------------

	pip install codemirror2
	git clone https://github.com/synw/django-dirtyedit.git && cp -r django-dirtyedit/dirtyedit . && rm -rf django-dirtyedit

Option: django-reversion:

	pip install django-reversion

To disable django-reversion add the setting `USE_REVERSION = False`

Add these to INSTALLED_APPS:

	'codemirror2',
	'dirtyedit',
	'reversion', #optional

Warning
--------------

:warning: When you first time create a file you have to populate its initial content in the admin interface, the application is not going to read the file from the filesystem

Handle with care: its pretty easy to break things with this module! Only give access to it to trusted admin users.

Todo
--------------

- Limit file edition to `templates`, `media` and `static` with maybe an option for extra dirs
- Read the file content on creation and populate initial data into the instance