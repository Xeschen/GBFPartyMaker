import sys

def init():
    global joblist
    joblist = [[]]
    joblist = joblist + [[1, 7, 3, '버서커'], [2, 7, 1, '스파르타'], [3, 5, 1, '세이지'], [4, 5, 4, '워록'], [5, 4, 10, '의적'], [6, 7, 4, '카오스루다'], [7, 6, 6, '레슬러'], [8, 2, 10, '하운드독'], [9, 9, 4, '엘류시온'], [10, 1, 3, '아프사라스']]
    joblist = joblist + [[11, 7, 8, '글로리'], [12, 5, 5, '흑묘도사'], [13, 8, 2, '검호'], [14, 8, 6, '마법전사'], [15, 4, 10, '닥터']]

def akashaIndex(a):
    if a in [1, 8]:
        return [1, 8]
    elif a in [2, 10]:
        return [2, 10]
    elif a in [3, 6]:
        return [3, 6]
    elif a in [4, 7]:
        return [4, 7]
    elif a in [5, 9]:
        return [5, 9]

def akashaHangul(a):
    if a == [1, 8]:
        return '창'
    elif a == [2, 10]:
        return '활'
    elif a == [3, 6]:
        return '도끼'
    elif a == [4, 7]:
        return '검'
    elif a == [5, 9]:
        return '지팡이'

def omegaHangul(a):
	if a == 1:
		return '창'
	elif a == 2:
		return '활'
	elif a == 3:
		return '도끼'
	elif a == 4:
		return '단검'
	elif a == 5:
		return '지팡이'
	elif a == 6:
		return '격투'
	elif a == 7:
		return '검'
	elif a == 8:
		return '도'
	elif a == 9:
		return '악기'
	elif a == 10:
		return '총'

def elemHangul(a):
	if a == 0:
		return '화'
	elif a == 1:
		return '수'
	elif a == 2:
		return '토'
	elif a == 3:
		return '풍'
	elif a == 4:
		return '광'
	elif a == 5:
		return '암'
		
def prettyParty(party):
	ret = set()
	for p in party:
		li = []
		li.append(findCharaName(p[0]))
		li.append(findCharaName(p[1]))
		li.append(findCharaName(p[2]))
		p2 = tuple(li)
		ret.add(p2)
	return ret
		
def findCharaName(num):
	for datum in datalist:
		for data in datum:
			if data[0] == num:
				return data[4]
		
def parse():
	global datalist
	datalist = [[],[],[],[],[],[]]
	f = open("data.txt", 'r', encoding='UTF8')
	line = f.readline()

	while True:
		line = f.readline()
		if not line:
			break
		t = line.split('\t')
		if str(t[0])[0] == '#':
			continue
		t[0] = int(t[0])
		t[1] = int(t[1])
		t[2] = int(t[2])
		t[3] = int(t[3])
		t[4] = t[4].split('\n')[0]
		datalist[t[1]].append(t)

	f.close()
	return

def search(job, elem):
#	job = [2, 7, 1, '스파르타']
#	elem = 2
	print('속성: '+elemHangul(elem))
	print('직업: '+job[3])
	print('오메가\t아카샤')
	for i in range(0, 2):
		akasha = akashaIndex(job[i+1])
		if i == 1 and akashaIndex(job[1]) == akashaIndex(job[2]):
			continue
		akashaSet = set()
		for data in datalist[elem]:
			if data[2] in akasha or data[3] in akasha:
				akashaSet.add(data[0])
		for j in range(0, 2):
			omega = job[j+1]
			if j == 1 and job[1] == job[2]:
				continue
			omegaSet = set()
			for data in datalist[elem]:
				if omega in data[2:4]:
					omegaSet.add(data[0])
			coreSet = akashaSet & omegaSet
			domainSet = akashaSet | omegaSet
			if coreSet == set():
				continue
			party = set()
			for core in coreSet:
				possibility = []
				possibility.append(core)
				for core2 in omegaSet - {core}:
					temp = possibility.copy()
					temp.append(core2)
					for b in domainSet - {core, core2}:
						temp2 = temp.copy()
						temp2.append(b)
						temp2.sort()
						party.add(tuple(temp2))
			if party == set():
				continue
			print(omegaHangul(omega)+'\t'+akashaHangul(akasha)+'\t'+str(prettyParty(party)))
	print('\n')
		
def searchWhole():
	for elem in range(0,6):
		for job in joblist:
			search(job, elem)
		
def searchElem(elem):
	for job in joblist:
		search(job, elem)
	
def searchJob(job):
	for elem in range(0,6):
		search(joblist[job], elem)

		
init()
parse()
searchJob(10)







