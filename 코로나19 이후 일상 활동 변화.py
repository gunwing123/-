import matplotlib.pyplot as plt
import numpy as np
import json
import urllib.request as request 

json_str = request.urlopen("url").read()#https://data.go.kr/data/15077856/fileData.do 에 들어가서 Api주소 받고 url에 넣기
d = json.loads(json_str)

down = [0,0,0,0,0,0,0,0,0,0]
no = [0,0,0,0,0,0,0,0,0,0]
case = [0,0,0,0,0,0,0,0,0,0]
up = [0,0,0,0,0,0,0,0,0,0]
name= [0,0,0,0,0,0,0,0,0,0]
count = 0
while count<8:
    for e in  d['data']:
        a = e['감소']#감소 데이터
        down[count] = a
        a = e['변화 없음']
        no[count] = a#변화 없음 데이터
        a = e['증가']
        up[count] = a#증가 데이터
        a = e['항목']
        name[count] = a#이름 데이터
        count = count + 1
count = len(name)

a = 0
while a<count:
    down[a] = float(down[a])
    no[a] = float(no[a])
    up[a] = float(up[a])
    case[a] = down[a] - up[a]
    a = a+1#자료형 변환 str→int

plt.rc('font', family='NanumGothic')
fig, ax = plt.subplots(2,2)
plt.suptitle('코로나19 이후 일상 활동 변화', fontsize = 30)
x = np.arange(len(name))#그래프 기본 바탕

plt.subplot(221)
plt.pie(up, labels = name, autopct = '%.1f%%', textprops={'size':15})
plt.title('증가 비율',fontsize = 20)#증가 비율 그래프
plt.subplot(223)
plt.pie(no, labels = name, autopct = '%.1f%%', textprops={'size':15})
plt.title('유지 비율',fontsize = 20)#유지 비율 그래프
plt.subplot(222)
plt.pie(down, labels = name, autopct = '%.1f%%', textprops={'size':15})
plt.title('감소 비율',fontsize = 20)#감소 비율 그래프
plt.subplot(224)
plt.pie(case, labels = name, autopct = '%.1f%%', textprops={'size':15})
plt.title('감소 - 증가',fontsize = 20) #감소-증가 비율 그래프
plt.show()
