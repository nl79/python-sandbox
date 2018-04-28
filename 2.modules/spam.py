def spam():

    def spam2():

        def spam3():
            z = " even more spam"
            z += y
            print("In Spam3, locals are {}".format(locals()))
            return z

        y = " more spam" + x
        y += spam3()
        print("In Spam2, locals are {}".format(locals()))

        return y

    x = " spam "
    x += spam2()
    print("In Spam1, locals are {}".format(locals()))

    return x

print(spam())