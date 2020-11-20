#!/usr/bin/env python3
#---------------------------------------------------------------------
# 14:37 06.01.2017
#---------------------------------------------------------------------
import os
import glob
import codecs 
import re
import string
#---------------------------------------------------------------------
numeral_map = tuple(zip(
    (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
))

def int_to_roman(i):
    result = []
    for integer, numeral in numeral_map:
        count = i // integer
        result.append(numeral * count)
        i -= integer * count
    return ''.join(result)

def roman_to_int(n):
    i = result = 0
    for integer, numeral in numeral_map:
        while n[i:i + len(numeral)] == numeral:
            result += integer
            i += len(numeral)
    return result
#---------------------------------------------------------------------
def roman_numerals(line):
	#match=re.search(r'\b(?=[MDCLXVI])(M{0,3})(C[DM]|D?C{0,3})(X[LC]|L?X{0,3})(I[VX]|V?I{0,3})\b',line) 
	#if match:
	#	print('['+match.group(0)+']')
	line = re.sub(r'\s+\b(?=[MDCLXVI])(M{0,3})(C[DM]|D?C{0,3})(X[LC]|L?X{0,3})(I[VX]|V?I{0,3})\b','',line) 
	return line
#---------------------------------------------------------------------
def shortLine(line):
    parts = re.split(r'[=\*]+|ДБЛ', line)
    line = parts[0].strip()
    if len(line) > 60:
        line = line[:65].strip()
        match=re.search('\s\w+$',line)
        if match and match.start(0) > 0: 
            line = line[:match.start(0)].strip()
    return line
#info = (data[:75] + '..') if len(data) > 75 else data
#---------------------------------------------------------------------
def removeExtras(line):
	#http://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python
	#filter(lambda ch: ch not in " ?.!/;:", line)
	#line = ''.join(c for c in line if not c in r'.!/;:@#$"`')
	line = line.translate({ord(c): None for c in r'.!/;:@#$"`'})
	
	#line = re.sub('(?<=\s)\w(?=\s+)', '', line) #look behind and look ahead
	line = re.sub('\s+[a-zA-Zа-яА-Я]{1,2}(?=\s+)', '', line)
	line = re.sub('\s+\d{1,2}(л|м)(?=\s*)', '', line)
	return line
#---------------------------------------------------------------------
patternDelim = re.compile('^(~+)|(-+)|(#+)',re.IGNORECASE)
patternSkip = re.compile(r'(\s+\*\s*$)|(\bДБЛ\b[^*]*\*?\s*$)')
def processLine(line):
    line = line.strip()
    if len(line) == 0 :
        return
    resRegExp = patternDelim.match(line)
    if resRegExp is not None:
        return
    resRegExp = patternSkip.search(line)
    if resRegExp is not None:
        print( "[{}] skipped".format(line[0:30]))
        return
    line = roman_numerals(line)
    line = removeExtras(line)
    line = shortLine(line)
    listUnits.append(line)
    #print( "[{}] len:{}".format(line,len(line)))
#---------------------------------------------------------------------
def readDescFile(fname):
    with codecs.open(fname, 'r', encoding='utf-8') as f:
        for line in f:
            processLine(line)
    f.close()     
#---------------------------------------------------------------------        
def findDescFile():
        print("Working dir: ["+os.getcwd()+"]")
        txts = sorted(glob.glob('*.txt'))
        print("Found {:d} txt file(s)".format(len(txts)))
        if len(txts) == 0:
            print("No description found!")
            quit()
        return txts[0]
#---------------------------------------------------------------------  
#--------------------------------------------------------------------- 
#--------------------------------------------------------------------- 
def getKey(key):
    appendSym = iter(list(string.ascii_lowercase))
    while key in imgsDict:
        #print ('Already exists [' + key + ']')
        key = key + next (appendSym)
    return key;
#---------------------------------------------------------------------
def processFname(imgName):
    match = re.search(r'(?:img_|\.)(\d+)(\S*)\.jpg',imgName,re.IGNORECASE) 
    if match:
        key = getKey(match.group(1))
        isRepeat = ( len(match.group(2)) > 0 )
        if isRepeat:
            key = key + '_'
        #print (key + ' [' + match.group(2) + '] =' + repr(isRepeat) )
        imgItem = (imgName,isRepeat)
        imgsDict[key] = imgItem
    else:
        print ('Key not found for [' + img + ']')
#--------------------------------------------------------------------- 
#--------------------------------------------------------------------- 
#--------------------------------------------------------------------- 
def processKey(key):
	fdat = imgsDict[key] 
	if not fdat[1] or 'description' not in processKey.__dict__:
		processKey.description = next(iterUnits)
	#print(processKey.description[:20] + ' ' + fdat[0] + ' ' +  repr(fdat[1]))
	fileName = processKey.description + '.' + key + '.jpg'
	print (fileName)
	os.rename(fdat[0], fileName)
#processKey.description = None
#--------------------------------------------------------------------- 
#--------------------------------------------------------------------- 
#--------------------------------------------------------------------- 
fDescName = findDescFile()
print("Description file used: [{0}]".format(fDescName))
listUnits = list()
readDescFile(fDescName)
print ("Read {:d} descriptions".format(len(listUnits)))
if len(listUnits) == 0:
	print("No descriptions read!")
	quit()
#---------------------------------------------------------------------
imgFilesNames = glob.glob('*.jpg')
nImages = len(imgFilesNames)
print("Found {:d} images in {:s}".format(nImages,os.getcwd()))
imgsDict = dict()
for s in imgFilesNames:
    processFname(s)  
#print( sorted(imgsDict.keys()))
#---------------------------------------------------------------------
keys = sorted(imgsDict.keys())
iterUnits = iter(listUnits)
try:
	for key in keys:
		processKey(key)  
except StopIteration:
	print('No more descriptions!')

if os.path.isfile("Thumbs.db"):
    os.remove("Thumbs.db")





        



