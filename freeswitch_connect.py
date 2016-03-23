#!/usr/bin/env python

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect('192.168.2.22', username='wcs', password='C!0ver')
except paramiko.SSHException:
    print "Connection Failed"
    quit()
stdin, stdout, stderr = ssh.exec_command('fscli;show')




for lines in stdout:
	print lines



#for line in stdout:
	#print line

'''
ssh.exec_command("fscli")

print "logged in to freeswitch"

stdin, stdout, stderr = ssh.exec_command("show channels")

for lines in stdout:
    print lines'''


ssh.close()
