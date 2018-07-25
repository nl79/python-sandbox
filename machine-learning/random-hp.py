import sys
import math
import random
import numpy as np
from sklearn import svm


# python3 bagged-gini.py ionosphere/ionosphere.data ionosphere/ionosphere.trainlabels.0
# perl test_error.pl bagged-gini ionosphere


class RandomHP(object):

    def __init__(self):
      return

    def dot(self, m1, m2):
      res = 0
      for i in range(0, len(m1), 1):
          res += m1[i] * m2[i]

      return res

    def generate(self, X, y, k):
     
      # Initialize The Sets
      Z = []
      for j in range(0, len(X)):
        Z.append([0])
    
      zPrime = []
      for j in range(0, len(y)):
        zPrime.append([0])
    
      for i in range(0, k):

        '''
        a. Create random vector w where each wj is uniformly sampled between -1 and 1.
        '''
        W = []
        for j in range(0, len(X[0])):
          W.append(random.uniform(-1, 1))

        '''
        b. Let xj be our training data points. Determine the largest and smallest wTxj
        across all xj. Select w0 randomly between [smallest wTxj, largest wTxj].
        '''
        z = []
        for j in range(0, len(X)):
          z.append(self.dot(X[j], W))
        
        valMin = float("inf")
        valMax = float("-inf")

        for j in range(0, len(z)):
          if(z[j] < valMin):
            valMin = z[j]
          
          if(z[j] > valMax):
            valMax = z[j]
        w0 = random.uniform(valMin, valMax)


        '''
        c. Project training data X (each row is datapoint xj) onto w. 
        Let projection vector zi be Xw + w0 (here X has dimensions n by m and w is m by 1).
        Append (1+sign(zi))/2 as new column to the right end of Z. Remember that zi is
        a vector and so (1+sign(zi))/2 is 0 if the sign is -1 and 1 otherwise.
        '''
        for j in range(0, len(z)):
          z[j] = self.sign(z[j] + w0)
       
        '''
        Append (1+sign(zi))/2 as new column to the right end of Z
        '''
        for j in range(0, len(Z)):
          Z[j].insert(0, z[j])

        '''
        d. Project test data X' (each row is datapoint xj) onto w. 
        Let projection vector z'i be X'w. Append z'i as new column to the right end 
        of Z'.
        '''
        z = []
        for j in range(0, len(y)):
          z.append(self.dot(y[j], W))

        for j in range(0, len(z)):
          z[j] = self.sign(z[j] + w0)

        for j in range(0, len(zPrime)):
          zPrime[j].insert(0, z[j])

      return [Z, zPrime]

    def sign(self, x):
      if( x <= 0):
        return -1
      else:
        return +1

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


# Read Label
def readLabels(filename):

    file = open(labelfile)

    labels = {}
    line = file.readline()
    while(line != ''):
        a = line.split()
        labels[int(a[1])] = int(a[0])
        line = file.readline()

    file.close()

    return labels


# Splits the input data into the classified(training data) and
# unclassified (test data)
def splitData(data, labels):

    training = []
    test = []

    for i in range(0, len(data), 1):

        if(labels.get(i) == None):
            test.append(data[i])
        else:
            training.append(data[i])

    return {"training": training, "test": test}


if __name__ == "__main__":
    # validate parameters
    if len(sys.argv) < 3:
        exit()


    datafile = sys.argv[1]
    labelfile = sys.argv[2]

    traindata = []
    testdata = []

    # read datafile
    data = readData(datafile)

    # read labelfile
    labels = readLabels(labelfile)

    # If no unclassified data is supplied, try to extract it from the initial
    # data input
    if len(sys.argv) >= 4:
        testfile = sys.argv[3]
        testdata = readData(testfile)
        traindata = data
    else:
        data = splitData(data, labels)
        testdata = data.get("test")
        traindata = data.get("training")

    hp = RandomHP()
    Z, zPrime = hp.generate(traindata, testdata, 2)

  
    for i in range(0, len(Z)):
      print(Z[i])
    print('*'*10)
    for i in range(0, len(zPrime)):
      print(zPrime[i])

