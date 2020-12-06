#!/usr/bin/env python3
# $Id$

import re


patternDelim = re.compile(r'^(-+)|(#+)',re.IGNORECASE)
patternSkip = re.compile(r'(\s+\*\s*$)|(\bДБЛ\b[^*]*\*?\s*$)')


strings = [
    '88-055 Конвертик =3шт * ',
    '------ ',
    '0999 1983 Проверка ДБЛ '
    ]

for line in strings:
    line = line.strip()
    if len(line) == 0 :
        continue
    resRegDelim = patternDelim.match(line)
    if resRegDelim is not None:
        continue
    resRegSkip = patternSkip.search(line)
    if resRegSkip is not None:
        print( "[{}] skipped".format(line[0:40]))
        continue
    print( "[{}] len:{}".format(line,len(line)))
	
# for next commit after 
# Author:			Alex <alexey.v.v@mail.ru>
#  Date:			1 minute ago (06.12.2020 21:39:21)
#Commit hash:	e6898aac726c67d6fd467afb5b8ee4e026201cfc
#Child:			Commit index
#Parent:			2a355055
# after Id d718b29c7911d9b38bb22fe1a0091f51b829b658	
	

