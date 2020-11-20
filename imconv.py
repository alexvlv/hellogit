#!/usr/bin/python3
# -------------------------------------------------------------------------------
# Name:        imconv
# Purpose:
#
# Author:      Admin
#
# Created:     18.11.2018
# Copyright:   (c) Admin 2018
# Licence:     <your licence>
# -------------------------------------------------------------------------------

import argparse
import sys
import os
import time
import glob

from PIL import Image

########################################################################
class ImageConverter:
    """Resize and convert images in directory"""
    dirname = None
    fileNames = None
    outsize = 1600, 1200
    vertsize = outsize[1], outsize[0]
    outdir = 'out'
    foutdir = None

    # ----------------------------------------------------------------------
    def process(self, dirname):
        assert isinstance(dirname, str)
        self.dirname = dirname
        mask = dirname + os.sep + '*.jpg'
        fnames = glob.glob(mask)
        nimgs = len(fnames)
        print("Found {:d} images in [{:s}]".format(nimgs,dirname))
        if nimgs == 0:
            return 0
        self.foutdir = os.path.abspath(dirname + os.sep + self.outdir)
        if not os.path.exists(self.foutdir):
            os.makedirs(self.foutdir)
        for fname in fnames:
            self.convert(fname)
        thumb = self.foutdir + os.sep + 'Thumbs.db'
        if os.path.isfile(thumb):
            os.remove(thumb)
        if not os.listdir(self.foutdir):
            os.rmdir(self.foutdir)

    # ----------------------------------------------------------------------
    def convert(self, fname):
        outname = self.foutdir + os.sep + os.path.basename(fname)
        if os.path.exists(outname):
            print("[{:s}]... SKIP".format(fname, ))
            return
        print("[{:s}]... ".format(fname,), end='')
        im = Image.open(fname)
        width, height = im.size
        newsize = self.outsize if width > height else self.vertsize
        if newsize[0]>=width or newsize[1]>=height:
            print("  {:d}x{:d} SKIP".format(width,height))
            return
        imn = im.resize(newsize,Image.BICUBIC)
        if width < height:
            imr = imn.rotate(90,expand=True)
            imn = imr
        imn.save(outname, quality=60, optimize=True)
        print('OK')



# -------------------------------------------------------------------------------
def main():

    parser = argparse.ArgumentParser(description='Main base viewer')
    parser.add_argument('-d', '--dir', help='Working directory', default=os.getcwd())

    args = parser.parse_args()

    imgs = ImageConverter()
    #imgs.process(os.getcwd())
    imgs.process(args.dir)

# -------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
# -------------------------------------------------------------------------------
