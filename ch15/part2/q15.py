

data = [13,0,10,12,1,5,8]
last_spoken = data[-1]

spoken = { v:(None,i+1) for i,v in enumerate(data) }

for i in range(len(data)+1, 30000001):
    if (last_spoken in spoken and spoken[last_spoken][0] is not None):
        speak = spoken[last_spoken][-1] - spoken[last_spoken][-2]
    else:
        speak = 0
    #print(speak)

    if (speak in spoken):
        v = spoken[speak]
        spoken[speak] = (v[1],i)
    else:
        spoken[speak] = (None,i)

    last_spoken = speak
print(last_spoken)
