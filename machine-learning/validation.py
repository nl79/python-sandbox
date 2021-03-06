from sklearn.svm import LinearSVC
import random
import sys

class CrossValidate(object):
  def __init__(self, X, y):
    return None

  def split(self, X, Y, t=.9):
    ids = []

    for i in range(0, len(X)):
      ids.append(i)

    newX = []
    newY = []
    xPrime = []
    yPrime = []

    random.shuffle(ids)

    cutoff = int(.9 * len(ids))

    for i in range(0, cutoff):
      newX.append(X[ids[i]])
      newY.append(Y[ids[i]])

    for i in range(cutoff, len(ids)):
      xPrime.append(X[ids[i]])
      yPrime.append(Y[ids[i]])

    return newX, newY, xPrime, yPrime

  def error(self, p, y):
    err = 0
    for i in range(0, len(p)):
      if(p[i] != y[i]):
        err += 1

    err = err/len(y)
    return err

  def getC(self, X, y, s = 1):
    random.seed()
    C = [.001, .01, .1, 1, 10, 100]
    error = {}

    for i in range(0, len(C)):
      error[C[i]] = 0

    ids = []

    for i in range(0, len(X)):
      ids.append(i)

    splits = s

    for x in range(0, splits):
      
      newX, newY, xPrime, yPrime = self.split(X, y)

      for i in range(0, len(C)):
        c = C[i]
        clf = LinearSVC(C=c)
        clf.fit(newX, newY)
        prediction = clf.predict(xPrime)

        error[c] += self.error(prediction, yPrime)

    bestC = 0
    errorMin = float("inf")

    for key in error:
        error[key] = error[key]/splits
        if(error[key] < errorMin):
            errorMin = error[key]
            bestC = key
 
    #print("Errors: ", error)
    #print("Min Error: {} | Best C: {}".format(errorMin, bestC))
    return {"C": bestC, "e": errorMin}

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
    
    else:
         # read labelfile
        print('Reading Labels...')
        y = readLabels(labelfile)

        print('Splitting Data...')
        X, y, t, tRowNum = splitData(X, y)
    
    cv = CrossValidate(X, y)

    print(cv.getC(X, y))

