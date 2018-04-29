# a = 12
# b = 4
# print( a + b)
# print(a.__add__(b))

class Kettle(object):

    # almost "static" property
    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price);

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)
print(hamilton.switch_on())
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

print("*" * 80)

kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power)

print("Swith to atomic power")
Kettle.power_source = "Atomic"
print(Kettle.power_source)

print("Switch kenwood to gas")
kenwood.power_source = "GAS"
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)