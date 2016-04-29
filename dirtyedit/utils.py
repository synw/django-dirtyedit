# -*- coding: utf-8 -*-

import os
from django.conf import settings
from django.utils.translation import ugettext as _
from dirtyedit.conf import AUTHORIZED_PATHS, EXCLUDED_PATHS, CAN_CREATE_FILES

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

def check_file(relative_path, edit_mode=False):
    # check if the directory is authorized
    if relative_path == '':
        msg = filepath_form+_(u"<div class=\"dirtymsg\">Please provide a file path</div>")
        return ('warn', msg)
    if relative_path == '/':
        msg = filepath_form+_(u'<div class="dirtymsg">What?</div>')
        return (False, msg)
    if relative_path.endswith('/'):
        msg = filepath_form+_(u"<div class=\"dirtymsg\">Path '<strong>%s</strong>' is invalid: please provide a filename</div>") % (relative_path,)
        return (False, msg)
    if not relative_path.startswith('/'):
        msg = filepath_form+_(u'<div class="dirtymsg">Path <strong>\'%s\'</strong> is invalid: please start it with a /</div>') % (relative_path,)
        return (False, msg)
    pathlist = relative_path.split('/')[1:]
    folderpath = '/'+'/'.join(pathlist[:len(pathlist)-1])
    absolute_folderpath  = settings.BASE_DIR+folderpath
    if len(pathlist)>1:
        filename = pathlist[len(pathlist)-1]
    else:
        if '.' not in pathlist[0]:
            msg = filepath_form+_(u"<div class=\"dirtymsg\">Path '<strong>%s</strong>' is invalid: please provide a filename</div>") % (relative_path,)
            return (False, msg)
    for fpath in EXCLUDED_PATHS:
        if relative_path.startswith(fpath):
            msg = filepath_form+_(u"<div class=\"dirtymsg\">You can not edit files in the directory '<strong>%s</strong>'</div>") % (folderpath,)
            return (False, msg)
    if not os.path.isdir(absolute_folderpath):
        msg = filepath_form+_(u"<div class=\"dirtymsg\">The directory <strong>%s</strong>' does not exist</div>") % (folderpath,)
        return (False, msg)
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
        return (False, msg)
    filepath=settings.BASE_DIR+relative_path
    # check if file exists
    if not os.path.isfile(filepath):
        # check if filename has an extension
        if not '.' in filename:
            msg = filepath_form+_(u"<div class=\"dirtymsg\">Invalid filename '<strong>%s</strong>': please provide an extention (ex '%s.html')</div>") % (filename,filename)
            return (False, msg)
        # msgs
        if CAN_CREATE_FILES is True:
            if not edit_mode is True:
                msg = _(u"<div class=\"dirtymsg\">A new file will be created at '<strong>%s</strong>'</div>") % (relative_path,)
                return ('infos', msg)
        else:
            if not edit_mode is True:
                msg = filepath_form+_(u"<div class=\"dirtymsg\">File '<strong>%s</strong>' not found</div>") % (relative_path,)
            else:
                msg = filepath_form+_(u"<div class=\"dirtymsg\">You can not create files</div>")
            return (False, msg)
    return (True, '')

def read_file(relative_path):
    status, msg = check_file(relative_path)
    if status in [False, 'warn', 'infos']:
        return (status, msg, None)
    # read file
    filepath=settings.BASE_DIR+relative_path
    filex = open(filepath, "r")
    filecontent = filex.read()
    msg = _(u"File found: data populated")
    return (True, msg, filecontent)

def write_file(relative_path, content):
    status, msg = check_file(relative_path, edit_mode=True)
    if status in [False, 'warn', 'infos']:
        return (status, msg)
    else:
        filepath=settings.BASE_DIR+relative_path
        #~ write the file
        filex = open(filepath, "w")
        filex.write(content)
        filex.close()
    return (True, msg)

