import os
from dataprocess import judgeweek,judgeage,judgetime

def GetTree(filename):
	Ainput = []
	with open("tree/" + filename, 'r',encoding="utf8") as fread:
		for line in fread.readlines():
			line = line.strip()
			line = line.replace(' ', '')
			linelist = line.split("##")
			# print(linelist)
			Ainput.append(linelist)
	Ainput[0][0] = '0'
	Ainput.reverse()

	Amap = {}
	# Amap['name']=1
	for i in Ainput:
		Amap[i[2]] = int(i[0])
	# print(Amap)

	TreeA = []
	for i in range(len(Ainput)):
		TreeA.append([])

	for i in range(len(Ainput)):
		ID = Ainput[i][0]
		for j in range(len(Ainput)):
			if(Ainput[j][1] is ID):
				# TreeA[i][j] = 1
				TreeA[i].append(1)
			else:
				# TreeA[i][j] = -1
				TreeA[i].append(-1)
		TreeA[i][i] = 0

	for i in range(len(TreeA)):
		# print(TreeA[i])
		for j in range(len(TreeA[i])):
			# print(TreeA[i][j])
			if TreeA[i][j] > 0:
				index = j
				for k in range(len(TreeA[index])):
					if TreeA[index][k] > 0:
						TreeA[i][k] = TreeA[index][k] + 1

	TreeA.reverse()
	for i in range(len(TreeA)):
		TreeA[i].reverse()

	return TreeA,Amap

def read_tree():		
	Tree = []
	Map = []
	filenames = os.listdir("tree")
	for filename in filenames:
		# print(filename)
		Atree = []
		Amap = []
		Atree,Amap = GetTree(filename)
		# print(Atree,Amap)
		Tree.append(Atree)
		Map.append(Amap)
	return Tree,Map

Tree,Map = read_tree()
print("Tree")
print(Tree)
print("Map")
print(Map)

# data
# data1 = ['周一', '上午劳作时', '行动老人', '80']
# data2 = ['周二', '上午劳作时', '行动老人', '90']
# data3 = ['周六', '上午劳作时', '活力老人', '120']
# data4 = ['周天', '下午劳作时', '活力老人', '100']
# data5 = ['周五', '晚休闲', '地上心动老人', '70']
# U = [data1,data2,data3,data4,data5]
# print(U)
# for i in range(len(U)):
# 	for j in range(len(Tree)):
# 		U[i][j] = Map[j][U[i][j]]
# print(U)

U = []
with open('purchasingLog.txt','r',encoding="utf8") as dataread:
	for line in dataread.readlines():
		data = []
		line = line.strip().replace(" ","").split('T')
		data.append(judgeweek(line[0]))
		line1 = line[1].split(',')
		data.append(judgetime(line1[0]))
		data.append(judgeage(int(line1[1])))
		data.append(line1[2])
		U.append(data)
for i in range(len(U)):
	for j in range(len(Tree)):
		U[i][j] = Map[j][U[i][j]]
# print(U)

# topic 
T = 0.3
S = 0.8
topic_total = 0
for data in U:
	topic_total += float(data[len(data)-1])
topic = topic_total*T
print(topic)

# once julei
def search(U,abstract_tree):
	distance = 0
	topic_number = 0
	number = 0
	for data in U:
		dis = 0
		judge = 0
		for i in range(len(abstract_tree)):
			# print(type(data[i]))
			# print(data[i])
			if(Tree[i][abstract_tree[i]][data[i]] >= 0):
				dis += Tree[i][abstract_tree[i]][data[i]]
			else:
				judge = 1
				break
		if(judge is 0):
			dis = 1.0*dis/len(abstract_tree)
			topic_number += float(data[len(data)-1])
			distance += dis
			number += 1
	if(number > 0):
		distance = 1.0*distance/number
	return topic_number,distance


def xunhuan(j,Set,flag,abstract_set,abstract_tree):
	Set[j].clear()
	for i in range(len(Tree[j])):
		if(i in Set[j]):
			continue
		abstract_tree[j] = i
		if(j+1 is len(Tree)-1):
			Set[j+1].clear()
			flag[j] = 0
			for k in range(len(Tree[j+1])):
				if(k in Set[j+1]):
					continue
				abstract_tree[j+1] = k
				topic_number,distance = search(U,abstract_tree)
				if(topic_number >= topic):
					for f in range(len(flag)):
						flag[f] = 1
					if(distance <= S):
						abt = []
						for i in range(len(abstract_tree)):
							abt.append(abstract_tree[i])
						abstract_set.append((abt,distance))
				else:
					for m in range(len(Tree[j+1][k])):
						if(Tree[j+1][k][m] > 0):
							Set[j+1].add(m)
			if(flag[j] is 0):
				for n in range(len(Tree[j][i])):
					if(Tree[j][i][n] > 0):
						Set[j].add(i)
		else:
			flag[j] = 0
			xunhuan(j+1,Set,flag,abstract_set,abstract_tree)  # j+1 溢出
	if(j > 0):
		if(flag[j-1] is 0):
			for n in range(len(Tree[j-1][i])):
				if(Tree[j-1][i][n] > 0):
					Set[j-1].add(n)


def Clustering():
	Set = []
	abstract_set = []
	abstract_tree = []
	flag = []
	for i in range(len(Tree)):
		seti = set()
		Set.append(seti)
	for i in range(len(Tree) - 1):
		flagi = 0
		flag.append(flagi)
	for i in range(len(Tree)):
		abt = -1
		abstract_tree.append(abt)
	xunhuan(0,Set,flag,abstract_set,abstract_tree)
	# Set = []
	# abstract_set = xunhuan(0,abstract_set,abstract_tree,flag,Set)

	# abstract_set = []

	# seti = set()
	# for i in range(len(Tree[0])):
	# 	# print(seti)
	# 	if(i in seti):
	# 		continue


	# 	setj = set()
	# 	jflag = 0
	# 	for j in range(len(Tree[1])):
	# 		# print(setj)
	# 		if(j in setj):
	# 			continue


	# 		setk = set()
	# 		kflag = 0
	# 		for k in range(len(Tree[2])):
	# 			if(k in setk):
	# 				# print("HH")
	# 				continue
	# 			abstract_tree = [i,j,k]
	# 			# print(abstract_tree)
	# 			topic_number,distance = search(U,abstract_tree)
	# 			# if(i is 1 and j is 6 and k is 1):
	# 			# 	print("jjjj")
	# 			# 	print(topic_number,topic,distance,S)
	# 			if(topic_number >= topic):
	# 				kflag = 1
	# 				jflag = 1
	# 				if(distance <= S):
	# 					print(abstract_set)
	# 					abstract_set.append((abstract_tree,distance))
	# 			else:
	# 				for m in range(len(Tree[2][k])):
	# 					if (Tree[2][k][m] > 0):
	# 						setk.add(m)


	# 		if(kflag is 0):
	# 			for n in range(len(Tree[1][j])):
	# 				if (Tree[1][j][n] > 0):
	# 					setj.add(j)


	# 	if(jflag is 0):
	# 		for h in range(len(Tree[0][i])):
	# 			if(Tree[0][i][h] > 0):
	# 				seti.add(i)

	# print(abstract_set)
	abstract_set = sorted(abstract_set,key=lambda abstract_set: abstract_set[1])
	if(abstract_set):
		return abstract_set[0][0]
	else:
		return -1

def emit(abstract_tree):
	set_emit = []
	for data in U:
		judge = 0
		for i in range(len(abstract_tree)):
			if(Tree[i][abstract_tree[i]][data[i]] < 0):
				judge = 1
		if(judge is 0):
			set_emit.append(data)
	for data in set_emit:
		U.remove(data)


while(1):
	abstract = Clustering()
	if(abstract is -1):
		# print("QQQ")
		break
	else:
		# print("HHH")
		print(abstract)
		emit(abstract)
		# print(U)

# abstract = Clustering()
# print(abstract)





