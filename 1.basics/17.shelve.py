import shelve

# with shelve.open('fixtures/ShelfTest') as fruit:
#     fruit['orange'] = 'a sweet, orange citrus fruit'
#     fruit['apple'] = 'apple'
#     fruit['lemon'] = 'lemon'
#     fruit['grape'] = 'grape'
#     fruit['lime'] = 'lime'
#
#     print(fruit['orange'])
#     print(fruit['grape'])

# fruit = shelve.open('fixtures/ShelfTest')
# fruit['orange'] = 'a sweet, orange citrus fruit'
# fruit['apple'] = 'apple'
# fruit['lemon'] = 'lemon'
# fruit['grape'] = 'grape'
# fruit['lime'] = 'lime'

# print(fruit['orange'])
# print(fruit['grape'])
#
# fruit['lime'] = 'lime update'
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])

# while True:
#     shelve_key = input("Plese enter a fruit")
#     if shelve_key == 'quit':
#         break
#     description = fruit.get(shelve_key)
#     print(description)
#
# fruit.close()

# blt = ['bacon', 'lettuce', 'tomato', 'bread']
# beans_on_toast = ['beans', 'bread']
# scrambled_eggs = ['eggs', 'butter', 'milk']
# soup = ['tin of soup']
# paste = ['paste', 'cheese']
#
# with shelve.open('recipe', writeback=True) as recipes:
#     recipes['blt'] = blt
#     recipes['beans_on_toast'] = beans_on_toast
#     recipes['scrambled_eggs'] = scrambled_eggs
#     recipes['soup'] = soup
#     recipes['paste'] = paste
#
#     recipes['blt'].append('butter')
#     recipes['paste'].append('tomato')
#
#     temp_list = recipes['blt']
#     temp_list.append('butter')
#     recipes['blt'] = temp_list
#
#     temp_list = recipes['paste']
#     temp_list.append('tomato')
#     recipes['paste'] = temp_list
#
#     recipes['soup'].append('croutons')
#     recipes['paste'] = paste
#     recipes.sync()
#     paste.append('cream')
#
#     for snack in recipes:
#         print(snack, recipes[snack])
#

books = shelve.open('fixtures/book')

books["recipes"] = {
        'blt': ['bacon', 'lettuce', 'tomato', 'bread'],
        'beans_on_toast': ['beans', 'bread'],
        'scrambled_eggs': ['eggs', 'butter', 'milk'],
        'soup': ['tin of soup'],
        "paste": ['paste', 'cheese']
    }
books['maitenance'] = {
        'stuck': ['oil'],
        'loose': ['gaffer tape']
    }


print(books['recipes']['soup'])
print(books['recipes']['scrambled_eggs'])

print(books['maitenance']['loose'])
books.close()