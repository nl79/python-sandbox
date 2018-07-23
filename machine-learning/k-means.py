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

        for j in range(0, k):
            m[j] = data[random.randrange(0, (len(data)-1))]
        
        return m

    def train(self, data, k):
        cols = len(data[0])
        rows = len(data)
        y = {}
        diff = 1

        m = self.initialize(data, k)

        prev = [[0]*cols for x in range(k)]

        dist = [0.1]*k

        mdist = [0]*k

        n = [0.1]*k

        totaldist = 1
        classes = []

        while ((totaldist) > 0):
            for i in range(0, rows, 1):

                dist = [0.1]*k

                for p in range(0, k, 1):
                    for j in range(0, cols, 1):
                        dist[p] += ((data[i][j] - m[p][j])**2)

                for p in range(0, k, 1):
                    dist[p] = dist[p]**0.5

                mindist = min(dist)

                for p in range(0, k, 1):
                    if(dist[p]== mindist):
                        y[i] = p
                        n[p] += 1

                        break

            m = [[0]*cols for x in range(k)]
            col = []

            for i in range(0, rows, 1):
                for p in range(0, k, 1):
                    if(y.get(i) == p):
                        
                        for j in range(0, cols, 1):

                            temp = m[p][j]
                            temp1 = data[i][j]
                            m[p][j] = temp + temp1

            for j in range(0, cols, 1):
                for i in range(0, k, 1):
                    m[i][j] = m[i][j]/n[i]

            classes = [int(x) for x in n]
            n=[0.1]*k

            mdist = [0]*k

            for p in range(0, k, 1):
                for j in range(0, cols, 1):
                    mdist[p] += float((prev[p][j]-m[p][j])**2)

                mdist[p] = (mdist[p]) ** 0.5

            prev=m
            totaldist = 0
            for b in range(0, len(mdist), 1):
                totaldist += mdist[b]

            print ("distance:",totaldist)

        print("k =",k," | Clusters: ",classes)


    def process(self):
        return 0

    def means(self, data, k):
        return []

    def distance(self, x, k):
        sm = sum([(m - n)**2 for m, n in zip(x, k)])
        return math.sqrt(sm)

    def classify(self, data, w):
        
        return 0


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
    
    #print(km.initialize(data, int(k)))

    km.train(data, int(k))

