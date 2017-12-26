# number = "9,522,646,433,643,643"
# cleanedNumber = ''
#
# for i in range(0, len(number)):
#     if number[i] in '012345689':
#         cleanedNumber += number[i]
#
# newNumber = int(cleanedNumber)
# print('The number is {} '.format(newNumber))
#
# x = 23
# x += 1
# print(x)
#
# x -= 1
# print(x)
#
# x *= 5
# print(x)
#
# x /= 5
# print(x)
#
# x **= 2
# print(x)
#
# x %= 2
# print(x)
#
# msg = 'Hello '
#
# msg *= 5
# print(msg)
#

ip = input('Enter an IP Address ')
temp = '';
count = 0;
for char in ip:
    if char in '0123456789':
        temp += char

    else:
        count += 1
        print('Segment# ' + str(count) + ' ' + temp + ' Length: ' + str(len(temp)))
        temp = ''
else:
    print('Segment# ' + str(count + 1) + ' ' + temp + ' Length: ' + str(len(temp)))
