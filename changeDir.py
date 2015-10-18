## Code to check creation of file in a location and sending the snapshot of the Directory through email:


#!/usr/bin/python

import os, time
import smtplib
import getpass
import subprocess


## In the below function i am comparing two dictionaries as path that i am watching for
def run():
    path_to_watch = "/home/anupam/python_scripts"
    print "watching: " + path_to_watch
    before = dict ([(f, None) for f in os.listdir (path_to_watch)])

    ## The below while loop will be on the loop an dkeep on comparing before and after dicts
    ## If any file is removed it will compare remove with after and before dicts
    while 1:
        after = dict ([(f, None) for f in os.listdir (path_to_watch)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        global a

        if added: 
        	print "Added: ", ", ".join (added)

        	time.sleep(1)

        	## If anything is added a shell command "ls -l" would be executed to check the directory and would be stored in variable DirOverview      	

        	DirLook = subprocess.Popen("cd /home/anupam/python_scripts | ls -l", shell = True, stdout = subprocess.PIPE)

        	global DirOverview

        	DirOverview = ""

        	## Concatenating each line to DirOverview

        	for line in DirLook.stdout:
        		DirOverview = DirOverview + str(line) + "\n"

			print DirOverview

        	
        	## We would be sending an email notification to the user with the Directory snapshot
    		sender = 'ironhide.debnath@gmail.com'
    		reciever = ['ironhide.debnath@gmail.com']
    		username = 'ironhide.debnath@gmail.com'
    		password = getpass.getpass("%s's password: " % username)
    		marker = "AUNIQUEMARKER"

    		body ="""
    		A core file has been generated
    		"""
    		part1 = """From: From Person <ironhide.debnath@gmail.com>
    		To: To Person <ironhide.debnath@gmail.com>
    		Subject: Core files generated
    		MIME-Version: 1.0
    		Content-Type: text/html
    		%s
    		%s
    		""" % (body,DirOverview)
    		
    		# Define the attachment section
    		message = part1
    		mail= smtplib.SMTP('smtp.gmail.com:587')
    		mail.ehlo()
    		mail.starttls()
    		mail.ehlo()
    		mail.login('ironhide.debnath@gmail.com', password)
    		mail.sendmail(sender,reciever, message)
    		mail.close()

        	
        if removed: 
        	b = "Removed: ", ", ".join (removed)
        	print b
        before = after
        #time.sleep (10)
run()