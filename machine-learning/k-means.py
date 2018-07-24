import sys
import math
import random

# python3 k-means.py ionosphere/ionosphere.data ionosphere/ionosphere.trainlabels.0

class K_Means(object):

    def __init__(self, data, k):
        self.data = data
        self.m = self.initialize(data, k)

    def initialize(self, data, k):
        # Means list
        m = []
        
        for i in range(0, k):
            m.append([0]*len(data[0]))

        # assign random row to each cluster.
        for j in range(0, k):
            m[j] = data[random.randrange(0, (len(data)-1))]
        
        return m

    def distance(self, x, k):
        sm = sum([(m - n)**2 for m, n in zip(x, k)])
        return math.sqrt(sm)

    def findCluster(self, data, m, k):

        dMin = float('inf')
        c = None
        # Calculate the distance of the current row to all of the means
        for j in range(0, k):

            #calculate the distance to the mean
            d = self.distance(data, m[j])
            #print("Cluster: {} | distance: {} | min: {}".format(j, d, dMin))
            if(d < dMin):
                dMin = d
                c = j

        return c

    def cluster(self, data, k):
        cols = len(data[0])
        y = {}

        m = self.initialize(data, k)

        # Initial means values to compares against.
        prev = [[0]*cols for x in range(k)]

        delta = 1
    
        while ((delta) > 0):

             # Reset the counts of items in each cluster
            n=[0.1]*k

            # Calculate the distance from each row to the closest cluster
            for i in range(0, len(data)):

                # Find the closest cluster to the current row
                c = self.findCluster(data[i], m, k)
                
                # Save the cluster label.
                y[i] = c
                n[c] += 1

            # Reset/recalculate the means for each cluster
            m = [[0]*cols for x in range(k)]
            
            for i in range(0, len(data)):
                for p in range(0, k):

                    if(y.get(i) == p):
                        # Sum up the column values.
                        for j in range(0, len(data[i])):
                            m[p][j] += data[i][j]

            
            for i in range(0, k):
                for j in range(0, cols):
                    m[i][j] = m[i][j]/n[i]

           

            mdist = [0]*k

            # Get the distance between the previous means. 
            for p in range(0, k):
                mdist[p] = self.distance(prev[p], m[p])

            # Save the mean values of the current iteration.
            prev=m

            # Calculate the total distance to check of there is any difference between the previous 
            # iteration
            delta = sum(mdist)

        return y

# Read Data
def readData(filename):
    file = open(filename)
    data = []

    i = 0
    line = file.readline()

    while(line != ''):
        a = line.split()
        values = []
        for j in range(0, len(a), 1):
            values.append(float(a[j]))
        data.append(values)
        line = file.readline()

    file.close()

    return data

if __name__ == "__main__":

    # read datafile
    data = readData(sys.argv[1])

    #get the K value
    k = 2
    if(len(sys.argv) == 3):
        k = sys.argv[2]
    
    km = K_Means(data, int(k))

    result = km.cluster(data, int(k))
    for i in range(0, len(result)):
        print("{} {}".format(result[i], i))

