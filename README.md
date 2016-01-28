Django Dirty Edit
==============

A Django application to edit files from the admin interface. This make it possible for example to let graphic designers edit some css files in the admin interface. 

Install
--------------

	pip install codemirror2 django-reversion
	git clone https://github.com/synw/django-dirtyedit.git && cp -r django-dirtyedit/dirtyedit . && rm -rf django-dirtyedit

Add `'dirtyedit',` , `'reversion',` and `'codemirror2',` to INSTALLED_APPS

Warning
--------------

When you first time create a file you have to populate its initial content in the admin interface, the application is not going to read the file from the filesystem

Handle with care: its pretty easy to break things with this module! Only give access to it to trusted admin users.