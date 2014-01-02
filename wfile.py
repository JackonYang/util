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


def ipath(src_path, file_hdlr, file_ext='.py', ignore=None):
    # not exists
    if not os.path.exists(src_path):
        return 0

    src_path = os.path.abspath(src_path)
    # file
    if os.path.isfile(src_path):
        return file_hdlr(src_path)

    file_count = 0
    for path_name in os.listdir(src_path):
        if ignore and _is_ignore(path_name, ignore):
            continue
        abs_path = os.path.join(src_path, path_name)
        if os.path.isdir(abs_path):
            file_count += ipath(abs_path, file_hdlr, file_ext, ignore)
        elif abs_path.endswith(file_ext):
            file_count += int(file_hdlr(abs_path))
    return file_count

def _is_ignore(path, ptn, seq=','):
    if isinstance(ptn, basestring):
        ptn = ptn.strip('%s ' % seq)
        if seq in ptn:
            ptn = [iptn.strip() for iptn in ptn.split(seq)]
        else:
            ptn = [ptn]
    for iptn in ptn:
        if fnmatch.fnmatch(path, iptn):
            return True
    return False

    ptns = ptn.strip(', ').split(',')
    pass

if __name__ == '__main__':
    filename = u'hello.pdf'
    print md5_for_file(filename)
    # open_file(filename)
    def demo_file(fname):
        print 'hello %s' % fname
        return True
    print ipath('..', demo_file, ignore='.git, .ropeproject')
