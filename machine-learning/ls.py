import sys
import math
import random

#python3 ls.py ./breast_cancer/breast_cancer.data ./breast_cancer/breast_cancer.trainlabels.6
#python3 ls.py ./breast_cancer/breast_cancer.data ./breast_cancer/breast_cancer.trainlabels.6

class LeastSquares(object):

    def __init__(self, data, labels):
        self._data = data
        self._labels = labels

    def process(self):
        return self.descent(self._data, self._labels)

    def cost(self, w, data, label):
        error = 0
        for i in data:
            error += (self.dot(w, data[i]) - labels.get(i)) ** 2
        return error

    def descent(self, data, labels, eta = .001, stop = 0.001, max=20000):
        val = 1.0/len(data.get(0))
        count = 0

        w = [val for i in range(0, len(data[0]))]

        j = self.cost(w, data, labels)

        converged = False

        while not converged:
            dellf = [0 for i in range(0, len(data[0]))]

            # compute dellf
            for i in data:

                #get the dot product of w with the row.
                dp = self.dot(w, data[i])

                for j in range(0, len(data[i]), 1):
                    # calculate deffF
                    dellf[j] += (dp - labels.get(i)) * data[i][j]

            #update w
            for i in range(0, len(data[0]), 1):
                w[i] = w[i] - eta * dellf[i]

            #compute error
            error = self.cost(w, data, labels)

            #compare new error to previous iretaion
            if( abs(j - error) <= stop):
                converged = True

            j = error

            count += 1
            if(count == max):
                converged = True

        return w[:2]


    def dot(self, m1, m2):
        res = 0
        for i in range(0, len(m1), 1):
            res += m1[i] * m2[i]

        return res

    def distance(self, w):
        normw = 0
        for i in range(0, len(w), 1):
            normw += w[i] ** 2

        normw = math.sqrt(normw)

        # distance to d_origin
        d_origin = abs(w[len(w) - 1] / normw)

        return d_origin

    def classify(self, data):
        w = self._w;
        labels = {};

        for i in data:
            dp = self.dot(w, data[i])
            c = "1" if dp > 0 else "0"
            labels[i] = c
            print("{} {}".format(c, str(i)))
        return labels


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

        labels[int(a[1])] = -1 if int(a[0]) == 0 else int(a[0])
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
            d.append(1)
            test.setdefault(i, d)
        else:
            d = data[i]
            d.append(1)
            training.setdefault(i, d)

    return {"training": training, "test": test}


if __name__ == "__main__":

    print('here')
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

    w = ls.process()
    distance = ls.distance(w)
    print(w)
    print("Distance to origin: " + str(distance))


    #classify
    #classification = ls.classify(testdata)

    # Classify
    #classes = classify(testdata, labels, means)
