def python_foo():
    width = 80
    text = 'Spam and eggs'
    left_margin = (width - len(text)) // 2

    print(" " * left_margin, text)


def center_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


# Call the function
s1 = center_text('spam and eggs')
s2 = center_text('spam, spam and eggs')
s3 = center_text('spam, spam, spam and spam')
s4 = center_text(12)
s5 = center_text('first', 'second', 3, 8, 'spam')
print(s5)
