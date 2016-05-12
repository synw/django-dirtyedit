# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from codemirror2.widgets import CodeMirrorEditor
from dirtyedit.models import FileToEdit
from dirtyedit.conf import CODEMIRROR_KEYMAP, EDIT_MODE

if EDIT_MODE == 'html':
    from ckeditor_uploader.widgets import CKEditorUploadingWidget


class DirtyEditForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(DirtyEditForm, self).__init__(*args, **kwargs)
        if 'django_admin_bootstrapped' in settings.INSTALLED_APPS:
            self.fields['content'].label = ''
    
    if EDIT_MODE == 'html':
        content = forms.CharField(widget=CKEditorUploadingWidget())
    elif EDIT_MODE == 'code':
        content = forms.CharField(
                                  widget=CodeMirrorEditor(options={
                                                             'mode':'htmlmixed',
                                                             'width':'1170px',
                                                             'indentWithTabs':'true', 
                                                             'indentUnit' : '4',
                                                             'lineNumbers':'true',
                                                             'autofocus':'true',
                                                             #'highlightSelectionMatches': '{showToken: /\w/, annotateScrollbar: true}',
                                                             'styleActiveLine': 'true',
                                                             'autoCloseTags': 'true',
                                                             'keyMap': CODEMIRROR_KEYMAP,
                                                             'theme':'blackboard',
                                                             }, 
                                                             modes=['css', 'xml', 'javascript', 'htmlmixed'],
                                                             )
                                  
                                  )
    else:
        content = forms.CharField(widget=forms.Textarea)
    content.required = False

    
    class Meta:
        model = FileToEdit
        exclude = ('created','edited', 'editor')
