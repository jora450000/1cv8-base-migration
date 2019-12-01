#!/usr/bin/python
# -*- coding: utf-8 -*-

import fileinput
from pathlib2 import Path

import _locale, os, sys
_locale._getdefaultlocale = (lambda *args: ['ru_RU', 'utf8'])

StrOld = 'Connect=File="\\\\zeon\\Base\\Зарплата\";'
StrNew = 'Connect=Srvr=\"192.168.1.10\";Ref=\"zarplata\";'
path = '\\\\192.168.1.2\\c$\\Users'

print (f"find:    {StrOld}\nreplace: {StrNew}\npath:    {path}\n")


for entry in os.scandir(path):
        try:
            is_dir = entry.is_dir(follow_symlinks=False)
        except OSError as error:
            print('Error calling is_dir():', error, file=sys.stderr)
            continue
        if is_dir:
            print (entry.path)
            try:
                for filename in Path(entry.path).rglob('*.v8i'):
                    print(filename)
                    text = filename.read_text( )
                    filename.write_text(text.replace(StrOld,StrNew))
            except OSError as error:
       		    print('Error calling glob():', error, file=sys.stderr)
                    
        else:
            try:
                entry.stat(follow_symlinks=False)
            except OSError as error:
                print('Error calling stat():', error, file=sys.stderr)
