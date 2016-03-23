#!/usr/bin/env python

import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.2.22', 13750)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

# Waiting for password prompt
data = sock.recv(40000)

# Send password
message = 'auth wcs_dev_08\n\n'
print >>sys.stderr, 'sending "%s"' % message
sock.send(message)

# Receive data for the last command
data1 = sock.recv(40000)
print data1

time.sleep(3)

# Sending show channels command and receiving the output
sock.send("api show channels\n\n")
time.sleep(2)
channelData = sock.recv(4000)
print channelData

sock.close()

'''
ch = channelData.split()

if '2' in ch:
	print 'ok' '''