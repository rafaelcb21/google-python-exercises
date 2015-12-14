#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Problem description:
# https://developers.google.com/edu/python/exercises/copy-special


import sys
import os
import shutil
import subprocess

#Copy Special exercise

def copiar(diretorio, *args):
    if not os.path.exists(diretorio):
        os.mkdir(diretorio)

    for nvl1 in args:
        for file in nvl1:
            shutil.copy(file, diretorio)
            print('copy: %s TO %s'%(file, diretorio))

def zippar(diretorio, *args):
    cmd = ["C:/Program Files/Zip/zip.exe", "-j"] + diretorio + args[0]
    subprocess.call(cmd)

def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

        flag = True
        for file in args:
            if not os.path.exists(file):
                print('error: %s not found' %file )
                flag = False
        if flag:
            copiar(todir, args)

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

        flag = True
        for file in args:
            if not os.path.exists(file):
                print('error: %s not found' %file)
                flag = False
        if flag:
            zippar([tozip], args)

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

if __name__ == "__main__":
    main()
