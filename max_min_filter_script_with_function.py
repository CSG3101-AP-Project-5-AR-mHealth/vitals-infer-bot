import time
import json
from tqdm import tqdm
import matplotlib.pyplot as plt
import beacon


# Opening JSON file
f = open('heart_rate.json',"r")
strdata = f.read()
# returns JSON object as a dictionary

data = json.loads(strdata)
# Closing file
f.close()

# start time
start_time = time.time()

X, Y= beacon.parse_bpm(data)

print(time.time()- start_time, "seconds")

Beacon_list, Beacon_points = beacon.find_max_min(X)


print('length of the beacon-data : ', len(Beacon_list))
print('length of the beacon-data-points : ', len(Beacon_points))
