import matplotlib.pyplot as plt
import numpy as np
import json
import urllib.request as request 

json_str = request.urlopen("url").read()#https://www.data.go.kr/에 들어가서 Api주소 받고 url에 넣기
d = json.loads(json_str)


down = [0,0,0,0,0,0,0,0]
no = [0,0,0,0,0,0,0,0]
up = [0,0,0,0,0,0,0,0]
name= [0,0,0,0,0,0,0,0]
count = 0
for e in  d['data']:
    a = e['감소']
    down[count] = a
    count = count + 1#모든 감소데이터 받기
count = 0
for e in  d['data']:
    a = e['변화 없음']
    no[count] = a
    count = count + 1#모든 변화 없음데이터 받기
count = 0
for e in  d['data']:
    a = e['증가']
    up[count] = a
    count = count + 1#모든 증가데이터 받기
count = 0
for e in  d['data']:
    a = e['항목']
    name[count] = a
    count = count + 1#모든 감정데어터 받기
count = len(name)

a = 0
while a<count:
    down[a] = float(down[a])
    no[a] = float(no[a])
    up[a] = float(up[a])
    a = a+1#자료형 변환 str→int
    
plt.rc('font', family='NanumGothic')#글씨체 지정

fig, ax = plt.subplots(3,1,constrained_layout=True)#그래프 그리는 부분
x = np.arange(len(name))
plt.subplot(311)#증가비율 그래프
plt.bar(name, up, label = '증가', color = 'red')
plt.xlabel('감정')
plt.title('증가 비율')
plt.subplot(312)#유지비율 그래프
plt.bar(name, no, label = '변화없음',  color = 'black')
plt.xlabel('감정')
plt.title('유지 비율')
plt.subplot(313)#감소비율 그래프
plt.bar(x, down, label = '감소', color = 'blue')
plt.xticks(x, name)
plt.xlabel('감정')
plt.title('감소 비율')

plt.suptitle('코로나19로 인한 국민들의 감정 변화', fontsize = 20)#대주제

plt.show()
