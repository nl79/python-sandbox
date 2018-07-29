import sys
import math
import random
from sklearn.svm import LinearSVC
from validation import CrossValidate
import numpy as np

#python3 random-hp.py breast_cancer/breast_cancer.data  breast_cancer/breast_cancer.labels breast_cancer/breast_cancer.trainlabels.0

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
          #print("before: z[j]: {} ".format(z[j]))
          #print('w0: {}'.format(w0))
         
          res = self.sign(z[j] + w0)
          
          z[j] = res
          #print("res: {}".format(z[j]))
          #print("after: z[j]: {}".format(z[j]))
       
        '''
        Append (1+sign(zi))/2 as new column to the right end of Z
        '''
        for j in range(0, len(Z)):
          Z[j].insert(0, z[j])
          #Z[j].append(z[j])

        '''
        d. Project test data X' (each row is datapoint xj) onto w. 
        Let projection vector z'i be X'w. Append z'i as new column to the right end 
        of Z'.
        '''
        z = []
        for j in range(0, len(y)):
          z.append(self.dot(y[j], W))

        for j in range(0, len(z)):
          #z[j] = (1 + self.sign(z[j] + w0))/2
          res = self.sign(z[j] + w0)
          
          z[j] = res

        for j in range(0, len(zPrime)):
          zPrime[j].insert(0, z[j])
          #zPrime[j].append(z[j])
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
def readLabels(filename, flat=False):

    file = open(filename)


    labels = {} if flat == False else []

    line = file.readline()

    while(line != ''):
        a = line.split()

        l = int(a[0])

        if( flat == False):
            labels[int(a[1])] = l
        else:
            labels.append(l)

        line = file.readline()

    file.close()

    return labels


# unclassified (test data)
def splitData(data, labels):

    # Labels
    y = []

    # Training data
    X = []

    # Test data
    t = []

    for i in range(0, len(data), 1):

        label = labels.get(i)

        if(label == None):
            t.append(data[i])

        else:
            y.append(label)
            X.append(data[i])

    return X, y, t


def run(X, t, y, Y, C=None):
  cv = CrossValidate(X, y)

  # get the C value for the raw data.
  c = C if C != None else cv.getC(X, y, s=5)
 
  clf = LinearSVC(C=c)
  clf.fit(X, y)
  prediction = clf.predict(t)

  #Calculate the Error
  error = 0

  for i in range(0, len(prediction)):
    if(prediction[i] != Y[i]):
      error += 1

  error = error/float(len(Y))
  return error


if __name__ == "__main__":
    # validate parameters
    if len(sys.argv) < 3:
        exit()

    datafile = sys.argv[1]
    testlabel = sys.argv[2]
    trainlabel = sys.argv[3]
    
    traindata = []
    testdata = []

    # read datafile
    print('Reading Data...')
    X = readData(datafile)

    # read labelfile
    print('Reading Train Labels...')
    y = readLabels(trainlabel)

    print('Reading Test Labels...')
    Y = readLabels(testlabel, flat=True)

    print('Splitting Data...')
    X, y, t = splitData(X, y)

    hp = RandomHP()
    Z, zPrime = hp.generate(X, t, 10000)

    print("Original Data Error: ", run(X, t, y, Y))
    print("Modified Data Error: ", run(Z, zPrime, y, Y))