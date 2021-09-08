


# importing the required module
import time
import json
from tqdm import tqdm







f = open('heart_rate.json',"r")
strdata = f.read()
# returns JSON object as a dictionary

data = json.loads(strdata)

f.close()





# start time
start_time = time.time()
# declare lists
X = []
Y = []

x=0
for i in tqdm(data):
    temp = i['value']
    bpm = temp['bpm']
    X.append(bpm)
    Y.append(x)
    x+=1
print(time.time()- start_time, "seconds")




RV = X
Beacon_list  = []
Beacon_points = []
print('total len: ',len(RV))

i=1
while i<len(RV):
    if (RV[i]-RV[i-1])>0:
        while (RV[i]-RV[i-1])>=0:
            i+=1
            if i>=len(RV):
                break
        Beacon_points.append(i)
        Beacon_list.append(RV[i-1]) 
        
    elif (RV[i]-RV[i-1])<0:
        while (RV[i]-RV[i-1])<=0:
            
            i+=1
            if i>=len(RV):
                break
        Beacon_points.append(i)
        Beacon_list.append(RV[i-1]) 
    else:
        i+=1
    
    






print('length of the beacon-data : ', len(Beacon_list))
print('length of the beacon-data-points : ', len(Beacon_points))







