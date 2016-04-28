# -*- coding: utf-8 -*-

import os
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages


def read_file(request, filepath):
    filepath=settings.BASE_DIR+filepath
    if not os.path.isfile(filepath):
        messages.error(request, _(u"File %s not found") % (filepath,))
        return
    filex = open(filepath, "r")
    filecontent = filex.read()
    messages.success(request, _(u"File found: data populated"))
    return filecontent
    