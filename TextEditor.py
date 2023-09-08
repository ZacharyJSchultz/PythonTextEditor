import tkinter as tk
from tkinter import *
from tkinter.filedialog import asksaveasfilename

def save():
    filepath = asksaveasfilename(defaultextension = "txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    else:
        with open(filepath, "w") as output_file:
            text = editor.get(1.0, tk.END)
            output_file.write(text)
    window.title(f"{filepath}")
def clear():
    editor.delete("1.0", END)

window = Tk()                       #Create window using tkinter
window.geometry = "800 x 600"       #Text editor window size
window.title("Zach's Text Editor")

# Creates a heading, but looks bad so removed
#heading = Label(window, text = "Text Editor", font = ("bold", 26), bg = "grey")
#heading.pack()      #Ensures that the heading is actually put on the window

vertScroll = Scrollbar(window, orient = VERTICAL)   #Create a scrollbar on the right
vertScroll.pack(side = RIGHT, fill = Y)

editor = Text(window, width = 600, height = 800, yscrollcommand = vertScroll.set)    #Create the actual editor (where the user types)
editor.pack(fill = BOTH)

vertScroll.config(command = editor.yview)

saveButton = Button(window, text = 'Save', font = ('normal', 12), command = save, bg = 'red')       #Create save button
saveButton.place(x = 1360, y = 0)                                                                   #Place save button at specified coordinates

clearButton = Button(window, text = 'Clear', font = ('normal', 12), command = clear, bg = 'blue')
clearButton.place(x = 1294, y = 0)

if __name__ == '__main__':
    window.mainloop()