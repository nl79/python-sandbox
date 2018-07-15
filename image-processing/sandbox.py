import math
x = 8
y = 8
theta = 0
r = math.sqrt(x**2 + y**2)

phi = math.tan(x/y)
d = r * math.sin(theta - phi)
print("r: {} | phi: {} | d: {}".format(r, phi, d))


# X, Y coordinates of the 1s in the image
ones = [
    [0, 7],
    [1, 6],
    [2, 5],
    [3, 4],
    [4, 3],
    [5, 2],
    [6, 1],
    [7, 0]
]

for point in ones:
    x = point[0]
    y = point[1]
    print("--------({}, {})--------".format(x, y))
    #p = x_k * cos(theta) + y_k * sin(theta)
    for theta in range(-90, 100, 10):
        #i = theta
        p = x * math.cos(theta) + y * math.sin(theta)

        print("theta: {}".format(theta))
        print("p = {} * cos({}) + {} * sin({}) = {}".format(x, theta, y, theta, str(int(p))))
