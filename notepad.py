from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename

def newFile():
    global file
    root.title("Notepad")
    file=None
    textarea.delete(1.0, END)

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        textarea.delete(1.0,END)
        f=open(file, "r")    
        textarea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text documents","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(textarea.get(1.0, END))
            f.close()    

            root.title(os.path.basename(file)+ " - Notepad")
            print("File Saved")
    else:
        f=open(file,"w")
        f.write(textarea.get(1.0, END))
        f.close() 

def quitApp():
    root.destroy()
def copy():
    textarea.event_generate(("<<Copy>>"))
def cut():
    textarea.event_generate(("<<Cut>>"))
def paste():
    textarea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad", "Notepad by Saurabh")

root=Tk()
root.title("Notepad")
root.geometry("600x500")

textarea=Text(root, font=("helvetica, 20"))
file=None
textarea.pack(expand=True, fill=BOTH)

MenuBar=Menu(root)
fileMenu=Menu(MenuBar, tearoff=0)

fileMenu.add_command(label="New",command=newFile)

fileMenu.add_command(label="Open",command=openFile)

fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quitApp)
MenuBar.add_cascade(label="File",menu=fileMenu)

EditMenu=Menu(MenuBar,tearoff=0)
EditMenu.add_command(label="Copy",command=copy)
EditMenu.add_command(label="Cut",command=cut)
EditMenu.add_command(label="Paste",command=paste)

MenuBar.add_cascade(label="Edit",menu=EditMenu)

HelpMenu=Menu(MenuBar, tearoff=0)
HelpMenu.add_command(label="About Notepad",command=about)
MenuBar.add_cascade(label="Help",menu=HelpMenu)

root.config(menu=MenuBar)

Scroll=Scrollbar(textarea)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=Scroll.set)

root.mainloop()
