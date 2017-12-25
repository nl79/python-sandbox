# for i in range(1, 20):
#     print("I is now {}", format(i))

number = '9,223,3723,234,223,5235'
cleanedNumber = ''
# for i in range(0, len(number)):
#     print(number[i])

# for i in range(0, len(number)):
#     if( number[i] in '0123456789'):
#         cleanedNumber = cleanedNumber + number[i]
#         #print(number[i], end='')
#
# newNumber = int(cleanedNumber)
# print("The number is {}".format(cleanedNumber))

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

for state in ["not pining", "no more", 'a stiff', 'bereft or life']:
    print('This parrot is ' + state)

for i in range(0, 100, 5):
    print('i {}'.format(i))

for i in range(1,13):
    for j in range(1,13):
        print('{1} time {0} is {2}'.format(i, j, i*j), end='\t')
    print('')
