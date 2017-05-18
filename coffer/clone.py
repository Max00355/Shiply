from .coffer.utils import getRootDir, text, ccopy, isRoot, getArg
from .coffer import remove
import shutil
import sys
import os
import six

def copyEnv(path, to):
    six.print_((text.cloning))
    ccopy.copy(path, to)
    
def envExists(path):
    return os.path.exists(path)

def clone():
    if len(sys.argv) < 4:
        sys.exit(text.cloneHelper)
    if not isRoot.isRoot():
        sys.exit(text.notRoot)

    name = getArg.getArg(0)
    clone = getArg.getArg(1)

    path = getRootDir.getEnvsDir() + name
    clonePath = getRootDir.getEnvsDir() + clone

    if not envExists(path):
        sys.exit(text.envDoesntExistVar.format(name))
    if envExists(clonePath):
        sys.exit(text.envAlreadyExistsVar.format(clone))
    remove.unmountAll(path)
    copyEnv(path, clonePath)
    six.print_((text.cloned))
