# -*- coding: utf-8 -*-

from django import forms
from codemirror2.widgets import CodeMirrorEditor


class FileEditForm(forms.ModelForm):
    content = forms.CharField(widget=CodeMirrorEditor(options={'mode': 'htmlmixed','indentWithTabs':'true','lineNumbers':'true'}, modes=['css', 'xml', 'javascript', 'htmlmixed']))
    content.required = False
    location = forms.CharField()
    
    def __init__(self, *args, **kwargs):
        super(FileEditForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = 'Html'
        self.fields['location'].label = 'Url'
    
    