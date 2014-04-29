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
	
def inf_who_has_emitidos(array, ip):
	cont = 0
	for dic in array:
		if dic["op"]==1 and dic["psrc"]==ip:
			cont = cont + 1
	prob = float(cont)/len(array)
	if prob!=0:
		return -math.log(prob,2)
	else:
		return 0
		
def inf_who_has_recibidos(array, ip):
	cont = 0
	for dic in array:
		if dic["op"]==1 and dic["pdst"]==ip:
			cont = cont + 1
	prob = float(cont)/len(array)
	if prob!=0:
		return -math.log(prob,2)
	else:
		return 0

def graficador_1(data):

	n_groups = len(data)
	ips = []
	sent_who_has = []

	for d in data:
		ips.append(d[0])
		sent_who_has.append(d[1])

	index = np.arange(n_groups)

	bar_width = 0.4
	opacity = 0.4

	rects1 = plt.bar(index, sent_who_has, bar_width, alpha=opacity, color='blue', label='who_has enviados')

	plt.xlabel('Direcciones de IP')
	plt.ylabel('#Informacion')
	plt.ylim([0,15])
	plt.title('Mediciones tomadas en el starbucks')
	plt.xticks(index+bar_width*2, ips)
	plt.xticks(rotation=-60)
	plt.legend()
	plt.tight_layout()
	

	plt.savefig("sent_who_has")	
	plt.close()

def graficador_2(data):

	n_groups = len(data)
	ips = []
	received_who_has = []

	for d in data:
		ips.append(d[0])
		received_who_has.append(d[2])

	index = np.arange(n_groups)

	bar_width = 0.8
	opacity = 0.4

	rects2 = plt.bar(index, received_who_has, bar_width, alpha=opacity, color='red', label='who_has_recibidos')

	plt.xlabel('Direcciones de IP')
	plt.ylabel('#Informacion')
	plt.ylim([0,15])
	plt.title('Mediciones tomadas en el starbucks')
	plt.xticks(index+bar_width*2, ips)
	plt.xticks(rotation=-60)
	plt.legend()
	plt.tight_layout()

	plt.savefig("received_who_has")	
	plt.close()

			
if __name__ == '__main__':
	file = open(sys.argv[1])
	file = file.read()
	decoded_data = json.loads(file)
	conj = ips(decoded_data)
	ls=[]
	while len(conj)!=0:
		l=[]
		ip = conj.pop()
		inf1 = inf_who_has_emitidos(decoded_data,ip)
		inf2 = inf_who_has_recibidos(decoded_data,ip)
		l.append(ip)
		l.append(inf1)
		l.append(inf2)
		ls.append(l)
	graficador_1(ls)
	graficador_2(ls)
	

	
