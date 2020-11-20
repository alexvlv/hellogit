#!/usr/bin/env python3
#---------------------------------------------------------------------
# 10:05 14.01.2017
#---------------------------------------------------------------------
import os
import glob
import codecs
import re
import string


#---------------------------------------------------------------------
def processFname(imgName):
    match = re.search(r'(?:img_|\.)(\d+)(\S*)\.jpg',imgName,re.IGNORECASE) 
    if match:
        key = match.group(1)
        isRepeat = ( len(match.group(2)) > 0 )
        if isRepeat:
            key = key + '_'
        #print (key + ' [' + match.group(2) + '] =' + repr(isRepeat) )
        fileName = 'img_' + key + '.jpg'
        print (fileName)
        os.rename(imgName, fileName)
    else:
        print ('Key not found for [' + img + ']')
#--------------------------------------------------------------------- 
#---------------------------------------------------------------------
imgFilesNames = glob.glob('*.jpg')
nImages = len(imgFilesNames)
print("Found {:d} images in {:s}".format(nImages,os.getcwd()))
imgsDict = dict()
for s in imgFilesNames:
    processFname(s)  
#print( sorted(imgsDict.keys()))
#---------------------------------------------------------------------








        



