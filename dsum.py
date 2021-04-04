#! /usr/bin/env python
# -*- coding: utf-8 -*-
# чтобы не ругался на русские комментарии

import subprocess
import sys
from os import walk
import sys
import hashlib
import threading

hashes = []

# функция для вызова потоком
def get_fsum(filepath):
	# вызов процесса для подсчета хэша одного файла
	result = subprocess.run(
		[sys.executable, "fsum.py", filepath], capture_output=True, text=True
	)
	if (result.stderr):
		print("Error occured: " + result.stderr)
		exit()

	filehash = result.stdout.strip()

	print(" - hashsum for file " + filename + " is " + filehash)

	hashes.append(filehash) # помещает хэш в глобальную переменную

if (len(sys.argv) < 2):
	raise Exception('no directory provided, use cli argument')
	exit()

mypath = sys.argv[1]

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break

list_threads = []

for filename in filenames:

	filepath = dirpath + '/' + filename # составим относительный путь до файла

	t = threading.Thread(target=get_fsum, args=(filepath,)) # запуск потока
	list_threads.append(t)
	t.start()

for t in list_threads:
  t.join() # ждем завершения потоков

print("все потоки были завершены")

sha1 = hashlib.sha1() # для подсчета хэша самой директори
for filehash in hashes:
	sha1.update(filehash.encode())
print("hash for directory " + mypath + " is " + sha1.hexdigest())
