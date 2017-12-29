# t = ('a', 'b', 'c')
#
# print(t)
# print('a','b','c')
# print(('a','b','c'))
#

welcome = 'Welcome to my Nightmare', 'Alice Cooper', 1975
bad = 'Bad Company' 'Bad company', 1974
budgie = 'Nightflight', 'budgie', 1981, (
    (1, 'pulling the right'),
    (2, 'physcho'),
    (3, 'mayhem')
)
imelda = 'more mayhem', 'emilda may', 2011

print(imelda)
print(imelda[0])
print(imelda[1])
print(imelda[2])

imelda = imelda[0], 'Imedla May', imelda[2]

print(imelda)

imelda2 = ['Ride the lightning', 'imelda', 1984]
print(imelda2)
imelda2[0] = 'updated'
print(imelda2)

title, artist, year = imelda
print(title)
print(artist)
print(year)

title, artist, year, tracks = budgie
print(title)
print(artist)
print(year)
print(tracks)

