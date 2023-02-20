import sys, os
import random
import math


NUMPLAYERS = 11
NUMROUNDS = 4

MAXTRIES = 100000


def addPods(pods, l):
	i=0
	pod = []
	if len(l)%4 == 0:
		num3pods = 0
	else:
		num3pods = 4-len(l)%4

	for p in l:
		i+=1
		pod.append(p)
		#Si ya se llenaron los pods de 3 jugadores
		if num3pods <= 0:
			if i == 4:
				pods.append(set(pod))
				pod = []
				i = 0
		else:
			if i == 3:
				pods.append(set(pod))
				pod = []
				i = 0
				num3pods -= 1
	return pods


def generatePods(l):
	pods = []

	r = l.copy()
	for i in range(0, NUMROUNDS):
		random.shuffle(r)
		pods = addPods(pods, r)
		
	return pods


def checkPods(pods, l):
	#Si en dos pods repiten 3 o mas personas
	for i in range(0, len(pods)):
		pod = pods[i]
		for j in range(0, len(pods)): 
			if i > j:
				if len(pod.intersection(pods[j])) >= 3:
					return False

	#Si alguien se encuentra 3 veces con el mismo oponente
	for player in l:
		opEncounters = [0]*len(l)
		for pod in pods:
			if pod.intersection(set([player])) != set([]):
				for op in pod:
					if op != player:
						#Contar cuantas veces te encuntras con cada oponente
						opEncounters[op-1]+=1
		for numEncounters in opEncounters:
			if numEncounters >= 3:
				return False

	#Si hay pods de 3 que estén repartidos
	if len(l)%4 != 0:
		#Por cada pod de 3 se anotan los jugadores
		counter3pods = [0]*len(l)
		for pod in pods:
			if len(pod) == 3:
				for p in pod:
					counter3pods[p-1] += 1

		minimum = min(counter3pods)
		maximum = max(counter3pods)
		if minimum != 0:
			for i in range(0,len(counter3pods)):
				counter3pods[i] -= minimum
			
		if max(counter3pods) >= 2:
			return False
		#else:
		#	print("El jugador con menos pods de tres participa en " + str(minimum) + " pods de tres.")
		#	print("Y el jugador con mas pods de tres participa en " + str(maximum) + " pods de tres." )

	return True


if __name__ == "__main__":
	l=[]

	#Initiallize l
	i=0
	while i < NUMPLAYERS:
		i += 1
		l.append(i)


	numtries=0
	validPods = False
	while not validPods:
		pods = generatePods(l)
		validPods = checkPods(pods, l)
		numtries+=1
		if numtries > MAXTRIES:
			print("Maximum number of tries reached. Exiting.")
			exit()
	
	print("Número de jugadores: " + str(NUMPLAYERS))
	podsPerRound = math.ceil(NUMPLAYERS/4)
	numPods = 0
	for i in range(0, NUMROUNDS):
		print()
		print("Ronda " + str(i+1) +":")
		r = []
		for j in range(0, podsPerRound):
			r.append(pods[i*podsPerRound + j])
		for j in range(0, len(r)):
			print("   - ", end='')
			for p in r[len(r)-j-1]:
				print(str(p) + ' '*(4-len(str(p))), end='')
			print()
			


	#print(str(numtries)+ " tries.")
	#print(pods)


