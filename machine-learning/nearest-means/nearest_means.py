import sys
#python3 nearest_means.py ../data/breast_cancer/breast_cancer.data ../data/breast_cancer/breast_cancer.trainlabels.6

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
    classes = {}
    n = [0,0]

    line = file.readline()

    while(line != ''):
        a = line.split()
        labels[int(a[1])] = int(a[0])
        line = file.readline()

        #Check if the class key exists, if not add it, if yes increment countself.
        if a[0] in classes:
            classes[a[0]] += 1
        else:
            classes.setdefault(a[0], 1)

        n[int(a[0])] += 1

    file.close()

    return {"labels": labels, "counts": n, "classes": classes}

def computeMeans(data, labels):

    rows = len(data)
    cols = len(data[0])

    classes = labels.get('classes')
    labels = labels.get('labels')

    ### Compute means
    # build the means dict and initialize the class list of attribute vaues to 0
    means = {}
    for key in classes:
        means.setdefault(str(key), [0]*cols)

    for i in range(0, rows, 1):

        # get the row class value
        c = labels.get(i)

        # If class exists, sum up the data values for that row and that class.
        if c != None:
            current = means.get(str(c))
            for j in range(0, cols, 1):
                current[j] += data[i][j]

    # Calculate the means.
    for j in range(0, cols, 1):
        for c in classes:
            means[c][j] = means[c][j] / classes[c]

    return means


def classify(data, labels, means):
    rows = len(data)
    if rows == 0:
        return False

    cols = len(data[0])
    classes = labels.get('classes')
    labels = labels.get('labels')

    # Iterate over every row
    for i in range(0, rows, 1):

        # Initialize the deviation collection
        # Zero out the deviation values for each row.
        d = {}
        for key in classes:
            d.setdefault(key, 0)

        # Iterate over every column
        for j in range(0, cols, 1):
            for key in classes:
                d[key] += (means.get(key)[j] - data[i][j])**2

            # Calculate the max
            max = 0
            c = None
            for key in d:
                if d[key] > max:
                    max = d[key]
                    c = key

            print('{} {}'.format(c, i))

    return False


# Splits the input data into the classified(training data) and
# unclassified (test data)
def splitData(data, labels):

    training = []
    test = []
    labels = labels.get('labels')

    for i in range(0, len(data), 1):

        if(labels.get(i) == None):
            test.append(data[i])
        else:
            training.append(data[i])

    return {"training": training, "test": test}


if __name__ == "__main__":
    #validate parameters
    print('arvs', sys.argv);

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

    #compute means
    means = computeMeans(traindata,labels)

    # Classify
    classes = classify(testdata, labels, means)
