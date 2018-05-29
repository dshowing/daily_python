#!/usr/bin/env python
# encoding = utf-8

import tail
import time
import sys
import stomp

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)

def send_msg(txt):
    conn = stomp.Connection([('192.168.238.130', 61613)])
    #print 'connectioned'
    #conn.set_listener('', MyListener())
    conn.start()
    conn.connect('admin', 'admin', wait=True)
    conn.send(body=txt, destination='/topic/HoneyPot')
    #print 'sended'
    time.sleep(1)
    conn.disconnect()
    #print 'closed'

t = tail.Tail('/home/doushuo/syslog')
t.register_callback(send_msg)
t.follow(s=1)
