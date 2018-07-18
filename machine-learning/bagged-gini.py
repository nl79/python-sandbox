import sys
import math
import random

# python3 bagged-gini.py ionosphere/ionosphere.data ionosphere/ionosphere.trainlabels.0
# perl test_error.pl bagged-gini ionosphere

class Bag(object):

    def __init__(self, data, labels):
        self._data = data
        self._labels = labels

    def shuffle(self):
        n = len(self._data)

        data = {}
        labels = {}
        oKeys = []

        keys = list(self._data.keys())

        for i in range(0, n):

            key = keys[random.randint(0, n-1)]

            data.setdefault(i, self._data.get(key))
            labels.setdefault(i, self._labels.get(key))

            # for debugging Original Keys
            oKeys.append(key)

        return {'X': data, 'y': labels, 'keys': oKeys}

    def aggregate(self, data):
      result = []
      if(len(data) == 1):
        return result

      totals = {}

      for i in range(0, len(data)):
        for key in data[i]:
          val = int(data[i][key])
          if(key in totals):
            totals[key].append(val)
          else:
            totals.setdefault(key,[val])
      
      for key in totals:
        total = sum(totals[key])
        c = ''
        if(total >= math.floor(len(totals[key])/2)):
          c = 1
        else:
          c = 0
      
        print("{} {}".format(str(c), str(key)))
        result.append((key, c))

      return result


class DecisionTree(object):

    def __init__(self, data, labels):
        self._data = data
        self._labels = labels

    def gini(self, cols, split, rows):

        # left split size
        lsize = split

        # right split size
        rsize = len(cols) - lsize

        # left proportion
        lp = 0

        # right proportion
        rp = 0

        for i in range(0, split):
            if(cols[i][1] == 0):
                lp += 1

        for j in range(split, len(cols)):
            if(cols[j][1] == 0):
                rp += 1

        #gini = (lsize/rows)*(lp/lsize)*(1 - lp/lsize) + (rsize/rows)*(rp/rsize)*(1 - rp/rsize);

        # where lsize is the size of the left partition, lp is the
        # proportion of -1 labels in the left partition, rsize is the
        # size of the right partition, rp is the proportion of -1
        # labels in the right partition, and rows is the total number of
        # datapoints in the dataset d (passed to the function)

        gini = (lsize/rows)*(lp/lsize)*(1 - lp/lsize) + \
            (rsize/rows)*(rp/rsize)*(1 - rp/rsize)
        #print("({}/{})*({}/{})*(1 - {}/{}) + ({}/{})*({}/{})*(1 - {}/{})".format(lsize, rows, lp, lsize,lp,lsize,rsize,rows,rp,rsize,rp,rsize))
        return gini

    def threshold(self, data, split):

        # Valiate the split is not at the beginning or end of the data array.
        a = data[split-1][0]
        b = data[split][0]

        return (a + b) / 2

    def extractColumnData(self, i, data, label):
        col = []
        for key in data:
            col.append((data[key][i], label.get(key)))

        return sorted(col, key=lambda x: x[0])

    def process(self):
        return self.run(self._data, self._labels)

    def run(self, data, label):

        min = float("inf")
        split = 0
        feature = 0

        temp = None

        rows = len(data)
        cols = len(data.get(list(data.keys())[0]))

        for j in range(0, cols, 1):
            cData = self.extractColumnData(j, data, label)

            # split the data and get the Gini score
            for i in range(1, len(cData)):
                score = self.gini(cData, i, rows)

                if(score < min):
                    min = score
                    feature = j
                    split = i
                    temp = cData

        threshold = self.threshold(temp, split)

        return {"k": feature, "s": threshold}

    def classify(self, data, params):
        k = params['k']
        s = params['s']

        o = {}

        key = sorted(data.keys())
        for i in key:
            row = data[i]
            val = row[k]

            c = "1" if val < s else "0"

            o.setdefault(i, c)

        return o

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
    # validate parameters
    if len(sys.argv) < 3:
        exit()

    # Number of bags to create
    bags = 20

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

    results = []
    # Create the bagging object.
    bag = Bag(traindata, labels)

    for i in range(0, bags):

        # Crete a random data set with labels.
        model = bag.shuffle()

        # print(sorted(model['keys']))

        # process the model and store the labels.
        dt = DecisionTree(model['X'], model['y'])
        params = dt.process()
        classification = dt.classify(testdata, params)
        results.append(classification)
        # print(params)
        # print(classification)
        # print("Feature: {} | Split: {}".format(params["k"], params["s"]))

# Pick the most common labels out of all of the models.
classification = bag.aggregate(results)