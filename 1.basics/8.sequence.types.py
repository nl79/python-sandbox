# ipAddress = input('Please enter an IP address')
# print(ipAddress.count('.'))

parrot_list = ['non pinin', 'no more', 'a stiff', 'bareft of life']
parrot_list.append('A norwegian blue')

for state in parrot_list:
    print('This parrot is {}'.format(state))

even = [2,4,6,8]
odd = [1,3,5,7,9]

number = even + odd
number.sort()
print(number)

#return a new object
sortedNumbers = sorted(number)
print(sortedNumbers)

if number == sortedNumbers:
    print('The lists are equal')
else:
    print('The list are not equal')
