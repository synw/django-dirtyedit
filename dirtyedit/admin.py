# -*- coding: utf-8 -*-

import os
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.contrib import messages
from codemirror2.widgets import CodeMirrorEditor
from dirtyedit.models import FileToEdit
from dirtyedit.forms import DirtyEditForm
from dirtyedit.utils import read_file, write_file
from dirtyedit.conf import USE_REVERSION


admin_class=admin.ModelAdmin
if USE_REVERSION:
    from reversion.admin import VersionAdmin
    admin_class=VersionAdmin
@admin.register(FileToEdit)
class FileToEditAdmin(admin_class):
    form = DirtyEditForm
    fieldsets = (
            (None, {
                'fields': ('content',)
            }),
            (None, {
                'fields': ('relative_path',)
            }),
            )
    
    def save_model(self, request, obj, form, change):
        #~ record editor
        if getattr(obj, 'editor', None) is None:
            obj.editor = request.user
        status, msg = write_file(obj.relative_path, obj.content)
        if msg <> '':
            if status == 'warn':
                messages.warning(request, msg)
            elif status == 'infos':
                messages.info(request, msg)
            else:
                messages.error(request, msg)
        return super(FileToEditAdmin, self).save_model(request, obj, form, change)
    
    def get_changeform_initial_data(self, request):
        if 'fpath' in request.GET.keys():
            filepath = request.GET.get('fpath')
            status_msg, msg, filecontent = read_file(filepath)
            if status_msg is True:
                messages.success(request, msg)
                return {'content': filecontent, 'relative_path':filepath}
            else:
                if status_msg == 'warn':
                    messages.warning(request, msg)
                    return
                elif status_msg == 'infos':
                    messages.info(request, msg)
                    return {'relative_path':filepath}
                messages.error(request, msg)
                return
        return




