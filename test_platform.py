# -*- coding: utf-8-*-
import sys
import subprocess

def open_file(filename):
    platform_cmd = {
            'win32': 'start',  # win7 32bit, win7 64bit
            'cygwin': 'start',  # cygwin
            'linux2': 'xdg-open',  # ubuntu 12.04 64bit
            'darwin': 'open',  # Mac
            }
    subprocess.call((platform_cmd.get(sys.platform, 'xdg-open'), filename))


if __name__ == '__main__':
    filename = u'hello.pdf'
    print sys.platform
    open_file(filename)
