# -*- coding: utf-8 -*-

import os
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.contrib import messages
from codemirror2.widgets import CodeMirrorEditor
from dirtyedit.models import FileToEdit
from dirtyedit.forms import DirtyEditForm
from dirtyedit.utils import read_file
from dirtyedit.conf import USE_REVERSION


admin_class=admin.ModelAdmin
if USE_REVERSION:
    admin_class=VersionAdmin
@admin.register(FileToEdit)
class FileToEditAdmin(admin_class):
    form = DirtyEditForm
    save_on_top = True
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
        #~ save file
        file_content = obj.content
        something_wrong = False
        try:
            filepath=settings.BASE_DIR+obj.relative_path
            #~ check if the file exists
            if not os.path.isfile(filepath):
                messages.error(request, "File "+obj.relative_path+" not found - nothing saved on disk")
                something_wrong = True
            else:
                #~ write the file
                filex = open(filepath, "w")
                filex.write(file_content)
                filex.close()
        except Exception, e:
            messages.error(request, str(e))
            something_wrong = True
        if not something_wrong:
            obj.save()  
    
    def get_changeform_initial_data(self, request):
        if 'fpath' in request.GET.keys():
            filepath = request.GET.get('fpath')
            status_msg, msg, filecontent = read_file(request, filepath)
            if status_msg is True:
                messages.success(request, msg)
                return {'content': filecontent, 'relative_path':filepath}
            else:
                if status_msg == 'warn':
                    messages.warning(request, msg)
                    return
                elif status_msg == 'infos':
                    messages.info(request, msg)
                    return
                messages.error(request, msg)
                return
        return




