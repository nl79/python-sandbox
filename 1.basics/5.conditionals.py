for i in range(1, 12):
    print("No {} squared is {} and cubed is {:4}".format(i, i**2, i**3))
    print("Calculation complete")
    print("try again")

name = input("Please enter your name: ")
age = int(input("How old are you, {0}: ".format(name)))
print(age)

if age >= 18:
    print('You are old enough to vote')
    print("Please put an X in the box")
else:
    print('Please come back in {0} years'.format(18 - age))

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < 5:
    print('Please guess higher')
    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
elif guess > 5:
    print("Please guess lower")
    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it")
    else:
        print('Sorry, you have no guessed correctly')
else:
    print("you got it first time")

age = int(input("How old are you: "))

if (age >= 16) and (age <= 65):
    print("have a good day at work")

if 16 <= age <= 65:
    print('have a good day at work')

if (age < 16) or (age > 65):
    print('enjoy your free time')
else:
    print('have a good day at work')


#Boolean operations
x = input("Please enter some text ")
if x:
    print('You entered {}'.format(x))
else:
    print('You did not enter anything')

print(not False)
print(not True)

name = input("Enter Name: ")
age = int(input("Enter Age: "))

if 17 < age < 31:
    print("Welcome to the holiday")
else:
    print("You dont fit the criteria")

