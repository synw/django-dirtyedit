# -*- coding: utf-8 -*-

import os
from django.conf import settings
from django.utils.translation import ugettext as _
from dirtyedit.conf import AUTHORIZED_PATHS, CAN_CREATE_FILES

filepath_form = """
<style>
.dirtymsg {
    line-height:2.3em;
}
</style>
<form class="form-inline pull-left" method="get" action="/admin/dirtyedit/filetoedit/add/" style="margin-right:1em;top:-0.3em">            
    <div class="form-group">
        <div class="input-group">      
              <input class="form-control" id="fpath" name="fpath" placeholder="File path" type="search">
            <span class="input-group-btn">
                <button class="btn btn-primary" type="submit"><i class="fa fa-plus"></i>&nbsp;Add file</button>
            </span>
        </div>
    </div>
</form>
"""

def read_file(request, relative_path):
    # check if the directory is authorized
    if relative_path == '':
        msg = filepath_form+_(u"<div class=\"dirtymsg\">Please provide a file path")
        return ('warn', msg, None)
    if relative_path.endswith('/'):
        msg = filepath_form+_(u"<div class=\"dirtymsg\">Path '<strong>%s</strong>' is invalid: please provide a filename</div>") % (relative_path,)
        return (False, msg, None)
    if relative_path == '/':
        msg = filepath_form+_(u'<div class="dirtymsg">What?</div>')
        return (False, msg, None)
    if not relative_path.startswith('/'):
        msg = filepath_form+_(u'<div class="dirtymsg">Path <strong>\'%s\'</strong> is invalid: please start it with a /</div>') % (relative_path,)
        return (False, msg, None)
    pathlist = relative_path.split('/')[1:]
    #if len(pathlist)==0:
    #    msg = filepath_form+ _(u"<div class=\"dirtymsg\">Path '<strong>%s</strong>' is invalid</div>") % (relative_path,)
    #    return ('warn', msg, None)
    if len(pathlist)>1:
        filename = pathlist[len(pathlist)-1]
    else:
        if '.' not in pathlist[0]:
            msg = filepath_form+_(u"<div class=\"dirtymsg\">Path '<strong>%s</strong>' is invalid: please provide a filename</div>") % (relative_path,)
            return (False, msg, None)
    folderpath = '/'+'/'.join(pathlist[:len(pathlist)-1])
    # check vs authorized paths
    is_authorized = False
    for authorized_path in AUTHORIZED_PATHS:
        #~ check if the path is part of the authorized path
        if folderpath.startswith(authorized_path):
            #print 'OK Authorized : '+authorized_path+ ' == Folderpath '+folderpath
            is_authorized = True
            break
    if is_authorized is False:
        msg = filepath_form+_(u"<div class=\"dirtymsg\">You can not edit files in the directory '<strong>%s</strong>'</div>") % (folderpath,)
        return (False, msg, None)
    filepath=settings.BASE_DIR+relative_path
    # check if file exists
    if not os.path.isfile(filepath):
        # check if filename has an extension
        if not '.' in filename:
            msg = filepath_form+_(u"<div class=\"dirtymsg\">Invalid filename '<strong>%s</strong>': please provide an extention (ex '%s.html')</div>") % (filename,filename)
            return (False, msg, None)
        # msgs
        if CAN_CREATE_FILES is True:
            msg = _(u"<div class=\"dirtymsg\">A new file will be created at '<strong>%s</strong>'</div>") % (relative_path,)
            return ('infos', msg, None)
        else:
            msg = filepath_form+_(u"<div class=\"dirtymsg\">File '<strong>%s</strong>' not found</div>") % (relative_path,)
            return (False, msg, None)
    # read file
    filex = open(filepath, "r")
    filecontent = filex.read()
    msg = _(u"File found: data populated")
    return (True, msg, filecontent)