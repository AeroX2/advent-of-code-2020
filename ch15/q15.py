

data = [13,0,10,12,1,5,8]
last_spoken = data[-1]

spoken = { v:[i+1] for i,v in enumerate(data) }

for i in range(len(data)+1, 2021):
    if (last_spoken in spoken and len(spoken[last_spoken]) > 1):
        speak = spoken[last_spoken][-1] - spoken[last_spoken][-2]
    else:
        speak = 0
    #print(speak)

    if (speak in spoken):
        spoken[speak].append(i)
    else:
        spoken[speak] = [i]

    last_spoken = speak
print(last_spoken)
