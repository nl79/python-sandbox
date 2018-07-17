import sys
import math
import random
from sklearn.svm import LinearSVC

# python3 dimensionality-reduction.py data/SNP/testdata data/SNP/truelabels.txt data/SNP/traindata
# python3 dimensionality-reduction.py data/SNP/testdata data/SNP/truelabels.txt data/SNP/traindata


class ChiSVM(object):

    def __init__(self, data, labels):
        self._data = data
        self._labels = labels

    def chiSqr(self, X, y, k):
        cols = len(X[0])

        T = []

        F = {}

        for j in range(0, cols):
            
          # Contingency table for the distribution
          crosstab = [[1, 1], [1, 1], [1, 1]]

          for i in X:
            
            #Extract the label for the Vector
            label = int(y.get(i))

            if label == 0:

                if X[i][j] == 0:
                    crosstab[0][0] += 1
                elif X[i][j] == 1:
                    crosstab[1][0] += 1
                elif X[i][j] == 2:
                    crosstab[2][0] += 1

            elif label == 1:

                if X[i][j] == 0:
                    crosstab[0][1] += 1
                elif X[i][j] == 1:
                    crosstab[1][1] += 1
                elif X[i][j] == 2:
                    crosstab[2][1] += 1

          # Sum up the columns values
          cTotals = []
          for key in crosstab:
            cTotals.append(sum(key))
          
          # Sum up the row values.
          rTotals = []
          for key in zip(*crosstab):
            rTotals.append(sum(key))
          
          total = sum(cTotals)

          # Calculate the expected value.
          exp = []
          for c in cTotals:
            temp = []
            for r in rTotals:
              temp.append((r*c)/total)
            exp.append(temp)
          
          sqr = []
          for e in range(0, len(exp)):
            col = []
            for c in range(0, len(exp[e])):
              col.append(((crosstab[e][c] - exp[e][c])**2)/exp[e][c])
            sqr.append(col)
          
          sqrSum = []
          for x in zip(*sqr):
            sqrSum.append(sum(x))

          #T.append(sum(sqrSum))
          F.setdefault(j, sqrSum)
        
        #fields = sorted(range(len(T)), key=F.__getitem__, reverse=True)
        fields = sorted(F.iteritems(), key=lambda (k,v): (v,k))

        print(fields)
        return fields
        #return fields[:k]


# Read Data
def readData(filename):
    file = open(filename)
    data = []

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

    csvm = ChiSVM(traindata, labels)

    params = csvm.chiSqr(traindata, labels, 15)
    print(params)
    #classification = dt.classify(testdata, params)