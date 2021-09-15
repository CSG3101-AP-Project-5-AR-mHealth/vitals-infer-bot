import time
import json
from tqdm import tqdm
import matplotlib.pyplot as plt
import beacon


# Opening JSON file
f = open('heart_rate.json',"r")
strdata = f.read()
# returns JSON object as 
# a dictionary

data = json.loads(strdata)
# Closing file
f.close()

# start time
start_time = time.time()

X, Y= beacon.parse_bpm(data[:200])

print(time.time()- start_time, "seconds")

Beacon_list, Beacon_points = beacon.find_max_min(X)
Beacon_list1, Beacon_points1 = beacon.find_INF_points(X)


print('length of the beacon-data : ', len(Beacon_list))
print('length of the beacon-data-points : ', len(Beacon_points))

print('length of the beacon-data1 : ', len(Beacon_list1))
print('length of the beacon-data-points1 : ', len(Beacon_points1))



# plotting the points
plt.figure(figsize=(15, 5))
# plot mins and maxs
plt.plot(Beacon_points, Beacon_list,color='g',label ='min_max')
# plot inf_v final
plt.plot(Beacon_points1, Beacon_list1,color='b',label ='final INF_V')
# plot original data
plt.plot(Y, X,color='r', label ='Orignal')
# Function add a legend  
plt.legend()
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('Graph Analysis')
 
# function to show the plot
plt.show()