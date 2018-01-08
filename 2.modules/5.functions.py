def python_foo():
    width = 80
    text = 'Spam and eggs'
    left_margin = (width - len(text)) // 2

    print(" " * left_margin, text)


def center_text(text):
    text = str(text)
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)

#Call the function
center_text('spam and eggs')
center_text('spam, spam and eggs')
center_text('spam, spam, spam and spam')
center_text(12)
