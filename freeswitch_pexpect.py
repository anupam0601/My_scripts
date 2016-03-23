#!/usr/bin/env python
import pexpect
import pxssh
import sys
import time

PASS = "C!0ver"

child = pexpect.spawn("ssh wcs@192.168.2.22")
i=child.expect(['yes/no','[Pp]assword:',pexpect.EOF,pexpect.TIMEOUT])

if i==0:
    child.sendline('yes')
    child.expect_exact('Password:')
    child.sendline(PASS)
    child.expect_exact('$')
    print child.before


if i==1:
    child.sendline(PASS)
    child.expect_exact('$')
    print child.before

## Command to login to freeswitch
    child.sendline("fscli")
    child.expect_exact('>')
    print child.before

## Command to show channels in freeswitch
    child.sendline("show channels")
    child.expect_exact('total.')
    print child.before

## Command to make a call
    child.sendline("originate user/1052 inline")
    time.sleep(4)
    child.expect('72')
    print child.before


## Status of a call







