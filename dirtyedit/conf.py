# -*- coding: utf-8 -*-

from django.conf import settings


edit_modes = ('html','code')

authorized_paths = ('/media', '/static', '/templates')

EDIT_MODE = getattr(settings, 'DIRTYEDIT_EDIT_MODE', edit_modes[1])
CODEMIRROR_KEYMAP = getattr(settings, 'DIRTYEDIT_CODEMIRROR_KEYMAP', 'default')

USE_REVERSION = getattr(settings, 'DIRTYEDIT_USE_REVERSION', True)

AUTHORIZED_PATHS = getattr(settings, 'DIRTYEDIT_AUTHORIZED_PATHS', authorized_paths)
EXCLUDED_PATHS = getattr(settings, 'DIRTYEDIT_EXCLUDED_PATHS', ())

CAN_CREATE_FILES = getattr(settings, 'DIRTYEDIT_CAN_CREATE_FILES', False)