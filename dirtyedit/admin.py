# -*- coding: utf-8 -*-

import os
from django.conf import settings
from django.contrib import admin
from django.contrib import messages
from codemirror2.widgets import CodeMirrorEditor
from dirtyedit.models import FileToEdit
from dirtyedit.forms import FileEditForm


USE_REVERSION=getattr(settings, 'USE_REVERSION', True)
if USE_REVERSION:
    from reversion.admin import VersionAdmin
    
admin_class=admin.ModelAdmin
if USE_REVERSION:
    admin_class=VersionAdmin
@admin.register(FileToEdit)
class FileToEdit(admin_class):
    form = FileEditForm
    save_on_top = True
    
    """
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.attname == "content":
            kwargs['widget'] = CodeMirrorEditor(options={'mode': 'htmlmixed','indentWithTabs':'true','lineNumbers':'true'}, modes=['css', 'xml', 'javascript', 'htmlmixed'])
        return super(FileToEdit, self).formfield_for_dbfield(db_field, **kwargs)
    """
    
    fieldsets = (
            (None, {
                'fields': ('content', 'location')
            }),
            )
    
    def save_model(self, request, obj, form, change):
        #~ record editor
        if getattr(obj, 'editor', None) is None:
            obj.editor = request.user
        #~ save file
        file_content = obj.content
        print obj.location
        something_wrong = False
        try:
            filepath=settings.BASE_DIR+obj.location
            #~ check if the file exists
            if not os.path.isfile(filepath):
                messages.error(request, "File "+obj.location+" not found - nothing saved on disk")
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





