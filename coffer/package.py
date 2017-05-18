from .coffer.utils import getRootDir, text, isRoot, getArg
from .coffer import remove
import shutil
import sys
import os
import six

def createArchive(path, name):
    six.print_((text.creatingPackage))
    shutil.make_archive(name, "tar", path)

def compress(path, name):
    createArchive(path, name)
    os.rename(name + ".tar", name + ".coffer")

def package():
    rootDir = getRootDir.getEnvsDir()
    env = getArg.getArg(0)

    if not env:
        sys.exit(text.packageHelper)
    if not isRoot.isRoot():
        sys.exit(text.notRoot)
    if not remove.checkIfExists(rootDir + env):
        sys.exit(text.envDoesntExist)
    
    remove.unmountAll(rootDir + env)
    compress(rootDir + env, env)
    six.print_((text.packaged))
