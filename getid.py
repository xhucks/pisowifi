# uncompyle6 version 3.5.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.5 (default, Aug  7 2019, 00:51:29) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-39)]
# Embedded file name: ./getid.py
# Compiled at: 2019-05-23 06:34:10
import uuid, hashlib, sys, subprocess, enc
myhash = enc.getserial()
print myhash
