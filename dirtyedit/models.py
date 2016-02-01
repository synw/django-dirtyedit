# -*- coding: utf-8 -*-

import os
from django.conf import settings
from django.db import models
from django.contrib import messages


class FileToEdit(models.Model):
    edited = models.DateTimeField(editable=False, null=True, auto_now=True, verbose_name=u'Edited')
    created = models.DateTimeField(editable=False, null=True, auto_now_add=True)
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, related_name='+', null=True, on_delete=models.SET_NULL, verbose_name=u'Edited by')   
    location = models.CharField(max_length=255, null=True, unique=True, verbose_name=u"File path")
    content = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name=u'File to edit'
        verbose_name_plural = u'Files to edit'
        
    def __unicode__(self):
        return str(self.location)
    

        
        
