import os
import urllib.request as urllib
from coffer.utils import getRootDir
import tarfile
from coffer.utils import text
import six
from six.moves.urllib.request import urlopen

def setup():
    root = getRootDir.getCofferDir()
    envs = getRootDir.getEnvsDir()
    os.mkdir(root)
    os.mkdir(envs)
    six.print_((text.downloadingFiles))
    deboot = urlopen("http://ftp.debian.org/debian/pool/main/d/debootstrap/debootstrap_1.0.81~bpo8+1.tar.gz")
    path = root + "deboot.tar"
    with open(path, 'wb') as tarf:
        tarf.write(deboot)
    tarfile.open(path).extractall(path=root)
    os.remove(path)
    edit = open(root + "debootstrap/debootstrap").readlines()
    edit[487] = "#" + edit[487]
    edit[488] = "#" + edit[488]
    edit[489] = "#" + edit[489]
    edit = "".join(edit)
    edit = "DEBOOTSTRAP_DIR={}\n".format(root + "debootstrap") + edit
    with open(root + "debootstrap/debootstrap", 'w') as w:
        w.write(edit) 
