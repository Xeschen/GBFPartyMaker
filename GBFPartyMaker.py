import sys

def init():
    global joblist
    joblist = []
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

def parse():
    global datalist
    datalist = []
    f = open("data.txt", 'r')
    line = f.readline()

    while True:
        line = f.readline()
        if not line:
            break
        t = line.split('\t')
        t[0] = int(t[0])
        t[1] = int(t[1])
        t[2] = int(t[2])
        t[3] = t[3].split('\n')[0]
        datalist.append(t)

    f.close()
    return

def search():
#    for job in joblist:
    job = [2, 7, 1, '스파르타']
    for i in range(0, 2):
        akasha = akashaIndex(job[i+1])
        akashaSet = set();
        for data in datalist:
            if data[1] in akasha or data[2] in akasha:
                akashaSet.add(data[0])
        print(akashaSet)


init()
parse()
search()
