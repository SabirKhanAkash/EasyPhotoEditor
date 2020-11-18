# Coded by Sabir Khan Akash 
# CSE '16, RUET
# www.github.com/SabirKhanAkash

from tkinter import *
from PIL import ImageTk, Image, ImageDraw, ImageFont
from PIL import ImageFilter
from PIL import Image
from PIL import ImageOps
from PIL import ImageFont
import PIL.ImageFont
import PIL.ImageOps
from tkinter import font, colorchooser, filedialog, messagebox
from tkinter import ttk
import tkinter as tk
import os,sys
import tkinter.messagebox
from tkinter.ttk import Combobox


root = Tk()
root.title("Easy Photo Editor")
root.iconbitmap("icons/EasyPhotoEditor.ico")
root.state("zoomed")

global op
global my_label2
global width, height
global reset_image
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
	global width,height
	global reset_image

	op = 1
	if count == 0:
		ImgDetails.destroy()
		my_label2.destroy()

	count = 1;
	frame.filename = filedialog.askopenfilename(initialdir="D:\\Study Materials\\Study\\My Python Workspace\\3-2 Project\\EasyPhotoEditor\\Images\\", title= " Select a file", filetypes= (("All files","*.*"),("png","*.png"),("jpg", " *.jpg")))
	edge = Image.open(frame.filename)
	width, height = edge.size
	
	reset_image = edge
	if width>890 or height>600:
		edge = edge.resize((890, 600), Image.ANTIALIAS)

	my_ImageOpen = ImageTk.PhotoImage(edge)
	my_label2 = ttk.Label(frame,image=my_ImageOpen)
	my_label2.pack(side=TOP,fill=BOTH,padx=2,pady=2,anchor="nw")
	width, height = edge.size

	if count == 1:
		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)
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
		renameWindow.iconbitmap("icons/rename.png")
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
	global imgX1Label,imgY1Label,imgX2Label,imgY2Label
	global my_label2,my_ImageOpen,edge, ImgDetails
	ImgDetails.destroy()
	
	if op == 1:
		
		global x1,x2,y1,y2 
		x1 = float(imgX1Label.get())
		y1 = float(imgY1Label.get())
		x2 = float(imgX2Label.get())
		y2 = float(imgY2Label.get())

		print(x1,y1,x2,y2)
		my_label2.destroy()
		edge = reset_image.crop((x1,y1,x2,y2))
		width, height = edge.size

		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

	imgX1Label.delete(0, END)
	imgX1Label.insert(0, "Enter X1 value here")
	imgX1Label.configure(state=DISABLED)

	def on_click(event):
		    imgX1Label.configure(state=NORMAL)
		    imgX1Label.delete(0, END)
		    imgX1Label.unbind('<Button-1>', on_click_id_X1)

	on_click_id_X1 = imgX1Label.bind('<Button-1>', on_click)

	imgY1Label.delete(0, END)
	imgY1Label.insert(0, "Enter Y1 value here")
	imgY1Label.configure(state=DISABLED)

	def on_click(event):
			    imgY1Label.configure(state=NORMAL)
			    imgY1Label.delete(0, END)
			    imgY1Label.unbind('<Button-1>', on_click_id_Y1)

	on_click_id_Y1 = imgY1Label.bind('<Button-1>', on_click)

	imgX2Label.delete(0, END)
	imgX2Label.insert(0, "Enter X2 value here")
	imgX2Label.configure(state=DISABLED)

	def on_click(event):
			    imgX2Label.configure(state=NORMAL)
			    imgX2Label.delete(0, END)
			    imgX2Label.unbind('<Button-1>', on_click_id_X2)

	on_click_id_X2 = imgX2Label.bind('<Button-1>', on_click)

	imgY2Label.delete(0, END)
	imgY2Label.insert(0, "Enter Y2 value here")
	imgY2Label.configure(state=DISABLED)

	def on_click(event):
			    imgY2Label.configure(state=NORMAL)
			    imgY2Label.delete(0, END)
			    imgY2Label.unbind('<Button-1>', on_click_id_Y2)

	on_click_id_Y2 = imgY2Label.bind('<Button-1>', on_click)


def reset_now():
	global imgX1Label,imgY1Label,imgX2Label,imgY2Label,txtY1Label,txtX1Label
	global my_label2,my_ImageOpen,edge,width,height
	global reset_image

	edge = reset_image
	if op == 1:
		my_label2.destroy()
		my_ImageOpen = ImageTk.PhotoImage(reset_image)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=LEFT,fill=X)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

	imgX1Label.delete(0, END)
	imgX1Label.insert(0, "Enter X1 value here")
	imgX1Label.configure(state=DISABLED)

	def on_click(event):
		    imgX1Label.configure(state=NORMAL)
		    imgX1Label.delete(0, END)
		    imgX1Label.unbind('<Button-1>', on_click_id_X1)

	on_click_id_X1 = imgX1Label.bind('<Button-1>', on_click)

	imgY1Label.delete(0, END)
	imgY1Label.insert(0, "Enter Y1 value here")
	imgY1Label.configure(state=DISABLED)

	def on_click(event):
			    imgY1Label.configure(state=NORMAL)
			    imgY1Label.delete(0, END)
			    imgY1Label.unbind('<Button-1>', on_click_id_Y1)

	on_click_id_Y1 = imgY1Label.bind('<Button-1>', on_click)

	imgX2Label.delete(0, END)
	imgX2Label.insert(0, "Enter X2 value here")
	imgX2Label.configure(state=DISABLED)

	def on_click(event):
			    imgX2Label.configure(state=NORMAL)
			    imgX2Label.delete(0, END)
			    imgX2Label.unbind('<Button-1>', on_click_id_X2)

	on_click_id_X2 = imgX2Label.bind('<Button-1>', on_click)

	imgY2Label.delete(0, END)
	imgY2Label.insert(0, "Enter Y2 value here")
	imgY2Label.configure(state=DISABLED)

	def on_click(event):
			    imgY2Label.configure(state=NORMAL)
			    imgY2Label.delete(0, END)
			    imgY2Label.unbind('<Button-1>', on_click_id_Y2)

	on_click_id_Y2 = imgY2Label.bind('<Button-1>', on_click)

	txtX1Label.insert(0, "Enter X1 value here")
	txtX1Label.configure(state=DISABLED)

	def on_click(event):
			    txtX1Label.configure(state=NORMAL)
			    txtX1Label.delete(0, END)
			    txtX1Label.unbind('<Button-1>', on_click_id_tX1)

	on_click_id_tX1 = txtX1Label.bind('<Button-1>', on_click)

	txtY1Label = tk.Entry(addtext, width=30,borderwidth=3)
	txtY1Label.place(x=95,y=220,height=28,width=187)
	txtY1Label.insert(0, "Enter Y1 value here")
	txtY1Label.configure(state=DISABLED)

	def on_click(event):
			    txtY1Label.configure(state=NORMAL)
			    txtY1Label.delete(0, END)
			    txtY1Label.unbind('<Button-1>', on_click_id_tY1)

	on_click_id_tY1 = txtY1Label.bind('<Button-1>', on_click)


def left_rotate():
	global my_label2,my_ImageOpen,edge,a, ImgDetails
	

	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		edge = edge.rotate(90, expand=True)
		width, height = edge.size


		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")


def right_rotate():
	global my_label2,my_ImageOpen,edge,a, ImgDetails
	

	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		edge = edge.rotate(270, expand=True)
		width, height = edge.size


		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

def hori_flip():
	global my_label2,my_ImageOpen,edge,a, ImgDetails
	

	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		edge = edge.transpose(Image.FLIP_LEFT_RIGHT)
		width, height = edge.size


		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")


def ver_flip():
	global my_label2,my_ImageOpen,edge,a, ImgDetails
	

	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		edge = edge.transpose(Image.FLIP_TOP_BOTTOM)
		width, height = edge.size


		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

def blur():
	global my_label2,my_ImageOpen,edge,a, ImgDetails
	

	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		edge = edge.filter(ImageFilter.GaussianBlur(3))
		width, height = edge.size


		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

def BLACKBOARD():
	global my_label2,my_ImageOpen,edge,a, ImgDetails
	

	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		edge = edge.filter(ImageFilter.FIND_EDGES)
		width, height = edge.size


		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

def contour():
	global my_label2,my_ImageOpen,edge,a, ImgDetails
	

	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		edge = edge.filter(ImageFilter.CONTOUR)
		width, height = edge.size


		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

def edge_enhance():
	global my_label2,my_ImageOpen,edge,a, ImgDetails
	

	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		edge = edge.filter(ImageFilter.EDGE_ENHANCE)
		width, height = edge.size


		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

def sharpen():
	global my_label2,my_ImageOpen,edge,a, ImgDetails
	

	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		edge = edge.filter(ImageFilter.SHARPEN)
		width, height = edge.size


		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

def smooth_more():
	global my_label2,my_ImageOpen,edge,a, ImgDetails
	

	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		edge = edge.filter(ImageFilter.SMOOTH_MORE)
		width, height = edge.size


		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

def greyscale():
	global my_label2,my_ImageOpen,edge,a, ImgDetails
	

	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		width, height = edge.size
		pixels = edge.load()
		

		for py in range(height):
			for px in range(width):
				r,g,b = edge.getpixel((px,py))
				newr = (r+g+b)//3
				newg = (r+g+b)//3
				newb = (r+g+b)//3
				pixels[px,py] = (newr,newg,newb)

		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")	

def sepia():
	global my_label2,my_ImageOpen,edge,a, ImgDetails
	

	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		width, height = edge.size
		edge.convert("RGB")
		pixels = edge.load()
		

		for py in range(height):
			for px in range(width):
				r,g,b = edge.getpixel((px,py))
				newr = int((r * .393)+(g * .769)+(b* .189))
				newg = int((r * .349)+(g * .686)+(b* .168))
				newb = int((r * .272)+(g * .534)+(b* .131))
				pixels[px,py] = (newr,newg,newb)

		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")


def inverted():
	global my_label2,my_ImageOpen,edge,a, ImgDetails
	
	

	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		edge = PIL.ImageOps.invert(edge)
		width, height = edge.size


		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

def fontClicked(event):
	global Fontfamily
	fontDir = "D:\\Study Materials\\Study\\My Python Workspace\\3-2 Project\\EasyPhotoEditor\\fonts\\"
	fontExt = ".ttf"
	Fontfamily = fontDir+font.get()+fontExt
	print(Fontfamily)

def fontColorClicked(event):
	global Fontcolor
	Fontcolor = fontColor.get()

	if Fontcolor == "Violet":
		vr = int(102)
		vg = int(0) 
		vb = int(102)
	elif Fontcolor == "Yellow":
		yr = int(255)
		yg = int(255)
		yb = int(0)
	elif Fontcolor == "Blue":
		br = int(0)
		bg = int(0)
		bb = int(255)
	elif Fontcolor == "Green":
		gr = int(0)
		gg = int(102)
		gb = int(0)
	elif Fontcolor == "Orange":
		orr = int(255)
		org = int(128)
		orb = int(0)
	elif Fontcolor == "Black":
		br = int(0)
		bg = int(0)
		bb = int(0)
	elif Fontcolor == "Brown":
		brr = int(102)
		brg = int(51)
		brb = int(0)
	elif Fontcolor == "White":
		wr = int(255)
		wg = int(255)
		wb = int(255)
	elif Fontcolor == "Indigo":
		ir = int(51)
		ig = int(153)
		ib = int(255)
	elif Fontcolor == "Lime":
		lr = int(153)
		lg = int(255)
		lb = int(51)
	elif Fontcolor == "Gray":
		grr = int(128)
		grg = int(128)
		grb = int(128)

	print(Fontcolor)	

def fontSizeClicked(event):
	global Fontsize
	Fontsize = int(fontSize.get())
	print(Fontsize)	

def addtextnow():
	global my_label2,my_ImageOpen,edge,a, ImgDetails, Fontfamily,Fontcolor, Fontsize, txtX1Label, txtY1Label
	

	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		a = float(txtX1Label.get())
		b = float(txtY1Label.get())
		
		width, height = edge.size
		font_type = ImageFont.truetype(Fontfamily,Fontsize)
		draw = ImageDraw.Draw(edge)
		if Fontcolor == "Violet":
			vr = int(102)
			vg = int(0) 
			vb = int(102)
			draw.text(xy=(a,b),text="Hello World",fill=(vr,vg,vb),font=font_type)
		elif Fontcolor == "Yellow":
			yr = int(255)
			yg = int(255)
			yb = int(0)
			draw.text(xy=(a,b),text="Hello World",fill=(yr,yg,yb),font=font_type)
		elif Fontcolor == "Blue":
			br = int(0)
			bg = int(0)
			bb = int(255)
			draw.text(xy=(a,b),text="Hello World",fill=(br,bg,bb),font=font_type)
		elif Fontcolor == "Green":
			gr = int(0)
			gg = int(102)
			gb = int(0)
			draw.text(xy=(a,b),text="Hello World",fill=(gr,gg,gb),font=font_type)
		elif Fontcolor == "Orange":
			orr = int(255)
			org = int(128)
			orb = int(0)
			draw.text(xy=(a,b),text="Hello World",fill=(orr,org,orb),font=font_type)
		elif Fontcolor == "Black":
			br = int(0)
			bg = int(0)
			bb = int(0)
			draw.text(xy=(a,b),text="Hello World",fill=(br,bg,bb),font=font_type)
		elif Fontcolor == "Brown":
			brr = int(102)
			brg = int(51)
			brb = int(0)
			draw.text(xy=(a,b),text="Hello World",fill=(brr,brg,brb),font=font_type)
		elif Fontcolor == "White":
			wr = int(255)
			wg = int(255)
			wb = int(255)
			draw.text(xy=(a,b),text="Hello World",fill=(wr,wg,wb),font=font_type)
		elif Fontcolor == "Indigo":
			ir = int(51)
			ig = int(153)
			ib = int(255)
			draw.text(xy=(a,b),text="Hello World",fill=(ir,ig,ib),font=font_type)
		elif Fontcolor == "Lime":
			lr = int(153)
			lg = int(255)
			lb = int(51)
			draw.text(xy=(a,b),text="Hello World",fill=(lr,lg,lb),font=font_type)
		elif Fontcolor == "Gray":
			grr = int(128)
			grg = int(128)
			grb = int(128)
			draw.text(xy=(a,b),text="Hello World",fill=(grr,grg,grb),font=font_type)

		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

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
reset_icon = tk.PhotoImage(file='icons/reset.png')
reset_icon2 = tk.PhotoImage(file='icons/resettext.png')
crop2_icon = tk.PhotoImage(file='icons/crop2.png')

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
frame = LabelFrame(root,padx=20, pady=20, height=677, width= 944)
frame.place(x=5,y=3)

frameOpenFile = LabelFrame(root, padx=115, pady=1)
# frameOpenFile.pack(side=TOP,pady=1)
frameOpenFile.place(x=950,y=2)

frameTools = LabelFrame(root, padx=10, pady=0)
frameTools.place(x=950,y=116)

frameShare = LabelFrame(root, pady=1)
frameShare.place(x=950,y=560)

framesiteShare = LabelFrame(root, pady=1)
framesiteShare.place(x=950,y=620)

OpenImageButton = ttk.Button(frameOpenFile, text="Click here to open an image ",image=open_icon, compound=tk.TOP, command= file_open)
OpenImageButton.pack(ipadx=5,ipady=2, padx=5, pady=5)


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

CropButton = ttk.Button(crop, text="Crop", compound=tk.LEFT,command=crop_now, image=crop2_icon)
CropButton.pack(ipadx=2,ipady=1, padx=50, pady=2, side=LEFT)

ResetButton = ttk.Button(crop, text="Reset", compound=tk.LEFT, command=reset_now, image=reset_icon)
ResetButton.pack(ipadx=2,ipady=3, padx=10, pady=2, side=LEFT)

#Rotate Segment

LeftRotate = ttk.Button(rotate, text="Left Rotation", compound=tk.TOP, image=rotate_icon,command=left_rotate)
LeftRotate.pack(side=LEFT,ipadx=8,ipady=6, padx=15, pady=6)
RightRotate = ttk.Button(rotate, text="Right Rotation", compound=tk.TOP, image=rotateR_icon,command=right_rotate)
RightRotate.pack(side=RIGHT,ipadx=5,ipady=6, padx=15, pady=6)
HorizontalFlip = ttk.Button(rotate, text="Horizontal Flip", compound=tk.TOP, image=hflip_icon,command=hori_flip)
HorizontalFlip.pack(side=TOP,ipadx=3,ipady=6, padx=15, pady=37)
VerticalFlip = ttk.Button(rotate, text="Vertical Flip", compound=tk.TOP, image=vflip_icon,command=ver_flip)
VerticalFlip.pack(side=BOTTOM,ipadx=9,ipady=6, padx=15, pady=39)

ResetButton = ttk.Button(rotate, text="Reset", compound=tk.TOP, command=reset_now, image=reset_icon)
ResetButton.pack(ipadx=2,ipady=3, padx=0, pady=5, side=BOTTOM)

#Filters Segment

BLUR = ttk.Button(filters, text="BLUR\n", compound=tk.TOP,command=blur)
BLUR.place(x=35,y=18)
BLACKBOARD = ttk.Button(filters, text="BLACK\nBOARD", compound=tk.TOP,command=BLACKBOARD)
BLACKBOARD.place(x=155,y=18)
CONTOUR = ttk.Button(filters, text="CONTOUR\n", compound=tk.TOP,command=contour)
CONTOUR.place(x=270,y=18)
EDGE_ENHANCE = ttk.Button(filters, text="    EDGE \nENHANCE", compound=tk.TOP,command=edge_enhance)
EDGE_ENHANCE.place(x=35,y=125)
SHARPEN = ttk.Button(filters, text="SHARPEN\n", compound=tk.TOP,command=sharpen)
SHARPEN.place(x=155,y=125)
SMOOTH_MORE = ttk.Button(filters, text="    MORE \n SMOOTH", compound=tk.TOP,command=smooth_more)
SMOOTH_MORE.place(x=270,y=125)
INVERTED = ttk.Button(filters, text="INVERTED\n", compound=tk.TOP,command=inverted)
INVERTED.place(x=35,y=232)
GREYSCALE = ttk.Button(filters, text="GREYSCALE\n", compound=tk.TOP,command=greyscale)
GREYSCALE.place(x=155,y=232)
SEPIA = ttk.Button(filters, text="SEPIA\n", compound=tk.TOP,command=sepia)
SEPIA.place(x=270,y=232)

ResetButton = ttk.Button(filters, text="Reset", compound=tk.TOP, command=reset_now, image=reset_icon)
ResetButton.pack(ipadx=2,ipady=3, padx=0, pady=5, side=BOTTOM)

#AddText Segment
fontLabel = ttk.Label(addtext,text="Font Family")
fontLabel.place(x=95,y=15)
font = ttk.Combobox(addtext,values=('Bahnschrift','BisonBold','Calibri Bold Italic','Calibri Bold','Calibri Italic','Calibri Regular','CascadiaCode','ComicSans','FranklinGothic','Genuine','Impact','Juniorprince Regular','Krinkes Regular','SiyamRupali','TimesNewRoman','Unispace Bold','Unispace Bold Italic','Unispace Italic','Unispace Regular','ValentLovey'), width=35,justify=CENTER,state='readonly')
font.set("Choose a font family")
font.bind("<<ComboboxSelected>>",fontClicked)
font.place(x=98,y=40,height=28,width=180)

fontColorLabel = ttk.Label(addtext,text="Font Color")
fontColorLabel.place(x=95,y=85)
fontColor = ttk.Combobox(addtext,values=('Violet','Yellow','Blue','Green','Orange','Black','Brown','White','Indigo','Lime','Gray'), width=35,justify=CENTER,state='readonly')
fontColor.set("Choose a font color")
fontColor.bind("<<ComboboxSelected>>",fontColorClicked)
fontColor.place(x=98,y=109,height=28,width=180)

TextPosLabel = ttk.Label(addtext,text="Adjust Text Position")
TextPosLabel.place(x=95,y=155)

txtX1Label = tk.Entry(addtext, width=30,borderwidth=3)
txtX1Label.place(x=95,y=180,height=28,width=187)
txtX1Label.insert(0, "Enter X1 value here")
txtX1Label.configure(state=DISABLED)

def on_click(event):
		    txtX1Label.configure(state=NORMAL)
		    txtX1Label.delete(0, END)
		    txtX1Label.unbind('<Button-1>', on_click_id_tX1)

on_click_id_tX1 = txtX1Label.bind('<Button-1>', on_click)

txtY1Label = tk.Entry(addtext, width=30,borderwidth=3)
txtY1Label.place(x=95,y=220,height=28,width=187)
txtY1Label.insert(0, "Enter Y1 value here")
txtY1Label.configure(state=DISABLED)

def on_click(event):
		    txtY1Label.configure(state=NORMAL)
		    txtY1Label.delete(0, END)
		    txtY1Label.unbind('<Button-1>', on_click_id_tY1)

on_click_id_tY1 = txtY1Label.bind('<Button-1>', on_click)

fontSizeLabel = ttk.Label(addtext,text="Font Size")
fontSizeLabel.place(x=95,y=258)
fontSize = ttk.Combobox(addtext,values=('8','9','10','11','12','14','16','18','20','22','24','26','28','36','48','72','94','130'), width=35,justify=CENTER,state='readonly')
fontSize.set("Choose a Font Size")
fontSize.bind("<<ComboboxSelected>>",fontSizeClicked)
fontSize.place(x=98,y=280,height=28,width=180)

addtextButton = ttk.Button(addtext, text="Add Text", compound=tk.LEFT, image=text_icon, command=addtextnow)
addtextButton.place(x=72,y=330)

ResetButton = ttk.Button(addtext, text="Reset", compound=tk.LEFT, command=reset_now, image=reset_icon2)
ResetButton.place(x=200,y=331)

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
