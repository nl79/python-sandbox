import sys
import math

#python3 naive_bayes.py ../data/breast_cancer/breast_cancer.data ../data/breast_cancer/breast_cancer.trainlabels.6


class LeastSquares(object):

    def __init__(self, data, labels):
        self._data = data
        self._labels = labels
        self._rows = len(data)
        self._cols = len(data[0])
        self._classes = self.aggregateClasses()
        self._means = self.means()

    def aggregateClasses(self):
        labels = self._labels

        a = {};
        for key in labels:
            l = str(labels[key])
            if l in a:
                a[l] += 1
            else:
                a[l] = 1
        return a

    def innerProduct():
        return 0

    def classify(self, data):

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

    training = []
    test = {}

    for i in range(0, len(data), 1):

        if(labels.get(i) == None):
            test.setdefault(i, data[i])
        else:
            training.append(data[i])

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


    ls = LeastSquares(traindata, labels)

    #classify
    classification = ls.classify(testdata)

    # Classify
    #classes = classify(testdata, labels, means)
