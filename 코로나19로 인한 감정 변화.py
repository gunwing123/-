import matplotlib.pyplot as plt
import numpy as np
import json
import urllib.request as request 

json_str = request.urlopen("https://api.odcloud.kr/api/15077858/v1/uddi:a337f1a9-e6bf-4aaf-a46d-c8f2dc4fa5ee?page=1&perPage=10&serviceKey=fjAw3O7vBMc7m4yVmBADj7LMXG%2BPhyeCvbQr%2FqAIf3cGCS5lRSXoOSX9MWTHHRx8wo72khXHX9yrIBzX07sBMA%3D%3D").read()
d = json.loads(json_str)


down = [0,0,0,0,0,0,0,0]
no = [0,0,0,0,0,0,0,0]
up = [0,0,0,0,0,0,0,0]
name= [0,0,0,0,0,0,0,0]
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
    up[a] = float(up[a])
    a = a+1
plt.rc('font', family='NanumGothic')
fig, ax = plt.subplots(3,1,constrained_layout=True)

x = np.arange(len(name))



plt.subplot(311)
plt.bar(name, up, label = '증가', color = 'red')
plt.xlabel('감정')
plt.title('증가 비율')
plt.subplot(312)
plt.bar(name, no, label = '변화없음',  color = 'black')
plt.xlabel('감정')
plt.title('유지 비율')
plt.subplot(313)
plt.bar(x, down, label = '감소', color = 'blue')
plt.xticks(x, name)
plt.xlabel('감정')
plt.title('감소 비율')


plt.suptitle('코로나19로 인한 국민들의 감정 변화', fontsize = 20)

plt.show()