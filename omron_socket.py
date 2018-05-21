#!/usr/bin/env python 
#created by dshowing

from socket import *
from time import ctime
import binascii

HOST = '192.168.238.130'
PORT = 9600
BUFSIZE = 1024
ADDR = (HOST, PORT)

INFODATA1 = "46494e53000000100000000100000000000000ef00000005"
INFODATA2 = "46494e53000000720000000200000000c0000200efef0005000505010000434a324d2d43505533312020202020202020202030322e3031000000000030322e3130000000000000010000000000000000000000000000000000010000800180018001800000000000000000020100000a17800008010000000000"
INFODATA3 = "46494e53000000720000000200000000c0000200fbef00010005050100004350314c2d454d343044522d440000002020202030312e3030000000000030312e3038000000000000000000000000000000000000000000000000010000000000000000000000000000000000010100001417800008000000000000"

s = socket(AF_INET, SOCK_STREAM)
s.bind(ADDR)
s.listen(5)


while True:
    try:
    	print 'Waiting for connection ....'
    	conn, addr = s.accept()
    	print 'Connected client from:' , addr
        
    	while True:
            data = conn.recv(BUFSIZE)
            if not data:
                #print 'not data'
                break
            else:
                print 'Client: ', data.encode('hex')
                if data.encode('hex') == '46494e530000000c000000000000000000000000':
                    #print 'data is fins'
                    conn.sendall(binascii.a2b_hex(INFODATA1))
                    #print 'send fins recv'
                    data1 = conn.recv(BUFSIZE)
                    #print data1.encode('hex')
                    if data1.encode('hex') == '46494e530000001500000002000000008000020005000000ef05050100':
                        #print 'data is find1'
                        conn.sendall(binascii.a2b_hex(INFODATA3))
                        print 'send dev_info\nCycle Over !'
                    else:
                        break
                else:
                    break
    except Exception,e:
        print 'Error: ',e
s.close()
