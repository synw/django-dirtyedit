# -*- coding: utf-8 -*-

import os
from django.conf import settings
from django.contrib import admin
from django.contrib import messages
from codemirror2.widgets import CodeMirrorEditor
from dirtyedit.models import FileToEdit


@admin.register(FileToEdit)
class FileToEdit(admin.ModelAdmin):
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.attname == "content":
            kwargs['widget'] = CodeMirrorEditor(options={'mode': 'htmlmixed','indentWithTabs':'true','lineNumbers':'true'}, modes=['css', 'xml', 'javascript', 'htmlmixed'])
        return super(FileToEdit, self).formfield_for_dbfield(db_field, **kwargs)
    
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




