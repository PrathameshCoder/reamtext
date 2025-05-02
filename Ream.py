from tkinter import *
from tkinter import Text
from tkinter import PhotoImage
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import font
import os

global selected
selected = False
#Functions
def newFile():
    global file
    root.title("Untitled - Ream Text")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Ream Text")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile= "Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file =="":
        file = None

    else:
        #Save as new file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

    root.title(os.path.basename(file) + " - Ream Text")
    print("File Saved")

   # else:

    # Save the file

    #f = open(file, "w")

    #f.write(TextArea.get(1.0, END))

    #f.close()

def quitFile():
    root.destroy()

def cut():
    global selected
    if TextArea.selection_get():
        selected = TextArea.selection_get()
        TextArea.delete("sel.first", "sel.last")

def copy():
    global selected
    if TextArea.selection_get():
        selected = TextArea.selection_get()

def paste():
    if selected:
        position = TextArea.index(INSERT)
        TextArea.insert(position, selected)

def bold_it():
    #Create a font
    bold_font = font.Font(TextArea, TextArea.cget("font"))
    bold_font.configure(weight="bold")

    # Configure a Tag
    TextArea.tag_configure("bold", font=bold_font)

    #Define Current Tags
    current_tags = TextArea.tag_names("sel.first")

    # If Statement to see if text is bold
    if "bold" in current_tags:
        TextArea.tag_remove("bold", "sel.first", "sel.last")
    else:
        TextArea.tag_add("bold", "sel.first", "sel.last")

def italics_it():
    # Create a font
    italics_font = font.Font(TextArea, TextArea.cget("font"))
    italics_font.configure(slant="italic")

    # Configure a Tag
    TextArea.tag_configure("italic", font=italics_font)

    # Define Current Tags
    current_tags = TextArea.tag_names("sel.first")

    # If Statement to see if text is bold
    if "italic" in current_tags:
        TextArea.tag_remove("italic", "sel.first", "sel.last")
    else:
        TextArea.tag_add("italic", "sel.first", "sel.last")

def about():
    showinfo("Ream Text", "Ream Text by Rhythmic Chaos")

# Basic Configs
root = Tk()
root.geometry("750x500")
root.title("Untitled - Ream Text")
#root.wm_iconbitmap("icon.ico")
img = PhotoImage(file="Icon.gif")
root.tk.call('wm', 'iconphoto', root._w, img)


Hor_scroll = Scrollbar
# Text Area Setup
TextArea: Text = Text(root, font="Montserrat 13", undo=True,)
file = None
TextArea.pack(expand=True, fill=BOTH)

# MenuBar Setup

MenuBar = Menu(root)

filemenu = Menu(MenuBar, tearoff=0)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_separator()
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quitFile)

root.config(menu=MenuBar)

MenuBar.add_cascade(label="File", menu=filemenu)

# Edit Menu

editmenu = Menu(MenuBar, tearoff=0)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)
editmenu.add_separator()
editmenu.add_command(label="Undo", command=TextArea.edit_undo)
editmenu.add_command(label="Redo", command=TextArea.edit_redo)

root.config(menu=MenuBar)

MenuBar.add_cascade(label="Edit", menu=editmenu)

#Style Menu

Stylemenu = Menu(MenuBar, tearoff=0)
Stylemenu.add_command(label="Bold", command=bold_it)
Stylemenu.add_command(label="Italics", command=italics_it)

root.config(menu=MenuBar)

MenuBar.add_cascade(label="Style", menu=Stylemenu)

#Help Menu
HelpMenu = Menu(MenuBar, tearoff=0)
HelpMenu.add_command(label="About Ream", command=about)
MenuBar.add_cascade(label="Help", menu=HelpMenu)

#scroll bar

Scroll = Scrollbar(TextArea, cursor="mouse")
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

# Horizontal Bar
#Hor_scroll = Scrollbar(TextArea, cursor="mouse", orient=HORIZONTAL)
#Hor_scroll.pack(side=BOTTOM, fill=X)
#Scroll.config(command=TextArea.xview)
#Hor_scroll.config(command=TextArea.xview)

#Status Bar
statusvar = StringVar()
statusvar.set("Ream Text File")
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X,)


root.mainloop()