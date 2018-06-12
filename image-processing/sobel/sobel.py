# ref: https://blog.saush.com/2011/04/20/edge-detection-with-the-sobel-operator-in-ruby/
import sys
import math

class Sobel(object):

    def __init__(self, data):
        self.kernelX = [
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]
        ]

        self.kernelY = [
            [-1, -2, -1],
            [0, 0, 0],
            [1, 2, 1]
        ]

        self.data = self.pad(data)
        self.Gx = self.matrix()
        self.Gy = self.matrix()
        self.output = self.matrix()

        self.process()


    def matrix(self):
        d = self.data
        n = len(d);
        m = len(d[0]);
        return [[0]*m]*n

    def pad(self, d):
        n = len(d);
        m = len(d[0]);

        for i in range(0, len(d), 1):
            d[i].insert(0, 0)
            d[i].append(0)

        d.insert(0, [0]*(m+1))
        d.append([0]*(m+1));

        return d

    def process(self):
        d = self.data
        Kx = self.kernelX
        Ky = self.kernelY
        Gx = self.Gx
        Gy = self.Gy
        o = self.output

        for x in range(1, len(d)-2, 1):
            for y in range(1, len(d[x])-2, 1):

                # calculate each pixel
                Px =((Kx[0][0] * d[x-1][y-1])
                + (Kx[0][1] * d[x][y-1])
                + (Kx[0][2] * d[x+1][y-1]))
                + ((Kx[1][0] * d[x-1][y])
                + (Kx[1][1] * d[x][y])
                + (Kx[1][2] * d[x+1][y]))
                + ((Kx[2][0] * d[x-1][y+1])
                + (Kx[2][1] * d[x][y+1])
                + (Kx[2][2] * d[x+1][y+1]))

                Py =((Ky[0][0] * d[x-1][y-1])
                + (Ky[0][1] * d[x][y-1])
                + (Ky[0][2] * d[x+1][y-1]))
                + ((Ky[1][0] * d[x-1][y])
                + (Ky[1][1] * d[x][y])
                + (Ky[1][2] * d[x+1][y]))
                + ((Ky[2][0] * d[x-1][y+1])
                + (Ky[2][1] * d[x][y+1])
                + (Ky[2][2] * d[x+1][y+1]))

                #store each calculated pixel in Gx mapsself.
                Gx[x][y] = Px
                Gy[x][y] = Py

                o[x][y] = math.ceil(math.sqrt(Px**2 + Py**2))

        self.output = o

    def getGx(self):
        return self.Gx

    def getGy(self):
        return self.Gy

    def getResult(self):
        return self.output


if __name__ == "__main__":
    matrix = [
        [1,1,1,1,0,0,1,0],
        [1,1,0,1,1,1,1,1],
        [1,2,8,8,8,9,1,0],
        [0,1,8,9,9,9,1,0],
        [0,1,8,8,9,8,1,0],
        [1,1,8,9,9,8,1,1],
        [0,1,1,1,1,1,0,0],
        [1,0,0,0,0,0,0,0]
    ]



    sobel = Sobel(matrix);

    #print(sobel.pad(matrix))

    print(sobel.getGx())
    print(sobel.getGy())
    print(sobel.getResult())
