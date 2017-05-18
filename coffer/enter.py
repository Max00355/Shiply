import os
import string
from .coffer.utils import text, getRootDir, isRoot, getFlag, getArg
from .coffer import create
from .coffer import remove
import sys
import re
import six

def enterChroot(path):
    os.chdir(path)
    os.chroot(path)

def executeCommand(command="/bin/bash"):
    os.system(command)

def mount(directory, path):
    mounts = list(remove.getMounted(path))
    mounted = (path + "/" + directory).replace("//", "/") in mounts
    if not mounted:
        os.system("mount --bind {} {}/{}".format(directory, path, directory))
        six.print_((text.mounted.format(directory)))
    else:
        six.print_((text.alreadyMounted.format(directory)))

def checkMount(path):
    toMount = getFlag.getFlags("-m")
    if toMount:
        for directory in toMount:
            mount(directory, path)

def enter():
    if not isRoot.isRoot():
        sys.exit(text.notRoot)
    rootDir = getRootDir.getEnvsDir()
    name = getArg.getArg(0)
    if not name:
        sys.exit(text.enterHelper)
    template = getFlag.getFlag("-t")
    if template:
        create.executeTemplate(template)
    path = rootDir + name
    if not os.path.exists(path):
        sys.exit(text.envDoesntExist)
    checkMount(path) 
    enterChroot(path)
    command = getFlag.getFlag("-c")
    if command:
        executeCommand(command=command)
    else:
        executeCommand()
