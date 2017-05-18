from .coffer.utils import isRoot, text, getRootDir, getArg
from .coffer import remove
import os
import sys

def renameDir(path, name):
    os.rename(path, name)

def rename():
    if not isRoot.isRoot():
        sys.exit(text.notRoot)
    root = getRootDir.getEnvsDir()
    
    name = getArg.getArg(0)
    newName = getArg.getArg(1)

    if not name or not newName:
        sys.exit(text.renameHelper)

    if not os.path.exists(root + name):
        sys.exit(text.envDoesntExist)

    if os.path.exists(root + newName):
        sys.exit(text.nameAlreadyExists)
    remove.unmountAll(root + name)
    renameDir(root + name, root + newName)
    sys.exit(text.renameSuccessful)
