# Coded by Sabir Khan Akash 
# CSE '16, RUET
# www.github.com/SabirKhanAkash

from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from PIL import ImageFilter
from PIL import Image
from tkinter import font, colorchooser, filedialog, messagebox
from tkinter import ttk
import tkinter as tk
import os,sys
import tkinter.messagebox


root = Tk()
root.title("Easy Photo Editor")
root.iconbitmap("icons/EasyPhotoEditor.ico")
root.state("zoomed")

global op
global my_label2
op = 0

#All Functions

def hello():
    print("hello!")

def file_open(event=None):

	global my_ImageOpen
	global my_label2 
	global edge 
	global op
	global count
	global ImgDetails

	op = 1
	if count == 0:
		ImgDetails.destroy()

	count = 1;
	frame.filename = filedialog.askopenfilename(initialdir="D:\\Study Materials\\Study\\My Python Workspace\\3-2 Project\\EasyPhotoEditor\\Images\\", title= " Select a file", filetypes= (("All files","*.*"),("png","*.png"),("jpg", " *.jpg")))
	edge = Image.open(frame.filename)

	my_ImageOpen = ImageTk.PhotoImage(edge)
	my_label2 = ttk.Label(frame,image=my_ImageOpen)
	my_label2.pack(side=LEFT,fill=X)
	width, height = edge.size

	if count == 1:
		ImgDetails = Label(frameOpenFile, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack()
		count = 0


def save(event=None):
	if op == 0:
		tkinter.messagebox.showerror("Error","Open an image first !") 
	else:
		Image.open(frame.filename).save(frame.filename)
		print(op)


def save_as(event=None):
	if op == 1:
		filename = filedialog.asksaveasfile(mode='w', defaultextension='.jpg', title= " Save file as", filetypes= (("All files","*.*"),("png","*.png"),("jpg", " *.jpg")))
		edge.save(filename)
	else:
		tkinter.messagebox.showerror("Error","Open an image first !")
		
def rename(event=None):
	if op == 1:
		global e,f,renameWindow
		renameWindow = Tk()
		renameWindow.title("Rename this image")
		renameWindow.iconbitmap("icons/rename.ico")
		renameWindow.geometry("+400+250")
		renameWindow.minsize(300, 180)
		e = Entry(renameWindow, width=25,borderwidth=2)
		e.pack(side=LEFT,padx=15)
		e.insert(0, "Enter current name here")
		e.configure(state=DISABLED)

		def on_click(event):
		    e.configure(state=NORMAL)
		    e.delete(0, END)
		    e.unbind('<Button-1>', on_click_id_e)

		on_click_id_e = e.bind('<Button-1>', on_click)

		f = Entry(renameWindow, width=25,borderwidth=2)
		f.pack(side=LEFT,padx=15)
		f.insert(0, "Enter new name here")
		f.configure(state=DISABLED)

		def on_click(event):
		    f.configure(state=NORMAL)
		    f.delete(0, END)
		    f.unbind('<Button-1>', on_click_id_f)

		on_click_id_f = f.bind('<Button-1>', on_click)

		renameButton = ttk.Button(renameWindow, text="Rename", command=ren)
		renameButton.pack(side=LEFT,padx=10)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

def ren():
	global NewName,oldName 
	oldName = e.get()
	newName = f.get()
	os.chdir('D:\\Study Materials\\Study\\My Python Workspace\\3-2 Project\\EasyPhotoEditor\\Images\\')
	os.rename(oldName+".jpg",newName+".jpg")
	tkinter.messagebox.showinfo("Rename","Renamed successfully !")

def crop_now():
	global my_label2,my_ImageOpen,edge
	if op == 1:
		
		global x1,x2,y1,y2 
		x1 = float(imgX1Label.get())
		y1 = float(imgY1Label.get())
		x2 = float(imgX2Label.get())
		y2 = float(imgY2Label.get())
		print(x1,y1,x2,y2)
		edge = edge.crop((x1,y1,x2,y2))
		
		my_label2.destroy()

		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=LEFT,fill=X)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")


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
rotateR_icon = tk.PhotoImage(file='icons/rotateR.png')
hflip_icon = tk.PhotoImage(file='icons/hflip.png')
vflip_icon = tk.PhotoImage(file='icons/vflip.png')
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
filemenu.add_command(label="Save				        ", command=save, image=save_icon, compound=tk.LEFT, accelerator='ctrl+S')
filemenu.add_command(label="Save As    		            ", command=save_as, image=saveas_icon, compound=tk.LEFT, accelerator='ctrl+alt+S')
filemenu.add_command(label="Rename    		            ", command=rename, image=rename_icon, compound=tk.LEFT, accelerator='ctrl+R')
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

frameOpenFile = LabelFrame(root, padx=115, pady=1)
frameOpenFile.pack(side=TOP)

frameTools = LabelFrame(root, padx=10, pady=0)
frameTools.pack(side=TOP)

frameShare = LabelFrame(root)
frameShare.pack(side=TOP)

framesiteShare = LabelFrame(root)
framesiteShare.pack(side=TOP)

OpenImageButton = ttk.Button(frameOpenFile, text="Click here to open an image ",image=open_icon, compound=tk.TOP, command= file_open)
OpenImageButton.pack(ipadx=5,ipady=8, padx=5, pady=4)


myButton1 = ttk.Button(frameTools, text="Crop")
myButton2 = ttk.Button(frameTools, text="Rotate")
myButton3 = ttk.Button(frameTools, text="Filters")
myButton4 = ttk.Button(frameTools, text="Add Text")
myButton5 = ttk.Button(frameTools, text="Draw")
myButton6 = ttk.Button(frameTools, text="Adjust")


tabControl = ttk.Notebook(frameTools)

crop = ttk.Frame(tabControl)
tabControl.add(crop, text="    Crop    ", image=crop_icon, compound=tk.TOP)
tabControl.grid(row=0,column=0)

rotate = ttk.Frame(tabControl)
tabControl.add(rotate, text="    Rotate    ", image=rotate_icon, compound=tk.TOP)
tabControl.grid(row=0,column=1)

filters = ttk.Frame(tabControl)
tabControl.add(filters, text="    Filters    ", image=effects_icon, compound=tk.TOP)
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


#CROP SEGMENT

ep = Image.open("Images/Test.jpg")
HelpImage = ImageTk.PhotoImage(ep)
HelpImageLabel = ttk.Label(crop,image=HelpImage)
HelpImageLabel.pack()

imgX1Label = tk.Entry(crop, width=45,borderwidth=4)
imgX1Label.pack(ipadx=0,ipady=1,padx=2, pady=5)
imgX1Label.insert(0, "Enter X1 value here")
imgX1Label.configure(state=DISABLED)

def on_click(event):
		    imgX1Label.configure(state=NORMAL)
		    imgX1Label.delete(0, END)
		    imgX1Label.unbind('<Button-1>', on_click_id_X1)

on_click_id_X1 = imgX1Label.bind('<Button-1>', on_click)

imgY1Label = tk.Entry(crop, width=45,borderwidth=4)
imgY1Label.pack(ipadx=0,ipady=1,padx=1, pady=5)
imgY1Label.insert(0, "Enter Y1 value here")
imgY1Label.configure(state=DISABLED)

def on_click(event):
		    imgY1Label.configure(state=NORMAL)
		    imgY1Label.delete(0, END)
		    imgY1Label.unbind('<Button-1>', on_click_id_Y1)

on_click_id_Y1 = imgY1Label.bind('<Button-1>', on_click)

imgX2Label = tk.Entry(crop, width=45,borderwidth=4)
imgX2Label.pack(ipadx=0,ipady=1,padx=1, pady=5)
imgX2Label.insert(0, "Enter X2 value here")
imgX2Label.configure(state=DISABLED)

def on_click(event):
		    imgX2Label.configure(state=NORMAL)
		    imgX2Label.delete(0, END)
		    imgX2Label.unbind('<Button-1>', on_click_id_X2)

on_click_id_X2 = imgX2Label.bind('<Button-1>', on_click)

imgY2Label = tk.Entry(crop, width=45,borderwidth=4)
imgY2Label.pack(ipadx=0,ipady=1,padx=1, pady=5)
imgY2Label.insert(0, "Enter Y2 value here")
imgY2Label.configure(state=DISABLED)

def on_click(event):
		    imgY2Label.configure(state=NORMAL)
		    imgY2Label.delete(0, END)
		    imgY2Label.unbind('<Button-1>', on_click_id_Y2)

on_click_id_Y2 = imgY2Label.bind('<Button-1>', on_click)

CropButton = ttk.Button(crop, text="Crop", compound=tk.TOP,command=crop_now)
CropButton.pack(ipadx=2,ipady=3, padx=5, pady=5)


#Rotate Segment

LeftRotate = ttk.Button(rotate, text="Left Rotation", compound=tk.TOP, image=rotate_icon)
LeftRotate.pack(side=LEFT,ipadx=8,ipady=6, padx=15, pady=6)
RightRotate = ttk.Button(rotate, text="Right Rotation", compound=tk.TOP, image=rotateR_icon)
RightRotate.pack(side=RIGHT,ipadx=5,ipady=6, padx=15, pady=6)
HorizontalRotate = ttk.Button(rotate, text="Horizontal Flip", compound=tk.TOP, image=hflip_icon)
HorizontalRotate.pack(side=TOP,ipadx=3,ipady=6, padx=15, pady=37)
VerticalRotate = ttk.Button(rotate, text="Vertical Flip", compound=tk.TOP, image=vflip_icon)
VerticalRotate.pack(side=BOTTOM,ipadx=9,ipady=6, padx=15, pady=39)


#Filters Segment

Filter1 = ttk.Button(filters, text="Filter 1", compound=tk.TOP)
Filter1.place(x=35,y=18)
Filter2 = ttk.Button(filters, text="Filter 2", compound=tk.TOP)
Filter2.place(x=155,y=18)
Filter3 = ttk.Button(filters, text="Filter 3", compound=tk.TOP)
Filter3.place(x=270,y=18)

#Share Buttons Segment

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
