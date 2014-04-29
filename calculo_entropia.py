import numpy as np
import matplotlib.pyplot as plt
import json
import math
import sys

def ips(array):
	conj = []
	for dic in array:
		conj.append(dic["psrc"])
		conj.append(dic["pdst"])
	conj = set(conj)
	return conj
			
if __name__ == '__main__':
	file = open(sys.argv[1])
	file = file.read()
	decoded_data = json.loads(file)

	dstCount = 0
	srcCount = 0
	Ssrc = {}
	Sdst = {}
	for dic in decoded_data:
		if dic["op"] == 1:
			if not dic["psrc"] in Ssrc:
				Ssrc[dic["psrc"]] = 0
			Ssrc[dic["psrc"]]+=1
			srcCount+=1

			if not dic["pdst"] in Sdst:
				Sdst[dic["pdst"]] = 0
			Sdst[dic["pdst"]]+=1
			dstCount+=1

	entropy = 0	
	
	for key in Ssrc.keys():	
		prob = float(Ssrc[key])/srcCount		
		inf = 0
		if prob!=0:
			inf = -math.log(prob,2)
		entropy += prob * inf;				
	
	print "Src entropy: " + str(entropy)

	entropy = 0
	
	for key in Sdst.keys():	
		prob = float(Sdst[key])/dstCount
		inf = 0
		if prob!=0:
			inf = -math.log(prob,2)
		entropy += prob * inf;
	
	print "Dst entropy: " + str(entropy)
	
