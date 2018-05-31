import sys


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
        c = str(labels.get(i))

        # If class exists, sum up the data values for that row and that class.
        if c != None:
            current = means.get(c)
            for j in range(0, cols, 1):
                current[j] += data[i][j]

    # Calculate the means.
    for j in range(0, cols, 1):
        for c in classes:
            means[c][j] = means[c][j] / classes[c]

    return means


def classify(data, labels):

    rows = len(data)
    cols = len(data[0])

    classes = labels.get('classes')
    labels = labels.get('labels')

    ### Classify unlableed points
    for i in range(0, rows, 1):
        if(labels.get(i) == None):
            d0 = 0
            d1 = 0
            for j in range(0, cols, 1):
                d0 = d0 + ( m0[j] - data[i][j])**2
                d1 = d1 + ( m1[j] - data[i][j])**2

            if(d0 < d1):
                print('0 ', i)
            else:
                print('1 ', i)


if __name__ == "__main__":
    #validate parameters
    print('arvs', sys.argv);

    if len(sys.argv) < 3:
        exit()

    datafile = sys.argv[1]
    labelfile = sys.argv[2]

    #read datafile
    data = readData(datafile)

    #read labelfile
    labels = readLabels(labelfile)
    # counts = labels.get('counts')
    # labels = labels.get('labels')

    #compute means
    means = computeMeans(data,labels)
    print('means', means)

    #print('label.classes', labels.get('classes'))
    #print('means', means)
    print('here');
