# Dictionary
fruit = {
    'orange': 'a sweet, ornage citrus fruit',
     'apple': 'good for maing cider',
     'lemon': 'a sour, yellow citrus fruit',
     'grape': 'a small, sweet fruit growing in bushes'
    }
# print(fruit)
# print(fruit['lemon'])
#
# fruit['pear'] = 'an odd shaped apple'
# print(fruit)
#
# fruit['pear'] = 'good with tequila'
# print(fruit)
#
# del fruit['lemon']
#del fruit will delete the entire fruit dictionary.
# print(fruit)

#clear the dictionary
#fruit.clear()
# print(fruit)

# validate a key before using it.
#
# while True:
#     dict_key = input('Enter a fruit: ')
#     if dict_key == 'quit':
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We don't have a {}".format(dict_key))

for snack in fruit:
    print(snack)

# Default key value on get
# while True:
#     dict_key = input('Enter a fruit: ')
#     if dict_key == 'quit':
#         break
#     description = fruit.get(dict_key, "We don't have a " + dict_key)
#
#     print(description)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# for f in ordered_keys:
#     print(f + ' - ' + fruit[f])
#
# for val in fruit.values():
#     print(val)

# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit['tomato'] = 'not a slice'
# print(fruit_keys)

# print(fruit.items())
# # convert dict to a tuple of tuples
# f_tuple = tuple(fruit.items())
# print(f_tuple)
#
# for snack in f_tuple:
#     item, description = snack
#     print(item + " is " + description)
#
# print(dict(f_tuple))

veg = {
    'cabbage': 'every childs favorite',
    'sprouts': 'mmmm, lovely',
    'spinach': 'can i have some more fruit, please'
}

print(veg)

veg.update(fruit)

print(veg)
print(fruit.update(veg))
print(fruit)

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)
print(veg)
print(fruit)

