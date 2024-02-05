import pandas as pd
import numpy as np
import operator
dataset = pd.read_csv("final_test.csv")
def dist(training_set, test_set,length):
    dist=0
    for i in range(length):
        dist=dist+np.square(training_set[i]-test_set[i])
    dist2=np.sqrt(dist)
    return dist2

def knn(training_set, test_set, k):
    distance={}
    count1=0
    count2=0
    flag_index=0
    length=len(test_set[1])
#    print(training_set.iloc[2])
    for x in range(len(training_set)):
        d=dist(training_set.iloc[x], test_set, length)
        distance[x]=d[0]
    sort_distance=sorted(distance.items(),key=operator.itemgetter(1))
    #print(sort_distance)
    neighbors=[]
    for i in range(k):
        neighbors.append(sort_distance[i][0])
    #print(neighbors)
    for i in range(k):
        for j in range(i+1,k):
            if (training_set.iloc[neighbors[i],-1]==training_set.iloc[neighbors[j],-1]):
                count1+=1
        if(count1>=count2):
            count2=count1
            flag_index=neighbors[i]
        
    return (training_set.iloc[flag_index],-1)   



# making test data set
testSet = [[3.8, 3.4, 4.8, 3.4, 8]]
test = pd.DataFrame(testSet)

# assigning different values to k
k = 1
k1 = 3
k2 = 11

#supplying test data to the model
neigh = knn(dataset, test, k)
neigh1 = knn(dataset, test, k1)
neigh2 = knn(dataset, test, k2)

# printing output prediction
#knn(dataset,test, k1)
#print(result)
print(neigh)
#rint(result1)
print(neigh1)
#print(result2)
print(neigh2)
