import sys
import math
import random

#python3 gini.py ionosphere/ionosphere.data ionosphere/ionosphere.trainlabels.0

class DecisionTree(object):

    def __init__(self, data, labels):
        self._data = data
        self._labels = labels

    def gini(self, w, data, label):
        val = 0
        return val

    def getCounts(self, data):
      counts = {
        "p": 0,
        "n": 0
      }

      for key in data:
        l = label.get(key)
        if(l == 1):
          counts["p"] += 1
        else:
          counts["n"] += 1

      return counts

    def extractColumnData(self, i, data, label):
      col = []
      
      for key in data:
        col.append((data[key][i], label.get(key)))

      return sorted(col, key=lambda x: x[0])

    def process(self):
      return self.run(self._data, self._labels)

    def run(self, data, label):
      ginivals = []
      split = 0
      rows = len(data)
      cols = len(data.get(list(data.keys())[0]))

      for j in range(0, cols, 1):
        ginivals.append([0, 0])
      
      for j in range(0, cols, 1):
        col = self.extractColumnData(j, data, label)

        for i in range(1, len(col)-1):
            for j in range(0, i):
                #left split
            
            for k in range(i, len(col)):
                #right split

            
        

      
      return 0


#### Read Data
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


#### Read Label
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

    training = {}
    test = {}

    for i in range(0, len(data), 1):

        if(labels.get(i) == None):
            d = data[i]
            test.setdefault(i, d)
        else:
            d = data[i]
            training.setdefault(i, d)

    return {"training": training, "test": test}


if __name__ == "__main__":
    #validate parameters
    if len(sys.argv) < 3:
        exit()

    datafile = sys.argv[1]
    labelfile = sys.argv[2]

    traindata = []
    testdata = []

    #read datafile
    data = readData(datafile)

    #read labelfile
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


    dt = DecisionTree(traindata, labels)

    dt.process()

