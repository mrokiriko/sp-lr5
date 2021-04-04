#! /usr/bin/env python
# -*- coding: utf-8 -*-
# чтобы не ругался на русские комментарии

import sys
import hashlib

BUF_SIZE = 65536 # подсчет данных по 64 килобаййта

sha1 = hashlib.sha1()

if (len(sys.argv) < 2):
	raise Exception('no file provided, use cli argument')
	exit()

filename = sys.argv[1]

with open(filename, 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        sha1.update(data)

print(sha1.hexdigest())