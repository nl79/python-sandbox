# for i in range(1, 20):
#     print("I is now {}", format(i))

# number = '9,223,3723,234,223,5235'
# cleanedNumber = ''
# for i in range(0, len(number)):
#     print(number[i])

# for i in range(0, len(number)):
#     if( number[i] in '0123456789'):
#         cleanedNumber = cleanedNumber + number[i]
#         #print(number[i], end='')
#
# newNumber = int(cleanedNumber)
# print("The number is {}".format(cleanedNumber))

# for char in number:
#     if char in '0123456789':
#         cleanedNumber = cleanedNumber + char
#
# newNumber = int(cleanedNumber)
# print("The number is {}".format(newNumber))
#
# for state in ["not pining", "no more", 'a stiff', 'bereft or life']:
#     print('This parrot is ' + state)
#
# for i in range(0, 100, 5):
#     print('i {}'.format(i))
#
# for i in range(1,13):
#     for j in range(1,13):
#         print('{1} time {0} is {2}'.format(i, j, i*j), end='\t')
#     print('')
#
# shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']
# for item in shopping_list:
#     if item == 'spam':
#         print('I am ignoring item ' + item)
#         #continue
#         break
#     print("Buy " + item)
#

# meal = ['egg', 'bacon', 'spam', 'sausage']
# nasty_food_item = ''
#
# #Else for a 'for' loop will be executed if the 'break' is NOT executed.
# # the else will execute if the loop runs to completion.
# for item in meal:
#     if item == 'spam':
#         nasty_food_item = item
#         break
# else:
#     print("I'll have a plate of that, then, please")
#
# if nasty_food_item == 'spam':
#     print("Can't I have anything with out spam in it")


# i = 0
# while i < 10:
#     print('i is now {}'.format(i))
#     i += 1
#
# avaiable_exits = ['east', 'north east', 'south']
# chosen_exit = ''
# while chosen_exit not in avaiable_exits:
#     chosen_exit = input('Please choo a direction')
#     if chosen_exit == 'quit':
#         print('Game over')
#         break
# else:
#     print('arent you glad you got out of there!')

import random
highest = 10
answer = random.randint(1, highest)

print('Please guess a number between 1 and {}: '.format(highest))

# guess = int(input())
# if guess != answer:
#     if guess < answer:
#         print('Please guess higher')
#     else:
#         print('Please guess lower')
#     guess = int(input())
#     if guess == answer:
#         print('Well done, you guessed it')
#     else:
#         print('sorry, you have no guessed correctly')
# else:
#     print('You got it first time')
#


