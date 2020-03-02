# uncompyle6 version 3.5.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.5 (default, Aug  7 2019, 00:51:29) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-39)]
# Embedded file name: ./testcdkey.py
# Compiled at: 2019-05-23 06:28:09
from time import sleep
import time, sys, hashlib, uuid, subprocess, enc
s = enc.getserial()
c = enc.getcdkey()
e = enc.encode(s)
if e != c:
    print 'E3'
    sys.exit()
print 'success'
