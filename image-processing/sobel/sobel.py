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

        self.data = data
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

        for y in range(0, len(d)-2, 1):
            for x in range(0, len(d[y])-2, 1):
                Px = 0;
                Py = 0;
                #calculate each pixel
                for i in range(0, len(Kx), 1):
                    for j in range(0, len(Kx[i]), 1):
                        print('(Kx[i][j]', Kx[i][j])
                        print('d[y-1][x-1]', d[y+i][x+j])
                        print('(Kx[i][j] * d[y-1][x-1])', (Kx[i][j] * d[y+i][x+j]))
                        Px += (Kx[i][j] * d[y+i][x+j])
                        print(Px)
                # Px =(Kx[0][0] * d[y][x])
                # + (Kx[0][1] * d[y][x+1])
                # + (Kx[0][2] * d[y][x+2])
                #
                # + (Kx[1][0] * d[y+1][x])
                # + (Kx[1][1] * d[y+1][x+1])
                # + (Kx[1][2] * d[y+1][x+2])
                #
                # + (Kx[2][0] * d[y+2][x])
                # + (Kx[2][1] * d[y+2][x+1])
                # + (Kx[2][2] * d[y+2][x+2])

                #print(Px)

                # Py =((Ky[0][0] * d[y-1][x-1])
                # + (Ky[1][0] * d[y][x-1])
                # + (Ky[2][0] * d[y+1][x-1]))
                # + ((Ky[0][1] * d[y-1][x])
                # + (Ky[1][1] * d[y][x])
                # + (Ky[2][1] * d[y+1][x]))
                # + ((Ky[0][2] * d[y-1][x+1])
                # + (Ky[1][2] * d[y][x+1])
                # + (Ky[2][2] * d[y+1][x+1]))
                #
                # #store each calculated pixel in Gx mapsself.
                Gx[y][x] = Px
                # Gy[y-1][x-1] = Py
                #
                # o[x][y] = math.ceil(math.sqrt(Px**2 + Py**2))

        self.output = o

    def getGx(self):
        return self.Gx

    def getGy(self):
        return self.Gy

    def getResult(self):
        return self.output


def pretty(data):
    r = '';
    for row in range(0, len(data)-1, 1):
        for col in range(0, len(data[row])-1, 1):
            r += str(data[row][col]) + ','
        print(r)
        r = '';

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
    pretty(sobel.getGx())
    pretty(sobel.getGy())
    pretty(sobel.getResult())
