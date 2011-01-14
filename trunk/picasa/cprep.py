#!/usr/bin/python

import sys
import os

def cprep(src, dest):
	for file in os.listdir(src):
		s="%s/%s" % (src,file)
		d="%s/%s" % (dest,file)
		if os.path.isfile(s):
			fcopy(s,d)
		elif os.path.isdir(s):
			os.mkdir(d)
			cprep(s,d)
			

def fcopy(src, dest):
	fs=open(src,"r")
	fd=open(dest,"w")

	for line in fs:
		fd.write(line)

	fs.close()
	fd.close()



if len(sys.argv) != 3:
	print "erreur syntax : %s repertoireSrc repertoireDest" % (sys.argv[0])
	sys.exit(1)


if not os.path.isdir(sys.argv[2]):
	os.makedirs(sys.argv[2])

src = os.path.abspath(sys.argv[1])
dest = os.path.abspath(sys.argv[2])

cprep(src,dest)



sys.exit(0)
