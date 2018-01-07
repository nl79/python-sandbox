# jabber = open('./fixtures/sample.txt', 'r')
#
# for line in jabber:
#     print(line)
#
# jabber.close()

# with open('./fixtures/sample.txt', 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open('./fixtures/sample.txt', 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# with open('./fixtures/sample.txt', 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')


# with open('./fixtures/sample.txt', 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
# for line in lines[::-1]:
#     print(line, end='')

# with open('./fixtures/sample.txt', 'r') as jabber:
#     lines = jabber.read()
# print(lines)
# for line in lines[::-1]:
#     print(line, end='')


###### Writing to File ###############
# citites = ['adelaide', 'alice springs', 'darwin', 'malbourne', 'syden']
#
# with open('fixtures/cities.txt', 'w') as city_file:
#     for city in citites:
#         print(city, file=city_file)

# cities = []
#
# with open('fixtures/cities.txt', 'r') as city_files:
#     for city in city_files:
#         cities.append(city.strip('\n'))
#
# print(cities)
# for city in cities:
#     print(city)

# imelda = "More Mayham", "Imelda May", "2011", (
#     (1, "Pulling the rug"),
#     (2, 'Psycho'),
#     (3, 'Maymham'),
#     (4, "Kentish Town walts")
# )
#
# with open("fixtures/imelda3.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)

# with open('fixtures/imelda3.txt', 'r') as imelda_file:
#     contents = imelda_file.readline()
#
# imelda = eval(contents)
#
# print(imelda)
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
# print(tracks)

with open('fixtures/times.txt', 'w') as tables:
    for i in range(2, 13):
        for j in range(1, 13):
            print('{1:>2} times {0} is {2}'.format(i, j, i * j), file=tables)
        print('-' * 20, file=tables)