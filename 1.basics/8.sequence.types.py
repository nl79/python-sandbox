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

even = [2,4,6,8]
odd = [1, 3, 5, 7, 9]
# another_even = even
# another_even.sort(reverse=True)
# print(even)
# print(even is another_even)
# another = list(even)
# print(even is another)

number = [even, odd]

for nums in number:
    print(nums)

    for val in nums:
        print(val)
