# -*- coding: utf-8-*-
"""wise file

"""
import time
import hashlib
import subprocess
import os
import sys
import fnmatch

def md5_for_file(filename, block_size=256*128, hr=True):
    """calculate md5 of a file

    Block size directly depends on the block size of your filesystem
    to avoid performances issues
    Here I have blocks of 4096 octets (Default NTFS)

    """
    md5 = hashlib.md5()
    with open(filename,'rb') as f: 
        for chunk in iter(lambda: f.read(block_size), b''): 
            md5.update(chunk)
    if hr:
        return md5.hexdigest()
    return md5.digest()


def open_file(filename):
    platform_cmd = {
            'win32': 'start',  # win7 32bit, win7 64bit
            'cygwin': 'start',  # cygwin
            'linux2': 'xdg-open',  # ubuntu 12.04 64bit
            'darwin': 'open',  # Mac
            }
    if sys.platform.startswith('win'):  # windows
        os.startfile(filename)
    else:
        subprocess.call((platform_cmd.get(sys.platform, 'xdg-open'), filename))


def is_hiden(filename):
    return filename.startswith('.')  # linux


if __name__ == '__main__':
    filename = u'hello.pdf'
    print md5_for_file(filename)
    # open_file(filename)
