import sys
import math
import random

# python3 k-means.py ionosphere/ionosphere.data ionosphere/ionosphere.trainlabels.0

class K_Means(object):

    def __init__(self, data, k):
        self._data = data

    def initialize(self, data, k):
        col = []
        m = []
        
        for i in range(0, len(data[0])):
            col.append(0)

        for j in range(0, k):
            m.append(col)

        rand = 0

        for p in range(0, k):
            rand=random.randrange(0, (len(data)-1))
            m[p] = data[rand]
        
        return col, m

        
    def process(self):
        return 0

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
    
    print(km.initialize(data, int(k)))
