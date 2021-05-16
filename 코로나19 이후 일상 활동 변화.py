import matplotlib.pyplot as plt
import numpy as np
import json
import urllib.request as request 

json_str = request.urlopen("url").read()#https://data.go.kr/data/15077856/fileData.do
d = json.loads(json_str)

down = [0,0,0,0,0,0,0,0,0,0]
no = [0,0,0,0,0,0,0,0,0,0]
case = [0,0,0,0,0,0,0,0,0,0]
up = [0,0,0,0,0,0,0,0,0,0]
name= [0,0,0,0,0,0,0,0,0,0]
count = 0
for e in  d['data']:
    a = e['감소']
    down[count] = a
    count = count + 1
count = 0
for e in  d['data']:
    a = e['변화 없음']
    no[count] = a
    count = count + 1
count = 0
for e in  d['data']:
    a = e['사례수']
    case[count] = a
    count = count + 1
count = 0
for e in  d['data']:
    a = e['증가']
    up[count] = a
    count = count + 1
count = 0
for e in  d['data']:
    a = e['항목']
    name[count] = a
    count = count + 1
count = len(name)

a = 0
while a<count:
    down[a] = float(down[a])
    no[a] = float(no[a])
    case[a] = float(case[a])
    up[a] = float(up[a])
    a = a+1

plt.rc('font', family='NanumGothic')
fig, ax = plt.subplots(2,2,constrained_layout=True)
x = np.arange(len(name))

plt.subplot(221)
plt.pie(case, labels = name, autopct = '%.1f%%')
plt.title('사례수')
plt.subplot(222)
plt.pie(up, labels = name, autopct = '%.1f%%')
plt.title('증가 비율')
plt.subplot(223)
plt.pie(no, labels = name, autopct = '%.1f%%')
plt.title('유지 비율')
plt.subplot(224)
plt.pie(down, labels = name, autopct = '%.1f%%')
plt.title('감소 비율')

plt.suptitle('코로나19 이후 일상 활동 변화', fontsize = 20)

plt.show()
