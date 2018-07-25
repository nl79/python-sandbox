
X = [
    [1, 0, 0, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 1]
]

y = [0, 0, 1, 1]

w = [0, 0, 0, 0]

C = 1

done = False

def dot(x, w):
    res = 0
    for i in range(0, len(x), 1):
        res += x[i] * w[i]
    return res

while done == False:

    for i in range(0, len(X)):
        #data row
        x = X[i]

        #class for the row
        c = y[i]

        #calculate the dot product
        prod = dot(x, w)
        print(i+1, w, "*",  x, "=", prod )
        
        #print("wTx: {}".format(prod))

        if(c == 0 and prod <= 0):
            #print("C: {}".format(0))
            for j in range(0, len(x)):
                w[j] += C * x[j]
        
        elif(c == 1 and prod >= 0):
            #print("C: {}".format(1))

            for j in range(0, len(x)):
                w[j] -= C * x[j]
            
        print("Updated W: ", w)
    
    # Check if the current W matrix has any errors
    #print("Validating")
    done = True
    for i in range(0, len(X)):
         #data row
        x = X[i]

        #class for the row
        c = y[i]

        prod = dot(x, w)
        #print("wTx: {}".format(prod))
        #print("Y: {}".format(c))

        if(prod > 0 and c == 0):
            continue
        elif(prod < 0 and c ==1):
            continue
        else:
            done = False
            break