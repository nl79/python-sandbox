# ipAddress = input('Please enter an IP address')
# print(ipAddress.count('.'))

# parrot_list = ['non pinin', 'no more', 'a stiff', 'bareft of life']
# parrot_list.append('A norwegian blue')
#
# for state in parrot_list:
#     print('This parrot is {}'.format(state))
#
# even = [2,4,6,8]
# odd = [1,3,5,7,9]
#
# number = even + odd
# number.sort()
# print(number)
#
# #return a new object
# sortedNumbers = sorted(number)
# print(sortedNumbers)
#
# if number == sortedNumbers:
#     print('The lists are equal')
# else:
#     print('The list are not equal')

#
# list_1 = []
# list_2 = list()
#
# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
# if(list_1 == list_2):
#     print('Lists are equal')

# even = [2,4,6,8]
# odd = [1, 3, 5, 7, 9]
# another_even = even
# another_even.sort(reverse=True)
# print(even)
# print(even is another_even)
# another = list(even)
# print(even is another)

# number = [even, odd]
#
# for nums in number:
#     print(nums)
#
#     for val in nums:
#         print(val)
#
# menu = []
# menu.append(['egg', 'spam', 'bacon'])
# menu.append(['egg', 'sausage', 'baconn'])
# menu.append(['egg', 'spam', 'bascon'])
# menu.append(['egg', 'bacon', 'sausage', 'spam'])
# menu.append(['spam', 'egg', 'spam', 'bacon', 'spam'])
#
# print(menu)
#
# for meal in menu:
#     if not 'spam' in meal:
#         for item in meal:
#             print(item)
#
# myList = ['a', 'b', 'c', 'd']
# numbers = '123456789'
# newString = ''
# for c in myList:
#     newString += c + ', '
#
# print(newString)
#
# newString1 = ' mississippi '.join(numbers)
# print(newString1)

# locations = {
#     0: 'You are sitting in front of a computer learning Python',
#     1: 'You are standing at the end of a road before a small brick building',
#     2: 'You are at the top of a hill',
#     3: 'You are inside a building, a wall house for a small stream',
#     4: 'You are in a valley beside a stream',
#     5: 'You are in the forest'
# }
#
# exits = [
#     {'Q': 0},
#     {'W': 2, 'E': 3, 'N': 5, 'S': 4, 'Q': 0},
#     {'N': 5, 'Q': 0},
#     {'W': 1, 'Q': 0},
#     {'N': 1, 'W': 2, 'Q': 0},
#     {'W': 2, 'S': 1, 'Q': 0}
# ]
#
# print(locations[0].split())
# print(locations[3].split(','))
# print(' '.join(locations[0].split()))
#
# loc = 1
# while True:
#     #avaiableExist = ''
#     # for direction in exits[loc].keys():
#     #     avaiableExist += direction + ', '
#     avaiableExist = ', '.join(exits[loc].keys())
#     print(locations[loc])
#
#     if(loc== 0):
#         break
#     direction = input('Available exist are ' + avaiableExist + ' ').upper()
#     print()
#     # Parase the user input, using our vacabulary dictionary if necessary
#
#     if direction in exits[loc]:
#         loc = exits[loc][direction]
#     else:
#         print('You cannot go in that dirction')