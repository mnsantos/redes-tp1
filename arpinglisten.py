#!/usr/bin/env python

from scapy.all import *
import json
import time

counter = 0
initialtime = time.time()

def monitor_callback(pkt):
  global counter
  #print "src " + pkt.src
  #print "dst " + pkt.dst
  #if pkt.op == 1:
  #  print "op who-has"
  #else:
  #  print "op is-at"
  #print pkt.show()
  p = {"src":pkt.src, "dst":pkt.dst, "psrc":pkt.psrc, "pdst":pkt.pdst, "op":pkt.op, "hwsrc":pkt.hwsrc, "hwdst":pkt.hwdst, "time":time.time()-initialtime}
  jsonObj = json.dumps(p, ensure_ascii=False)
  f = open('out.txt', 'a')
  f.write(",")
  f.write(jsonObj)
  f.write("\n")
  f.close()
  counter = counter+1
  print "wrote ARPs: " + str(counter)
  
if __name__ == '__main__':
  sniff(prn=monitor_callback, filter="arp", store = 0)
  
