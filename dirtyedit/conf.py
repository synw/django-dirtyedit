# -*- coding: utf-8 -*-

from django.conf import settings


EDIT_MODES = (
              'html',
              'code',
              )

EDIT_MODE = getattr(settings, 'DIRTYEDIT_EDIT_MODE', EDIT_MODES[1])
CODEMIRROR_KEYMAP = getattr(settings, 'DIRTYEDIT_CODEMIRROR_KEYMAP', 'default')

USE_REVERSION=getattr(settings, 'DIRTYEDIT_USE_REVERSION', False)