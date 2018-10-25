import re
import random
import numpy as np
import time


t1 = print(time.time())

print("Data construct..")

def timeConvert(time):
	time = time.split(':')
	Tsum = int(time[0])*3600 + int(time[1])*60 + int(time[2])
	return Tsum

Data = []
Pepole = set()
Eat = set()

with open('log.txt', 'r',encoding="utf8") as fread:
	for line in fread.readlines():
		data = line.strip().split('_')
		data = (data[0],data[1].split(','))
		data[1][0] = timeConvert(data[1][0])
		Data.append(data)
		Pepole.add(data[1][1])
		# Day.add(data[0])
		Eat.add(data[1][2])
Stu = list(Pepole)
Eat = list(Eat)

print("Stu index")
Stu_indices = dict((s,i) for i, s in enumerate(Stu))
Indices_Stu = dict((i,s) for i, s in enumerate(Stu))

print("Matrix construct..")
# Matrix = np.zeros([len(Stu),len(Stu)])
Matrix = []
for i in range(len(Stu)):
	matrix = []
	for j in range(len(Stu)):
		matrix.append(0)
	Matrix.append(matrix)

print("Data dividing")
U = []
for i in Eat:
	Ui = []
	for data in Data:
		if(data[1][2] == i):
			Ui.append(data)
	U.append(Ui)

print(len(U[0]))
print(len(U[1]))
print(len(U[2]))


def AddID(i,N,Aid,Atime,Aday):
	while(N < len(U[i])): #len(U[i])
		Bdata = U[i][N]
		if(Aday == Bdata[0]):
			if(Bdata[1][0] - Atime <= 300):
				Bpoint = Stu_indices.get(Bdata[1][1])
				Apoint = Stu_indices.get(Aid)
				Matrix[Apoint][Bpoint] += 1
				Matrix[Bpoint][Apoint] += 1
			else:
				break
		else:
			break
		N += 1

print("Computing data...")
for i,ui in enumerate(U):
	for N,data in enumerate(ui):
		Aid = data[1][1]
		Atime = data[1][0]
		Aday = data[0]
		AddID(i,N,Aid,Atime,Aday)

# for N,data in enumerate(U[0]):
# 	Aid = data[1][1]
# 	Atime = data[1][0]
# 	Aday = data[0]
# 	AddID(0,N,Aid,Atime,Aday)

t2 = print(time.time())			

baseline = np.zeros(len(Stu))
with open('log.txt', 'r',encoding="utf8") as fread:
	for line in fread.readlines():
		data = line.strip().split('_')
		# data = (data[0],data[1].split(','))
		data = data[1].split(',')
		# people = data[1][1]
		people = data[1]
		index = Stu_indices.get(people)
		baseline[index] += 1

# baseline = []
# for i in range(len(Stu)):
# 	ssum = 0
# 	for j in range(len(Stu)):
# 		ssum += Matrix[i][j]
# 	baseline.append(ssum)
print(baseline)
print(len(Stu))

Friend = []
for i in range(len(Stu)):
	friend = []
	for j in range(len(Stu)):
		if(Matrix[i][j]*4 >= baseline[i]):
			friend.append(Indices_Stu.get(j))
	Friend.append(friend)

# print(Friend)


# print(Matrix[0])
# print(Matrix[1])

index = Stu_indices.get('0')
fr = []
for j in range(len(Stu)):
	if(Matrix[index][j]*4 >= baseline[index]):
		fr.append(Indices_Stu.get(j))
print(fr)
