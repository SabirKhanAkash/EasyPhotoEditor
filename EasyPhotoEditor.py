from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import ttk

root = Tk()
root.title("Easy Photo Editor")
root.iconbitmap("EasyPhotoEditor.ico")
root.minsize(1366, 768)




def hello():
    print("hello!")

def file_open():
	global my_ImageOpen
	frame.filename = filedialog.askopenfilename(initialdir="D:/Study Materials/Study/My Python Workspace/3-2 Project/EasyPhotoEditor/Images", title= " Select a file", filetypes= (("png","*.png"),("jpg", " *.jpg"),("All files","*.*")))
	my_ImageOpen = ImageTk.PhotoImage(Image.open(frame.filename))
	my_label2 = ttk.Label(frame,image=my_ImageOpen)
	my_label2.grid(row=0,column=0)

# create pulldown menus
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open File  				    ", command=file_open)
filemenu.add_command(label="Save				        ", command=hello)
filemenu.add_command(label="Save As    		            ", command=hello)
filemenu.add_command(label="Rename    		            ", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit				        ", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)


editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo				", command=hello)
editmenu.add_command(label="Redo				", command=hello)
editmenu.add_command(label="Cut                 ", command=hello)
editmenu.add_command(label="Copy                ", command=hello)
editmenu.add_command(label="Paste               ", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About               ", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.geometry("1366x768+0+0")

frame = LabelFrame(root, padx=151, pady=30)
frame.grid(row=0,column=0)

frameTools = LabelFrame(root, padx=10, pady=50)
frameTools.grid(row=0,column=1,sticky=E)

frameOpenFile = LabelFrame(root, padx=505, pady=20)
frameOpenFile.grid(row=1,column=0)

def open():
	global my_ImageOpen
	frame.filename = filedialog.askopenfilename(initialdir="D:/Study Materials/Study/My Python Workspace/3-2 Project/EasyPhotoEditor/Images", title= " Select a file", filetypes= (("png","*.png"),("jpg", " *.jpg"),("All files","*.*")))
	my_ImageOpen = ImageTk.PhotoImage(Image.open(frame.filename))
	my_label2 = ttk.Label(frame,image=my_ImageOpen)
	my_label2.grid(row=0,column=0)

OpenImageButton = ttk.Button(frameOpenFile, text=" Open an image ", command= open)
OpenImageButton.grid(row=1,column=0)

# my_img = ImageTk.PhotoImage(Image.open("Images/Sample 3.png"))
my_label = ttk.Label(frame,text="currently no photo is selected !!!")
my_label.grid(row=0,column=0)


# def myClick1():
# 	myLabel1 = Label(root, text="Thanks for your rating !")
# 	myLabel1.grid()

# def myClick2():
# 	myLabel2 = Label(root, text="don't forget to rate us.")
# 	myLabel2.grid()

# def myClick3():
# 	myLabel3 = Label(root, text="OK We'll ask you later.")
# 	myLabel3.grid()

myButton1 = ttk.Button(frameTools, text="Crop")
myButton2 = ttk.Button(frameTools, text="Rotate")
myButton3 = ttk.Button(frameTools, text="Effects")
myButton4 = ttk.Button(frameTools, text="Add Text")
myButton5 = ttk.Button(frameTools, text="Draw")
myButton6 = ttk.Button(frameTools, text="Adjust")

myButton1.grid(row=0, column=1)
myButton2.grid(row=1, column=1)
myButton3.grid(row=0, column=2)
myButton4.grid(row=1, column=2)
myButton5.grid(row=0, column=3)
myButton6.grid(row=1, column=3)

root.mainloop()
