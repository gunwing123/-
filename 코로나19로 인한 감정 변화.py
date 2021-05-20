import matplotlib.pyplot as plt
import numpy as np
import json
import urllib.request as request 

json_str = request.urlopen("url").read()#https://data.go.kr/data/15077858/fileData.do에 들어가서 Api주소 받고 url에 넣기
d = json.loads(json_str)

down = [0,0,0,0,0,0,0,0]
ud = [0,0,0,0,0,0,0,0]
up = [0,0,0,0,0,0,0,0]
name= [0,0,0,0,0,0,0,0]
count = 0

while count<8:
    for e in  d['data']:
        a = e['감소']#감소 데이터
        down[count] = a
        a = e['증가']
        up[count] = a#증가 데이터
        a = e['항목']
        name[count] = a#이름 데이터
        count = count + 1
count = len(name)
a = 0

while a<count:
    down[a] = float(down[a])
    up[a] = float(up[a])
    ud[a] = up[a] - down[a]
    a = a+1#자료형 변환 str→int
    
plt.rc('font', family='NanumGothic')
fig, ax = plt.subplots(3,1,constrained_layout=True)
plt.suptitle('코로나19로 인한 국민들의 감정 변화', fontsize = 30)#제목
x = np.arange(len(name))#그래프 기본 바탕

plt.subplot(311)#증가 값 그래프
plt.bar(name, up, label = '증가', color = 'steelblue', width=0.3)
plt.xticks(fontsize=15)
plt.title('\n증가 값', fontsize = 20)
plt.subplot(312)#감소 값 그래프
plt.bar(name, down, label = '감소', color = 'grey', width=0.3)
plt.title('\n감소 값', fontsize = 20)
plt.xticks(fontsize=16)
plt.subplot(313)#증가-감소값 그래프
plt.bar(name, ud, label = '증가 - 감소',  color = 'black', width=0.3)
plt.title('\n증가 - 감소 값', fontsize = 20)
plt.xticks(fontsize=16)

plt.show()
