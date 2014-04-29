import json
import math

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
			
if __name__ == '__main__':
	file = open("out.txt")
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
	
	

	
