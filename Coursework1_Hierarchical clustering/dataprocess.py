from datetime import datetime

def judgetime(day):
	day = day.split(':')
	if(len(day) == 2):
		day.append("00")
	for i in range(len(day)):
		day[i] = int(day[i])
	if(day[0] < 8 and day[0] >= 0):
		return "早休闲"
	if(day[0] >= 8 and day[0] < 12):
		return "上午劳作时"
	if(day[0] == 12 and day[1] == 0 and day[2] == 0):
		return "上午劳作时"
	if(day[0] >= 12 and day[0] < 13):
		return "午休闲"
	if(day[0] >= 13 and day[0] < 17):
		return "下午劳作时"
	if(day[0] == 17 and day[1] == 0 and day[2] == 0):
		return "下午劳作时"
	if(day[0] >= 17 and day[0] <= 24):
		return "晚休闲"

def judgeage(age):
	if(age < 70):
		return "活力老人"
	if(age >= 70):
		if(age <= 79):
			return "行动老人"
		else:
			if(age <= 89):
				return "地上心动老人"
			else:
				return "床上心动老人"

Map = {1:"周一",2:"周二",3:"周三",4:"周四",5:"周五",6:"周六",7:"周天"}

def judgeweek(date):
	date = date.replace("-","")
	week = datetime.strptime(date,"%Y%m%d").weekday() + 1
	return Map[week]

# print(judgeweek("2018-05-25"))s

# U = []
# with open('purchasingLog.txt','r',encoding="utf8") as dataread:
# 	for line in dataread.readlines():
# 		data = []
# 		line = line.strip().replace(" ","").split('T')
# 		data.append(judgeweek(line[0]))
# 		line1 = line[1].split(',')
# 		data.append(judgetime(line1[0]))
# 		data.append(judgeage(int(line1[1])))
# 		data.append(line1[2])
# 		U.append(data)
# print(U)