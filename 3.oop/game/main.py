from player import Player

tim = Player("Time")

print(tim.name)
print(tim.lives)
tim.lives -= 1
print(tim.lives)
tim.lives -= 1
print(tim.lives)
tim.lives -= 1
print(tim.lives)
tim.lives -= 1
print(tim.lives)

tim.level = 2
print(tim)

tim.level += 5
print(tim)

tim.score = 500
print(tim)