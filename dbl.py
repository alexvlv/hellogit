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

