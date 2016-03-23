#!/usr/bin/env python
import subprocess
from itertools import chain


command = "tshark -r rtp_example.raw.gz -o rtp.heuristic_rtp:TRUE -qz rtp,streams"

turret = subprocess.Popen(command , shell=True, stdout=subprocess.PIPE)

readOut = turret.stdout

#readFile = [line.split(',') for line in (readOut.readlines()[2:])]

global listRtp

listRtp = []
for line in readOut:
	f = (line.split())
	listRtp.append(f)
	#print f

print listRtp

## Used chain() function to take list of lists as arguments and to iterate over them:
if '192.168.3.216' in chain(*listRtp):
	print "found"