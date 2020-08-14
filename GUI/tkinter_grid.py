import tkinter
root = tkinter.Tk() # there should be only one root window, and all the other widgets will be lower in hierarchy to the root so, the root has to be created first

root.title("yolo")
root.resizable(width = "false", height = "false")

root.minsize(width = 300, height = 100)
root.maxsize(width = 300, height = 100)


simple_label = tkinter.Label(root,text = 'hello world')
another_label = tkinter.Label(root, text = "some more text")
closing_button = tkinter.Button(root, text = "closing_button", command = simple_label.destroy)
another_button = tkinter.Button(root, text = "another_button", command = closing_button.destroy)

simple_label.grid(column = 0, row = 0, sticky = 'ns')
closing_button.grid(column = 1, row = 0, sticky = 'ns')
another_button.grid(column = 1, row = 1, sticky = 'ns')
another_label.grid(column = 2, row = 2,sticky = 'ns')
root.mainloop()

