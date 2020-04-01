# Coded by Sabir Khan Akash 
# CSE '16, RUET
# www.github.com/SabirKhanAkash

from tkinter import *
from PIL import ImageTk,Image
from tkinter import font, colorchooser, filedialog, messagebox
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title("Easy Photo Editor")
root.iconbitmap("icons/EasyPhotoEditor.ico")
root.state("zoomed")
# root.minsize(1366, 768)

def hello():
    print("hello!")

def file_open():
	global my_ImageOpen
	frame.filename = filedialog.askopenfilename(initialdir="D:/Study Materials/Study/My Python Workspace/3-2 Project/EasyPhotoEditor/Images", title= " Select a file", filetypes= (("png","*.png"),("jpg", " *.jpg"),("All files","*.*")))
	my_ImageOpen = ImageTk.PhotoImage(Image.open(frame.filename))
	my_label2 = ttk.Label(frame,image=my_ImageOpen)
	my_label2.pack(side=LEFT,fill=X)

# create pulldown menus
menubar = Menu(root)

#declaring all icons
open_icon = tk.PhotoImage(file='icons/open.png')

openf_icon = tk.PhotoImage(file='icons/openf.png')
save_icon = tk.PhotoImage(file='icons/save.png')
saveas_icon = tk.PhotoImage(file='icons/save_as.png')
rename_icon = tk.PhotoImage(file='icons/rename.png')
exit_icon = tk.PhotoImage(file='icons/exit.png')

undo_icon = tk.PhotoImage(file='icons/undo.png')
redo_icon = tk.PhotoImage(file='icons/redo.png')
cut_icon = tk.PhotoImage(file='icons/cut.png')
copy_icon = tk.PhotoImage(file='icons/copy.png')
paste_icon = tk.PhotoImage(file='icons/paste.png')

about_icon = tk.PhotoImage(file='icons/about.png')
updates_icon = tk.PhotoImage(file='icons/updates.png')
bug_icon = tk.PhotoImage(file='icons/bug.png')

light_default_icon = tk.PhotoImage(file='icons/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons/light_plus.png')
dark_icon = tk.PhotoImage(file='icons/dark.png')
red_icon = tk.PhotoImage(file='icons/red.png')
monokai_icon = tk.PhotoImage(file='icons/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons/night_blue.png')

crop_icon = tk.PhotoImage(file='icons/crop.png')
rotate_icon = tk.PhotoImage(file='icons/rotate.png')
effects_icon = tk.PhotoImage(file='icons/effects.png')
text_icon = tk.PhotoImage(file='icons/text.png')
draw_icon = tk.PhotoImage(file='icons/draw.png')
adjust_icon = tk.PhotoImage(file='icons/adjust.png')

share_icon = tk.PhotoImage(file='icons/share.png')

fb_icon = tk.PhotoImage(file='icons/facebook.png')
twitter_icon = tk.PhotoImage(file='icons/twitter.png')
insta_icon = tk.PhotoImage(file='icons/instagram.png')
gdrive_icon = tk.PhotoImage(file='icons/gdrive.png')
mail_icon = tk.PhotoImage(file='icons/mail.png')

#creating menu items
filemenu = tk.Menu(menubar, tearoff=0)
editmenu = tk.Menu(menubar, tearoff=0)
helpmenu = tk.Menu(menubar, tearoff=0)
thememenu = tk.Menu(menubar, tearoff=0)

#adding commands
filemenu.add_command(label="Open File  				    ", command=file_open, image=openf_icon, compound=tk.LEFT, accelerator='ctrl+O')
filemenu.add_command(label="Save				        ", command=hello, image=save_icon, compound=tk.LEFT, accelerator='ctrl+S')
filemenu.add_command(label="Save As    		            ", command=hello, image=saveas_icon, compound=tk.LEFT, accelerator='ctrl+alt+S')
filemenu.add_command(label="Rename    		            ", command=hello, image=rename_icon, compound=tk.LEFT, accelerator='ctrl+R')
filemenu.add_separator()
filemenu.add_command(label="Exit				        ", command=root.quit, image=exit_icon, compound=tk.LEFT, accelerator='ctrl+Q')

editmenu.add_command(label="Undo				", command=hello, image=undo_icon, compound=tk.LEFT, accelerator='ctrl+Z')
editmenu.add_command(label="Redo				", command=hello, image=redo_icon, compound=tk.LEFT, accelerator='ctrl+shift+z')
editmenu.add_separator()
editmenu.add_command(label="Cut                 ", command=hello, image=cut_icon, compound=tk.LEFT, accelerator='ctrl+X')
editmenu.add_command(label="Copy                ", command=hello, image=copy_icon, compound=tk.LEFT, accelerator='ctrl+C')
editmenu.add_command(label="Paste               ", command=hello, image=paste_icon, compound=tk.LEFT, accelerator='ctrl+V')

helpmenu.add_command(label="About EasyPhotoEditor       ", command=hello, image=about_icon, compound=tk.LEFT, accelerator='ctrl+A')
helpmenu.add_command(label="Check for updates           ", command=hello, image=updates_icon, compound=tk.LEFT, accelerator='ctrl+U')
helpmenu.add_command(label="Report Bugs to Dev           ", command=hello, image=bug_icon, compound=tk.LEFT, accelerator='ctrl+B')


theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
	' Light default': ('#000000', '#FFFFFF'),
	' Light plus': ('#474747', '#e0e0e0'),
	' Dark': ('#c4c4c4', '#2d2d2d'),
	' Red': ('#2d2d2d', '#ffe8e8'),
	' Monokai': ('#d3b774', '#474747'),
	' Night Blue': ('#ededed', '#6b9dc2'),
}
count = 0
for i in color_dict:
	thememenu.add_radiobutton(label=i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT)
	count = count + 1

#cascading all menus
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)
menubar.add_cascade(label="Theme", menu=thememenu)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

#declaring frames
frame = LabelFrame(root,padx=20, pady=20, height=700, width= 950)
frame.pack(side=LEFT)

frameOpenFile = LabelFrame(root, padx=115, pady=5)
frameOpenFile.pack(side=TOP)

frameTools = LabelFrame(root, padx=10, pady=10)
frameTools.pack(side=TOP)

frameShare = LabelFrame(root)
frameShare.pack(side=TOP)

framesiteShare = LabelFrame(root)
framesiteShare.pack(side=TOP)


def open():
	global my_ImageOpen
	frame.filename = filedialog.askopenfilename(initialdir="D:/Study Materials/Study/My Python Workspace/3-2 Project/EasyPhotoEditor/Images", title= " Select a file", filetypes= (("png","*.png"),("jpg", " *.jpg"),("All files","*.*")))
	my_ImageOpen = ImageTk.PhotoImage(Image.open(frame.filename))
	my_label2 = ttk.Label(frame,image=my_ImageOpen)
	my_label2.pack()

OpenImageButton = ttk.Button(frameOpenFile, text="Click here to open an image ",image=open_icon, compound=tk.TOP, command= open)
OpenImageButton.pack(ipadx=5,ipady=10, padx=5, pady=15)

# my_img = ImageTk.PhotoImage(Image.open("Images/Sample 3.png"))
# my_label = Label(frame,text="currently no photo is selected !!!")
# my_label.pack()


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


tabControl = ttk.Notebook(frameTools)

crop = ttk.Frame(tabControl)
tabControl.add(crop, text="    Crop    ", image=crop_icon, compound=tk.TOP)
tabControl.grid(row=0,column=0,ipady=160, pady=5)

rotate = ttk.Frame(tabControl)
tabControl.add(rotate, text="    Rotate    ", image=rotate_icon, compound=tk.TOP)
tabControl.grid(row=0,column=1)

effects = ttk.Frame(tabControl)
tabControl.add(effects, text="    Effects    ", image=effects_icon, compound=tk.TOP)
tabControl.grid(row=0,column=2)

addtext = ttk.Frame(tabControl)
tabControl.add(addtext, text="  Add Text  ", image=text_icon, compound=tk.TOP)
tabControl.grid(row=0,column=3)

draw = ttk.Frame(tabControl)
tabControl.add(draw, text="    Draw    ", image=draw_icon, compound=tk.TOP)
tabControl.grid(row=0,column=3)

adjust = ttk.Frame(tabControl)
tabControl.add(adjust, text="    Adjust    ", image=adjust_icon, compound=tk.TOP)
tabControl.grid(row=0,column=4)

# myButton1.grid(row=0, column=0, ipadx=1, ipady=8, )
# myButton2.grid(row=0, column=1, padx=15, ipadx=1, ipady=8)
# myButton3.grid(row=2, column=2, padx=30)
# myButton4.grid(row=3, column=2, padx=30)
# myButton5.grid(row=5, column=2, padx=30)
# myButton6.grid(row=6, column=2, padx=30)
# myButton2.pack(ipadx=20,ipady=10, padx=10, pady=10)
# myButton3.pack(ipadx=20,ipady=10, padx=10, pady=10)
# myButton4.pack(ipadx=20,ipady=10, padx=10, pady=10)
# myButton5.pack(ipadx=20,ipady=10, padx=10, pady=10)
# myButton6.pack(ipadx=20,ipady=10, padx=10, pady=10)

shareLabel = Label(frameShare, text="Share this image by uploading to following social networking sites !", image=share_icon, compound=tk.LEFT)
shareLabel.pack(side=TOP)
fbButton = ttk.Button(framesiteShare, text="Facebook",image=fb_icon, compound=tk.TOP)
fbButton.pack(side=LEFT,padx=3)
fbButton = ttk.Button(framesiteShare, text="Instagram",image=insta_icon, compound=tk.TOP)
fbButton.pack(side=LEFT,padx=3)
fbButton = ttk.Button(framesiteShare, text="Twitter",image=twitter_icon, compound=tk.TOP)
fbButton.pack(side=LEFT,padx=3)
fbButton = ttk.Button(framesiteShare, text="G Drive",image=gdrive_icon, compound=tk.TOP)
fbButton.pack(side=LEFT,padx=3)
fbButton = ttk.Button(framesiteShare, text="Gmail",image=mail_icon, compound=tk.TOP)
fbButton.pack(side=LEFT,padx=3)



root.mainloop()
