from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class DirtyEditConfig(AppConfig):
    name = "dirtyedit"
    verbose_name = _(u"Files editor")
    
    def ready(self):
        pass
        
        