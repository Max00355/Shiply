import os
from .coffer.utils import getRootDir, text, getFlag, ccopy, templateUtils, isRoot, content, getArg
import sys
import re
import string
import imp
import urllib.request as urllib
import platform
import six

def createDir(path):
    six.print_((text.createDir))
    if not os.path.exists(path):
        os.mkdir(path)
        return True
    return False

def copyBaseFiles(path):
    six.print_((text.copyingFiles))
    # Supports 64 bit and 32 bit, no arm yet (though should be an easy fix)
    if platform.architecture()[0] == "64bit":
        arch = "amd64"
    else:
        arch = "i386"
    
    version = getFlag.getFlag("-v")
    architecture = getFlag.getFlag("-a")
    repo = getFlag.getFlag("-r") 
    if version not in content.versions:
        version = "xenial"
    if architecture and architecture in content.architectures:
        arch = content.architectures.get(architecture)
    six.print_((text.usingVersion.format(version)))
    debCmd = "bash " + getRootDir.getCofferDir() + "debootstrap/debootstrap --arch=" + arch + " {} {}"
    if repo:
        debCmd += " " + repo
    os.system(debCmd.format(version, path))
    getSourceList(path, version)

def getSourceList(path, version):
    version = version.lower()
    if not os.path.exists(path + "/etc/apt/"):
        sys.exit(text.failedToCreate)
    
    if version in content.sources:
        with open(path + "/etc/apt/sources.list", 'w') as f:
            f.write(content.sources[version])

def executeTemplate(template):
    templateName = template.split("/")[-1]
    templateName = templateName.split(".")[0]
    imp.load_source(templateName, template) # This could break, but I'd rather allow it to break than do a try, except
    six.print_((text.templateSuccess))

def create():
    root = getRootDir.getEnvsDir()
    template = getFlag.getFlag("-t")
    name = getArg.getArg(0)
    if not name:
        sys.exit(text.createHelper)
    if not isRoot.isRoot():
        sys.exit(text.notRoot)
    path = root + name
    if not createDir(path):
        sys.exit(text.envAlreadyExists)
    copyBaseFiles(path)
    if template:
        executeTemplate(template)
    six.print_((text.envCreated))

