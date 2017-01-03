#!/usr/bin/env python

import os
import glob
import patoolib

def extractFiles(indir=os.getcwd(), out=os.getcwd() + '/extracted'):
    os.chdir(indir)
    archives=glob.glob("*.gz")
    if not os.path.exists(out):
        os.makedirs(out)
    files=os.listdir(out)
    for archive in archives:
        print archive, files
        if archive[:-3] not in files:
            patoolib.extract_archive(archive, outdir=out)

extractFiles()
