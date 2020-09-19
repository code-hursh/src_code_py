import tkinter
root = tkinter.Tk() # there should be only one root window, and all the other widgets will be lower in hierarchy to the root so, the root has to be created first

root.title("yolo")
root.resizable(width = "false", height = "false")

root.minsize(width = 300, height = 50)
root.maxsize(width = 300, height = 50)


# TO CREATE A WIDGET:
    # create the instance of the specifice widget's class
    # use the available methods to attach the widget to the parent widget

simple_label = tkinter.Label(root,text = 'hello world')

closing_button = tkinter.Button(root, text = "destroy", command = simple_label.destroy)

# simple_label.pack(fill = 'x')
# closing_button.pack(fill = 'x')

simple_label.pack(side = 'left')
closing_button.pack(side = 'left')



root.mainloop()

