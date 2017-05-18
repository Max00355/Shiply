import os
from .coffer.utils import getRootDir, text
import six

def ls():
    six.print_((text.availableEnvironments))
    check = os.listdir(getRootDir.getEnvsDir())
    if len(check) == 0:
        six.print_((text.noEnvs))
    else:
        six.print_(('\n'.join(check) + "\n"))
