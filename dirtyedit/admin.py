# -*- coding: utf-8 -*-

import os
from django.conf import settings
from django.contrib import admin
from django.contrib import messages
from codemirror2.widgets import CodeMirrorEditor
from dirtyedit.models import FileToEdit


USE_REVERSION=getattr(settings, 'USE_REVERSION', True)
if USE_REVERSION:
    from reversion.admin import VersionAdmin
    
admin_class=admin.ModelAdmin
if USE_REVERSION:
    admin_class=VersionAdmin
@admin.register(FileToEdit)
class FileToEditAdmin(admin_class):
    save_on_top = True
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
            
    def formfield_for_dbfield(self, db_field, **kwargs):
        obj_id = kwargs['request'].META['PATH_INFO'].strip('/').split('/')[-1]
        obj = FileToEdit.objects.get(pk=int(obj_id))
        print str(obj)
        if db_field.attname == "content":
            kwargs['widget'] = CodeMirrorEditor(options={
                                                         'mode':'htmlmixed',
                                                         'indentWithTabs':'true', 
                                                         'indentUnit' : '4',
                                                         'lineNumbers':'true',
                                                         'autofocus':'true',
                                                         #'highlightSelectionMatches': '{showToken: /\w/, annotateScrollbar: true}',
                                                         'styleActiveLine': 'true',
                                                         'autoCloseTags': 'true',
                                                         'keyMap':'vim',
                                                         'theme':'blackboard',
                                                         }, 
                                                         modes=['css', 'xml', 'javascript', 'htmlmixed'],
                                                         )
            kwargs['label'] = 'File content'
        return super(FileToEditAdmin, self).formfield_for_dbfield(db_field, **kwargs)





