import time
import json
from tqdm import tqdm

def parse_bpm(data):
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
    return X, Y


def find_max_min(X):

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

    return Beacon_list, Beacon_points
        
    

