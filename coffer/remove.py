from .coffer.utils import getRootDir, text, isRoot, getArg
import os
import shutil
import sys
import re
import six

def removeDir(path):
    six.print_((text.removingEnv))
    shutil.rmtree(path)

def checkIfExists(path):
    return os.path.exists(path)

def getMounted(path):
    mounted = os.popen("mount | grep 'coffer'").read()
    mounted = re.findall("on (.*) type", mounted)
    for m in mounted:
        if path in m:
            yield m

def unmountAll(path):
    for m in getMounted(path):
        six.print_((text.unmounted.format(m)))
        os.system("umount {}".format(m))

def remove():
    rootDir = getRootDir.getEnvsDir()

    name = getArg.getArg(0)

    if not name:
        sys.exit(text.removeHelper)
    if not isRoot.isRoot():
        sys.exit(text.notRoot)
    if not checkIfExists(rootDir + name):
        sys.exit(text.envDoesntExist)
    unmountAll(rootDir + name)
    removeDir(rootDir + name)
    six.print_((text.removed))
