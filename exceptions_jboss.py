###########################
# Author - Anupam Debnath #
###########################

#!/usr/bin/env python
 
import pexpect
import pxssh
import sys
import re
import os
import getopt
from datetime import datetime

 
USER="wcs"
PASS="C!0ver"
COMMAND="ssh -t %s@%s"
COMMAND1='echo "********* ";hostname;echo "*********";cd /var/log/jboss/;/bin/bash -c "grep -i Exception -B 3 -A 3 server.log"'


jbossException = ''
jbossException2 = ''
 
def dohost(host):
  command = COMMAND % (USER, host)
  child = pexpect.spawn(command)
  i=child.expect(['yes/no','[Pp]assword:',pexpect.EOF,pexpect.TIMEOUT])
  if i==0:
    child.sendline('yes')
    child.expect_exact('password:')
    child.sendline(PASS)
    child.expect("$")
    print child.before

# COMMAND1: To check for Null pointer exceptions:
    global jbossException
    child.sendline(COMMAND1)
    child.expect_exact('$')
    timeStamp = str(datetime.now())[:-7]
    runTime = "Run Time"
    jbossException = jbossException+'\n'+'****** '+runTime+' '+':'+timeStamp+' ******'+'\n'+'\n'+child.before + '\n' + '\n'
    print jbossException

    
  if i==1:
    child.sendline(PASS)
    child.expect_exact('$')
    print child.before
    
# COMMAND1: To check for Null pointer exceptions:
    global jbossException2
    child.sendline(COMMAND1)
    child.expect_exact('$')
    timeStamp_2 = str(datetime.now())[:-7]
    runTime_2 = "Run Time"
    jbossException2 = jbossException2+'\n'+'***** '+runTime_2+' '+':'+timeStamp_2+' *****'+'\n'+'\n'+child.before + '\n' + '\n'
    print jbossException2
    
   
  elif i==2:
    print "Script has read till end of file, It will move forward with next loop"

  elif i == 3:
    print "Timeout has reached, script is moving forward with next loop"

# Put your hosts in hostfilename one host per line:
 
for host in open('/home/administrator/test_scripts_auto/hostfile.txt'):
  dohost(host)


# Below code lines are to write to a text file from there to a css:
save_path = '/opt/lampp/htdocs/anupam/Automation_Results/'

completePath = os.path.join(save_path,'jboss_exceptions.txt')
completePath2 = os.path.join(save_path,'jboss.css')


# writing it to a text file
with open(completePath,"w") as f1:
  f1.write('############# EXCEPTIONS IN JBOSS ############'+'\n'+ jbossException + '\n')
  f1.write(jbossException2)


# Using with open so that it can handle file related exceptions and writing it to a css file
with open(completePath) as old, open(completePath2,"wb") as new:
  for line in old:
    if "/var" not in line:
      new.write(line)