import sys
import math
import random
from sklearn.svm import LinearSVC

# python3 dimensionality-reduction.py data/SNP/traindata data/SNP/truelabels.txt data/SNP/testdata
# python3 dimensionality-reduction.py ionosphere/ionosphere.data ionosphere/ionosphere.trainlabels.0

class ChiSVM(object):

    def __init__(self, data, labels):
        self._data = data
        self._labels = labels


    # Generate a new DAta Set using only the features in the list
    def reduce(self, data, features):
        X = []
        for i in range(0, len(data)):
            row = []
            for f in features:
                row.append(data[i][f])
            X.append(row)

        return X


    def chiSqr(self, X, y, k):
        cols = len(X[0])

        F = {}

        for j in range(0, cols):
            
          # Contingency table for the distribution
          crosstab = [[1, 1], [1, 1], [1, 1]]

          for i in range(0, len(X)):
            
            #Extract the label for the Vector
            label = int(y[i])

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

          F.setdefault(j, sum(sqrSum))
                
        fields = sorted(F, key=F.__getitem__, reverse=True)
        
        return fields[:k]


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
def readLabels(filename, flat=False):

    file = open(labelfile)


    labels = {} if flat == False else []

    line = file.readline()

    while(line != ''):
        a = line.split()

        if( flat == False):
            labels[int(a[1])] = int(a[0])
        else:
            labels.append(int(a[0]))

        line = file.readline()

    file.close()

    return labels


# Splits the input data into the classified(training data) and
# unclassified (test data)
def splitData(data, labels):

    # Labels
    y = []

    # Training data
    X = []

    # Test data
    t = []

    # Numerical position of the training data if in the single dataset is given.
    tRowNum = []

    for i in range(0, len(data), 1):

        label = labels.get(i)
        if(label == None):
            t.append(data[i])
            tRowNum.append(i)

        else:
            y.append(label)
            X.append(data[i])

    return X, y, t, tRowNum
    #return {"training": training, "test": test, "X": X, "y": y, "t": t}


if __name__ == "__main__":
    # validate parameters
    if len(sys.argv) < 3:
        exit()

    datafile = sys.argv[1]
    labelfile = sys.argv[2]

    traindata = []
    testdata = []

    # read datafile
    print('Reading Data...')
    X = readData(datafile)

    # If no unclassified data is supplied, try to extract it from the initial
    # data input
    if len(sys.argv) >= 4:
         # read labelfile
        print('Reading Labels...')
        y = readLabels(labelfile, flat=True)

        print('Reading Test Data...')
        t = readData(sys.argv[3])
    
        # Row numbers of the training data.
        # this is mostly so that there is no exception when attemption to access it
        # when printing the prediction values.
        tRowNum = list(range(0, len(t)))
    else:
         # read labelfile
        print('Reading Labels...')
        y = readLabels(labelfile)

        print('Splitting Data...')
        X, y, t, tRowNum = splitData(X, y)

    csvm = ChiSVM(X, y)

    print(len(X))
    print(len(y))

    print('Calculating ChiSqr...')
    features = csvm.chiSqr(X, y, 15)

    print('Features:')
    print(features)
    
    X = csvm.reduce(X, features)
    print("Reduced X")
  
    clf = LinearSVC(random_state=0)

    print("Fitting...")
    clf.fit(X, y)
    
    # Reduce the training data to the subset based on the feature list.
    tX = csvm.reduce(t, features)

    print("Predicting...")
    predictions = clf.predict(tX)
    
    # print(predictions)
    # print(tRowNum)

    for i in range(0, len(predictions)):
        print("{} {}".format(predictions[i], tRowNum[i]))