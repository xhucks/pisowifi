# uncompyle6 version 3.5.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.5 (default, Aug  7 2019, 00:51:29) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-39)]
# Embedded file name: ./getcdkey.py
# Compiled at: 2019-03-06 13:17:55
import uuid, hashlib, sys

def getcdkey():
    cdkey = ''
    try:
        f = open('/etc/cdkey', 'r')
        for line in f:
            cdkey = line

        f.close()
    except:
        cdkey = 'ERROR'
        sys.exit()

    return str.strip(cdkey)


cdk = getcdkey()
print cdk
