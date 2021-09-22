import time
import json
from tqdm import tqdm
from numpy import trapz

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
        
    

def find_INF_points(X):
    RV = X
    INF_V  = []
    Beacon_points = []
    print('total len: ',len(RV))

    VR_Gap = 0.3
    VR = 0.1

    i = 1
    INF_V.append(RV[i])
    Beacon_points.append(i)
    j = 0
    while i<len(RV):
    #     print(j)
        if (RV[i]-RV[i-1])>0:
            while (RV[i]-RV[i-1])>=0:
                i+=1
                if i>=len(RV):
                    break
            
            i=i-1
            Beacon_points.append(i)
            INF_V.append(RV[i]) 
            j+=1
            
            if (INF_V[j] - INF_V[j-1]) > VR_Gap:
                # INF_V[j] = RV[INF_V[j] - INF_V[j-1]]
                pass

            if abs(RV[i]-INF_V[j-1])> VR*INF_V[j-1]:
                INF_V[j] = RV[i]
                
            if (INF_V[j] - INF_V[j-1]) > VR_Gap:
                # INF_V[j] = RV[INF_V[j] - INF_V[j-1]]
                pass
            
        elif (RV[i]-RV[i-1])<0:
            while (RV[i]-RV[i-1])<=0:
                
                i+=1
                if i>=len(RV):
                    break
            i=i-1
            Beacon_points.append(i)
            INF_V.append(RV[i])
            j+=1
    #         print('j is',j)
    #         print('inf_v : ', (INF_V))
            if (INF_V[j] - INF_V[j-1]) > VR_Gap:
                # INF_V[j] = RV[INF_V[j] - INF_V[j-1]]
                pass

            if abs(RV[i]-INF_V[j-1])> VR*INF_V[j-1]:
                INF_V[j] = RV[i]
                
            if (INF_V[j] - INF_V[j-1]) > VR_Gap:
                # INF_V[j] = RV[INF_V[j] - INF_V[j-1]]
                pass
            
        i+=1
        
    return INF_V, Beacon_points
    # print('total len: ',len(INF_V)) 


def find_areas(X, INF_V):
    Su_points=[]
    Sl_points =[]
    So_Area = 0
    # temp_Area = 0
    for rv,inf in zip(X,INF_V):
        if inf>rv:
            Su_points.append(inf-rv)
        elif inf<=rv:
            Sl_points.append(rv-inf)
        
    So = trapz(X, dx=5)

    Su = trapz(Su_points, dx=5)

    Sl = trapz(Sl_points, dx=5)
    
    print('So area: ',So)

    print('Sl area: ',Sl)
    print('Su area: ',Su)

    S = Su + Sl
    print('S area: ',S)
    return(So, Su, Sl, S)