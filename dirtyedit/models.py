# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class FileToEdit(models.Model):
    edited = models.DateTimeField(editable=False, auto_now=True, verbose_name=_(u'Edited'))
    created = models.DateTimeField(editable=False, auto_now_add=True)
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, related_name='+', null=True, on_delete=models.SET_NULL, verbose_name=u'Edited by')   
    relative_path = models.CharField(max_length=255, null=True, unique=True, verbose_name=_(u"File path"))
    # to select the mode in codemirror: must figure out how to access this field value in admin.ModelAdmin first
    #file_type = models.CharField(max_length=60, blank=True, help_text=_(u'See here for a list: http://codemirror.net/mode/'))
    content = models.TextField(null=True, blank=True)
    
    
    class Meta:
        verbose_name=_(u'File to edit')
        verbose_name_plural = _(u'Files to edit')
        
    def __unicode__(self):
        return str(self.relative_path)
    

    

        
        
