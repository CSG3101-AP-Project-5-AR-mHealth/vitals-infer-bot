#!/usr/bin/env python
# coding: utf-8

# In[10]:


# importing the required module
import time
import json
from tqdm import tqdm
import matplotlib.pyplot as plt


# In[11]:


# Opening JSON file
f = open('heart_rate.json',"r")
strdata = f.read()
# returns JSON object as 
# a dictionary

data = json.loads(strdata)
# Closing file
f.close()


# In[12]:


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


# In[13]:


RV = X
INF_V  = []
Beacon_points = []
print('total len: ',len(RV))
VR_Gap = 0.15
VR = 0.017
i=1
while i<len(RV):
    if (RV[i]-RV[i-1])>0:
        while (RV[i]-RV[i-1])>=0:
            i+=1
            if i>=len(RV):
                break
        Beacon_points.append(i)
        INF_V.append(RV[i-1]) 
        
    elif (RV[i]-RV[i-1])<0:
        while (RV[i]-RV[i-1])<=0:
            
            i+=1
            if i>=len(RV):
                break
        Beacon_points.append(i)
        INF_V.append(RV[i-1]) 
    else:
        i+=1
    
    


# In[25]:



print('length of the beacon-data : ', len(INF_V))
print('length of the beacon-data-points : ', len(Beacon_points))


# In[24]:



# plotting the points
plt.figure(figsize=(30, 10))
# plot mins and maxs
plt.plot(Beacon_points, INF_V,color='g')
# plot original data
plt.plot(Y, X,color='r')
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('Original vs Min-Max')
 
# function to show the plot
plt.show()


# In[ ]:




