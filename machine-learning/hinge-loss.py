import sys
import math
import random

#python3 hinge-loss.py ionosphere/ionosphere.data ionosphere/ionosphere.trainlabels.0

class HingeLoss(object):

    def __init__(self, data, labels):
        self._data = data
        self._labels = labels

    def process(self, eta=.0001, stop = .000000001, max=float("inf")):
        return self.descent(self._data, self._labels, eta, stop, max)

    def cost(self, w, data, label):
        error = 0
        for i in data:
            error += (self.dot(w, data[i]) - labels.get(i)) ** 2
        return error

    def loss(self, w, data, label):
        loss = 0
        for i in data:
            loss += max(0, 1 - (label.get(i) * self.dot(w, data[i])))

        return loss

    def descent(self, data, labels, eta = .001, stop = .000000001, max=float("inf")):

        cols = len(data.get(list(data.keys())[0]))
        count = 0

        w = [0.02 * random.random() - 0.01]*cols

        J = self.loss(w, data, labels)

        converged = False

        while not converged:
            dellf = [0] * cols

            # compute dellf
            for i in data:

                # calculate the condition.
                c = labels.get(i) * self.dot(w, data[i])

                for j in range(0, len(data[i]), 1):

                    if(c < 1):
                        # calculate deffF
                        dellf[j] += -1 * (labels.get(i) * data[i][j])

                    else:
                        dellf[j] += 0


            #update w
            for i in range(0, cols, 1):
                w[i] = w[i] - eta * dellf[i]

            #compute loss
            loss = self.loss(w, data, labels)

            #compare new error to previous iretaion
            #print("loss: {}".format(loss))
            if( abs(J - loss) <= stop):
                converged = True

            J = loss

            count += 1
            #print(count)
            if(count == max):
                converged = True
        return w


    def distance(self, w):
        n = 0
        for i in range(0, (len(w) -1), 1):
            n += w[i] ** 2
        n = math.sqrt(n)

        return abs(w[len(w) - 1] / n)

    def dot(self, m1, m2):
        res = 0
        for i in range(0, len(m1), 1):
            res += m1[i] * m2[i]

        return res

    def classify(self, data, w):
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
    #validate parameters
    if len(sys.argv) < 3:
        exit()

    datafile = sys.argv[1]
    labelfile = sys.argv[2]

    traindata = []
    testdata = []

    # Change ETA here
    eta = .0001

    # Stop condition
    stop = .000000001

    # Max iterations
    maximum = 2000

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


    ls = HingeLoss(traindata, labels)
    w = ls.process(eta, stop, maximum)
    distance = ls.distance(w)
    # print(w[:-1])
    # print ("Distance to origin = " + str(distance))
    #classify
    classification = ls.classify(testdata, w)

    # Classify
    #classes = classify(testdata, labels, means)
