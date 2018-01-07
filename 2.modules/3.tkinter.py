try:
    import tkinter
except ImportError: #python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

#tkinter._test()
mainWindow = tkinter.Tk()

mainWindow.title('Hello World')
mainWindow.geometry('640x480+8+400')
mainWindow.mainloop()
