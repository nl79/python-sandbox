from player import Player
from enemy import Enemy, Troll, Vampyre, VampyreKing

random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

ugly_troll = Troll("Pug")
ugly_troll.take_damage(20)
print("Ugly Troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another Troll - {}".format(another_troll))

brother_troll = Troll("Urg")
print("Brother - {}".format(brother_troll))

ugly_troll.grunt()
another_troll.grunt()
brother_troll.grunt()

vamp = Vampyre("Vlad")
vamp.take_damage(7)
print(vamp)

king = VampyreKing("Dracula")


while vamp._alive:
    vamp.take_damage(1)
    king.take_damage(10)
    print(king)