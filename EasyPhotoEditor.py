# Coded by Sabir Khan Akash 
# CSE '16, RUET
# www.github.com/SabirKhanAkash

#importing Modules

import PIL.ImageFont
import PIL.ImageOps
import webbrowser
import tkinter as tk
import os,sys
import tkinter.messagebox
from tkinter import *
from PIL import ImageTk, Image, ImageDraw, ImageFont
from PIL import ImageFilter
from PIL import Image
from PIL import ImageOps
from PIL import ImageFont
from tkinter import font, colorchooser, filedialog, messagebox
from tkinter import ttk
from tkinter.ttk import Combobox
from PIL import ImageEnhance
from time import sleep

#declaring main root window

root = Tk()
root.title("Easy Photo Editor")
root.iconbitmap("icons/EasyPhotoEditor.ico")
root.state("zoomed")

#some global variables

global op
global my_label2
global width, height
global reset_image
global brmeter
op = 0

#All Functions

def hello():
    print("hello!")

def changeTheme():
	chosenTheme = theme_choice.get()
	colorTuple = color_dict.get(chosenTheme)
	fgColor, bgColor = colorTuple[0], colorTuple[1]
	frame.config(background=bgColor,fg=fgColor)
	framesiteShare.config(background=bgColor,fg=fgColor)
	frameShare.config(background=bgColor,fg=fgColor)
	frameTools.config(background=bgColor,fg=fgColor)
	frameOpenFile.config(background=bgColor,fg=fgColor)
	shareLabel.config(background=bgColor,fg=fgColor)


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
	frame.filename = filedialog.askopenfilename( title= " Select a file", defaultextension='.jpg', filetypes= (("jpg", " *.jpg"),("All files","*.*")))
	root.title(frame.filename+" - "+"Easy Photo Editor")
	print(frame.filename)
	edge = Image.open(frame.filename)
	width, height = edge.size
	
	reset_image = edge
	if width>890 or height>600:
		edge = edge.resize((890, 600), Image.ANTIALIAS)
		reset_image = edge
	my_ImageOpen = ImageTk.PhotoImage(edge)
	my_label2 = ttk.Label(frame,image=my_ImageOpen,justify=CENTER)
	my_label2.pack(side=TOP,fill=BOTH,padx=2,pady=2,anchor="nw")
	width, height = edge.size

	if count == 1:
		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)
		count = 0


def save(event=None):
	if op == 1:
		Image.open(frame.filename).save(frame.filename)
	else:
		tkinter.messagebox.showerror("Error","Open an image first !")
		


def save_as(event=None):
	if op == 1:
		filename = filedialog.asksaveasfile(mode='w', title= " Save file as", filetypes= (("jpg", " *.jpg"),("All files","*.*")))
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
		e = tk.Entry(renameWindow, width=25,borderwidth=2)
		e.pack(side=LEFT,padx=15)
		e.insert(0, "Enter current name here")
		e.configure(state=DISABLED)

		def on_click(event):
		    e.configure(state=NORMAL)
		    e.delete(0, END)
		    e.unbind('<Button-1>', on_click_id_e)

		on_click_id_e = e.bind('<Button-1>', on_click)

		f = tk.Entry(renameWindow, width=25,borderwidth=2)
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
	oldName2 = oldName+".jpg"
	print(frame.filename)
	os.chdir((frame.filename).removesuffix(oldName2))
	os.rename(oldName+".jpg",newName+".jpg")
	tkinter.messagebox.showinfo("Rename","Renamed successfully !")
	renameWindow.quit()

def quit(event=None):
	root.quit()

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
	global imgX1Label,imgY1Label,imgX2Label,imgY2Label,txtY1Label,txtX1Label,txtLabel
	global my_label2,my_ImageOpen,edge,width,height
	global reset_image
	brightness.set(5)
	contrast.set(5)
	shadow.set(5)
	saturation.set(5)
	sharpness.set(5)
	enhancement.set(0)
	

	if op == 1:
		my_label2.destroy()
		my_ImageOpen = ImageTk.PhotoImage(reset_image)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=LEFT,fill=X)
		
		edge = reset_image

	else:
		ImageTk.messagebox.showerror("Error","Open an image first !")

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

	txtX1Label.delete(0, END)
	txtX1Label.insert(0, "Enter X1 value here")
	txtX1Label.configure(state=DISABLED)

	def on_click(event):
			    txtX1Label.configure(state=NORMAL)
			    txtX1Label.delete(0, END)
			    txtX1Label.unbind('<Button-1>', on_click_id_tX1)

	on_click_id_tX1 = txtX1Label.bind('<Button-1>', on_click)

	txtY1Label.delete(0, END)
	txtY1Label.insert(0, "Enter Y1 value here")
	txtY1Label.configure(state=DISABLED)

	def on_click(event):
			    txtY1Label.configure(state=NORMAL)
			    txtY1Label.delete(0, END)
			    txtY1Label.unbind('<Button-1>', on_click_id_tY1)

	on_click_id_tY1 = txtY1Label.bind('<Button-1>', on_click)

	txtLabel.delete(0, END)
	txtLabel.insert(0, "Enter your Text here")
	txtLabel.configure(state=DISABLED)

	def on_click(event):
			    txtLabel.configure(state=NORMAL)
			    txtLabel.delete(0, END)
			    txtLabel.unbind('<Button-1>', on_click_id_tX)

	on_click_id_tX = txtLabel.bind('<Button-1>', on_click)


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
	global newr,newg,newb,r,g,b,px,py,pixels

	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		width, height = edge.size

		grey = ImageEnhance.Color(edge)
		edge = grey.enhance(0.0)

		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")	

def emboss():
	global my_label2,my_ImageOpen,edge,a, ImgDetails
	global newr,newg,newb,r,g,b,px,py,pixels,reset_image

	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		width, height = edge.size
		edge = edge.filter(ImageFilter.EDGE_ENHANCE)
		edge = edge.filter(ImageFilter.SMOOTH)
		edge = edge.filter(ImageFilter.EMBOSS)

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
	fontDir = "fonts/"
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
	global reset_image,draw,my_label2,my_ImageOpen,edge,a, ImgDetails, Fontfamily,Fontcolor, Fontsize, txtX1Label, txtY1Label,txtLabel
	
	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		a = float(txtX1Label.get())
		b = float(txtY1Label.get())
		maintext = txtLabel.get()
		
		width, height = edge.size
		font_type = ImageFont.truetype(Fontfamily,Fontsize)
		reset_image = edge
		draw = ImageDraw.Draw(edge)
		if Fontcolor == "Violet":
			vr = int(102)
			vg = int(0) 
			vb = int(102)
			draw.text(xy=(a,b),text=maintext,fill=(vr,vg,vb),font=font_type)
		elif Fontcolor == "Yellow":
			yr = int(255)
			yg = int(255)
			yb = int(0)
			draw.text(xy=(a,b),text=maintext,fill=(yr,yg,yb),font=font_type)
		elif Fontcolor == "Blue":
			br = int(0)
			bg = int(0)
			bb = int(255)
			draw.text(xy=(a,b),text=maintext,fill=(br,bg,bb),font=font_type)
		elif Fontcolor == "Green":
			gr = int(0)
			gg = int(102)
			gb = int(0)
			draw.text(xy=(a,b),text=maintext,fill=(gr,gg,gb),font=font_type)
		elif Fontcolor == "Orange":
			orr = int(255)
			org = int(128)
			orb = int(0)
			draw.text(xy=(a,b),text=maintext,fill=(orr,org,orb),font=font_type)
		elif Fontcolor == "Black":
			br = int(0)
			bg = int(0)
			bb = int(0)
			draw.text(xy=(a,b),text=maintext,fill=(br,bg,bb),font=font_type)
		elif Fontcolor == "Brown":
			brr = int(102)
			brg = int(51)
			brb = int(0)
			draw.text(xy=(a,b),text=maintext,fill=(brr,brg,brb),font=font_type)
		elif Fontcolor == "White":
			wr = int(255)
			wg = int(255)
			wb = int(255)
			draw.text(xy=(a,b),text=maintext,fill=(wr,wg,wb),font=font_type)
		elif Fontcolor == "Indigo":
			ir = int(51)
			ig = int(153)
			ib = int(255)
			draw.text(xy=(a,b),text=maintext,fill=(ir,ig,ib),font=font_type)
		elif Fontcolor == "Lime":
			lr = int(153)
			lg = int(255)
			lb = int(51)
			draw.text(xy=(a,b),text=maintext,fill=(lr,lg,lb),font=font_type)
		elif Fontcolor == "Gray":
			grr = int(128)
			grg = int(128)
			grb = int(128)
			draw.text(xy=(a,b),text=maintext,fill=(grr,grg,grb),font=font_type)

		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

def br():
	global my_label2,my_ImageOpen,edge,a, ImgDetails
	
	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		
		br_edge = ImageEnhance.Brightness(edge)

		if int(brightness.get()) == 0:
			edge = br_edge.enhance(0.5)
		elif int(brightness.get()) == 1:
			edge = br_edge.enhance(0.6)
		elif int(brightness.get()) == 2:
			edge = br_edge.enhance(0.7)
		elif int(brightness.get()) == 3:
			edge = br_edge.enhance(0.8)
		elif int(brightness.get()) == 4:
			edge = br_edge.enhance(0.9)
		elif int(brightness.get()) == 5:
			edge = br_edge.enhance(1.0)
		elif int(brightness.get()) == 6:
			edge = br_edge.enhance(1.1)
		elif int(brightness.get()) == 7:
			edge = br_edge.enhance(1.2)
		elif int(brightness.get()) == 8:
			edge = br_edge.enhance(1.3)
		elif int(brightness.get()) == 9:
			edge = br_edge.enhance(1.4)
		elif int(brightness.get()) == 10:
			edge = br_edge.enhance(1.5)

		width, height = edge.size


		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)



	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

def con():
	global my_label2,my_ImageOpen,edge,a, ImgDetails
	
	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		
		br_edge = ImageEnhance.Contrast(edge)

		if int(contrast.get()) == 0:
			edge = br_edge.enhance(0.5)
		elif int(contrast.get()) == 1:
			edge = br_edge.enhance(0.6)
		elif int(contrast.get()) == 2:
			edge = br_edge.enhance(0.7)
		elif int(contrast.get()) == 3:
			edge = br_edge.enhance(0.8)
		elif int(contrast.get()) == 4:
			edge = br_edge.enhance(0.9)
		elif int(contrast.get()) == 5:
			edge = br_edge.enhance(1.0)
		elif int(contrast.get()) == 6:
			edge = br_edge.enhance(1.1)
		elif int(contrast.get()) == 7:
			edge = br_edge.enhance(1.2)
		elif int(contrast.get()) == 8:
			edge = br_edge.enhance(1.3)
		elif int(contrast.get()) == 9:
			edge = br_edge.enhance(1.4)
		elif int(contrast.get()) == 10:
			edge = br_edge.enhance(1.5)

		width, height = edge.size


		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")


def sharp():
	global my_label2,my_ImageOpen,edge,a, ImgDetails
	
	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		
		br_edge = ImageEnhance.Sharpness(edge)

		if int(sharpness.get()) == 0:
			edge = br_edge.enhance(0.5)
		elif int(sharpness.get()) == 1:
			edge = br_edge.enhance(0.6)
		elif int(sharpness.get()) == 2:
			edge = br_edge.enhance(0.7)
		elif int(sharpness.get()) == 3:
			edge = br_edge.enhance(0.8)
		elif int(sharpness.get()) == 4:
			edge = br_edge.enhance(0.9)
		elif int(sharpness.get()) == 5:
			edge = br_edge.enhance(1.0)
		elif int(sharpness.get()) == 6:
			edge = br_edge.enhance(1.1)
		elif int(sharpness.get()) == 7:
			edge = br_edge.enhance(1.2)
		elif int(sharpness.get()) == 8:
			edge = br_edge.enhance(1.3)
		elif int(sharpness.get()) == 9:
			edge = br_edge.enhance(1.4)
		elif int(sharpness.get()) == 10:
			edge = br_edge.enhance(1.5)

		width, height = edge.size


		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

def sat():
	global my_label2,my_ImageOpen,edge,a, ImgDetails
	
	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		
		br_edge = ImageEnhance.Color(edge)

		if int(saturation.get()) == 0:
			edge = br_edge.enhance(0.5)
		elif int(saturation.get()) == 1:
			edge = br_edge.enhance(0.6)
		elif int(saturation.get()) == 2:
			edge = br_edge.enhance(0.7)
		elif int(saturation.get()) == 3:
			edge = br_edge.enhance(0.8)
		elif int(saturation.get()) == 4:
			edge = br_edge.enhance(0.9)
		elif int(saturation.get()) == 5:
			edge = br_edge.enhance(1.0)
		elif int(saturation.get()) == 6:
			edge = br_edge.enhance(1.1)
		elif int(saturation.get()) == 7:
			edge = br_edge.enhance(1.2)
		elif int(saturation.get()) == 8:
			edge = br_edge.enhance(1.3)
		elif int(saturation.get()) == 9:
			edge = br_edge.enhance(1.4)
		elif int(saturation.get()) == 10:
			edge = br_edge.enhance(1.5)

		width, height = edge.size


		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

def shad():
	global my_label2,my_ImageOpen,edge,a, ImgDetails
	
	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()
		
		# br_edge = ImageEnhance.Brightness(edge)
		# con_edge = ImageEnhance.Contrast(edge)

		if int(shadow.get()) == 0:
			br_edge = ImageEnhance.Brightness(edge)
			edge = br_edge.enhance(0.95)
			con_edge = ImageEnhance.Contrast(edge)
			edge = con_edge.enhance(1)
			sat_edge = ImageEnhance.Color(edge)
			edge = sat_edge.enhance(0.70)
		elif int(shadow.get()) == 1:
			br_edge = ImageEnhance.Brightness(edge)
			edge = br_edge.enhance(0.92)
			con_edge = ImageEnhance.Contrast(edge)
			edge = con_edge.enhance(1.05)
			sat_edge = ImageEnhance.Color(edge)
			edge = sat_edge.enhance(0.73)
		elif int(shadow.get()) == 2:
			br_edge = ImageEnhance.Brightness(edge)
			edge = br_edge.enhance(0.90)
			con_edge = ImageEnhance.Contrast(edge)
			edge = con_edge.enhance(1.10)
			sat_edge = ImageEnhance.Color(edge)
			edge = sat_edge.enhance(0.75)
		elif int(shadow.get()) == 3:
			br_edge = ImageEnhance.Brightness(edge)
			edge = br_edge.enhance(0.87)
			con_edge = ImageEnhance.Contrast(edge)
			edge = con_edge.enhance(1.15)
			sat_edge = ImageEnhance.Color(edge)
			edge = sat_edge.enhance(0.77)
		elif int(shadow.get()) == 4:
			br_edge = ImageEnhance.Brightness(edge)
			edge = br_edge.enhance(0.84)
			con_edge = ImageEnhance.Contrast(edge)
			edge = con_edge.enhance(1.20)
			sat_edge = ImageEnhance.Color(edge)
			edge = sat_edge.enhance(0.80)
		elif int(shadow.get()) == 5:
			br_edge = ImageEnhance.Brightness(edge)
			edge = br_edge.enhance(0.82)
			con_edge = ImageEnhance.Contrast(edge)
			edge = con_edge.enhance(1.25)
			sat_edge = ImageEnhance.Color(edge)
			edge = sat_edge.enhance(0.82)
		elif int(shadow.get()) == 6:
			br_edge = ImageEnhance.Brightness(edge)
			edge = br_edge.enhance(0.80)
			con_edge = ImageEnhance.Contrast(edge)
			edge = con_edge.enhance(1.30)
			sat_edge = ImageEnhance.Color(edge)
			edge = sat_edge.enhance(0.84)
		elif int(shadow.get()) == 7:
			br_edge = ImageEnhance.Brightness(edge)
			edge = br_edge.enhance(0.77)
			con_edge = ImageEnhance.Contrast(edge)
			edge = con_edge.enhance(1.35)
			sat_edge = ImageEnhance.Color(edge)
			edge = sat_edge.enhance(0.87)
		elif int(shadow.get()) == 8:
			br_edge = ImageEnhance.Brightness(edge)
			edge = br_edge.enhance(0.75)
			con_edge = ImageEnhance.Contrast(edge)
			edge = con_edge.enhance(1.40)
			sat_edge = ImageEnhance.Color(edge)
			edge = sat_edge.enhance(0.90)
		elif int(shadow.get()) == 9:
			br_edge = ImageEnhance.Brightness(edge)
			edge = br_edge.enhance(0.73)
			con_edge = ImageEnhance.Contrast(edge)
			edge = con_edge.enhance(1.45)
			sat_edge = ImageEnhance.Color(edge)
			edge = sat_edge.enhance(0.92)
		elif int(shadow.get()) == 10:
			br_edge = ImageEnhance.Brightness(edge)
			edge = br_edge.enhance(0.70)
			con_edge = ImageEnhance.Contrast(edge)
			edge = con_edge.enhance(1.50)
			sat_edge = ImageEnhance.Color(edge)
			edge = sat_edge.enhance(0.95)

		width, height = edge.size


		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

def en():
	global my_label2,my_ImageOpen,edge,a, ImgDetails
	

	if op == 1:
		ImgDetails.destroy()
		my_label2.destroy()

		edge = edge.filter(ImageFilter.DETAIL)
		width, height = edge.size


		my_ImageOpen = ImageTk.PhotoImage(edge)
		my_label2 = ttk.Label(frame,image=my_ImageOpen)
		my_label2.pack(side=TOP,fill=X)

		ImgDetails = Label(frame, text="current image's width = "+str(width)+" and height = "+str(height))
		ImgDetails.pack(side=BOTTOM)

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")	


def fb():
	if op == 1:
		webbrowser.open("http://www.facebook.com")

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

def ig():
	if op == 1:
		webbrowser.open("http://www.instagram.com")

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

def tw():
	if op == 1:
		webbrowser.open("http://www.twitter.com")

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

def gdr():
	if op == 1:
		webbrowser.open("http://www.drive.google.com")

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

def gm():
	if op == 1:
		webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

	else:
		tkinter.messagebox.showerror("Error","Open an image first !")

def taskaboutApp():
    sleep(3)
    aboutApp.destroy()

def taskupdate():
    sleep(2)
    updateApp.destroy()

def bug():
	webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
	reportBug.destroy()

def about():
	global aboutApp
	aboutApp = Tk()
	aboutApp.title("About Easy Photo Editor")
	aboutApp.iconbitmap("icons/EasyPhotoEditor.ico")
	aboutApp.geometry("+550+250")
	aboutApp.minsize(300, 180)
	aboutApp.resizable(0, 0)
	aboutApp.config(bg="black")
	name = Label(aboutApp,text="Easy Photo Editor",justify=CENTER,bg="black")
	name.config(font=("FranklinGothic", 20),fg="white")
	ver = Label(aboutApp,text="Version 1.0",justify=CENTER,bg="black")
	ver.config(font=("FranklinGothic",12),fg="white")
	name.place(x=35,y=35)
	ver.place(x=100,y=90)
	devName = Label(aboutApp,text="Developed by Sabir Khan Akash\n All Rights Reserved. © 2020",justify=CENTER,bg="black")
	devName.config(font=("FranklinGothic", 10),fg="white")
	devName.place(x=55,y=135)
	aboutApp.after(200, taskaboutApp)

def update():
	global updateApp
	updateApp = Tk()
	updateApp.title("Checking for Updates")
	updateApp.iconbitmap("icons/updates.ico")
	updateApp.geometry("+550+250")
	updateApp.minsize(300, 180)
	updateApp.resizable(0, 0)
	updateApp.config(bg="black")
	name = Label(updateApp,text="Easy Photo Editor",justify=CENTER,bg="black")
	name.config(font=("FranklinGothic", 20),fg="white")
	ver = Label(updateApp,text="Version 1.0",justify=CENTER,bg="black")
	ver.config(font=("FranklinGothic",12),fg="white")
	name.place(x=35,y=35)
	ver.place(x=100,y=90)
	updatetext = Label(updateApp,text="You are already using the latest version.",justify=CENTER,bg="black")
	updatetext.config(font=("FranklinGothic",10),fg="white")
	updatetext.place(x=35,y=135)
	updateApp.after(200, taskupdate)


def report():
	global reportBug
	reportBug = Tk()
	reportBug.title("Report Bugs to Dev")
	reportBug.iconbitmap("icons/bug.ico")
	reportBug.geometry("+550+250")
	reportBug.minsize(300, 100)
	reportBug.resizable(0, 0)
	reportBug.config(bg="black")
	name = Label(reportBug,text="Easy Photo Editor",justify=CENTER,bg="black")
	name.config(font=("FranklinGothic", 20),fg="white")
	ver = Label(reportBug,text="Version 1.0",justify=CENTER,bg="black")
	ver.config(font=("FranklinGothic",12),fg="white")
	devmail = Label(reportBug,text="Dev Mail: 1603108@student.ruet.ac.bd",justify=CENTER,bg="black")
	devmail.config(font=("FranklinGothic", 10),fg="white")
	name.place(x=35,y=35)
	ver.place(x=100,y=75)
	devmail.place(x=35,y=100)
	reportButton = ttk.Button(reportBug,text="Click Here to mail your bug report",command=bug)
	reportButton.place(x=55,y=135)


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
text_icon2 = tk.PhotoImage(file='icons/text2.png')
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
apply2_icon = tk.PhotoImage(file='icons/apply2.png')
adapply_icon = tk.PhotoImage(file='icons/apply.png')

#creating menu items
filemenu = tk.Menu(menubar, tearoff=0)
# editmenu = tk.Menu(menubar, tearoff=0)
helpmenu = tk.Menu(menubar, tearoff=0)
thememenu = tk.Menu(menubar, tearoff=0)

#adding commands
filemenu.add_command(label="Open File  		", command=file_open, image=openf_icon, compound=tk.LEFT,accelerator='ctrl+o')
filemenu.add_command(label="Save		    ", command=save, image=save_icon, compound=tk.LEFT,accelerator='ctrl+s')
filemenu.add_command(label="Save As         ", command=save_as, image=saveas_icon, compound=tk.LEFT,accelerator='alt+s')
filemenu.add_command(label="Rename          ", command=rename, image=rename_icon, compound=tk.LEFT,accelerator='ctrl+r')
filemenu.add_separator()
filemenu.add_command(label="Exit        ", command=quit, image=exit_icon, compound=tk.LEFT,accelerator='ctrl+q')

# editmenu.add_command(label="Undo				", command=hello, image=undo_icon, compound=tk.LEFT, accelerator='ctrl+Z')
# editmenu.add_command(label="Redo				", command=hello, image=redo_icon, compound=tk.LEFT, accelerator='ctrl+shift+z')
# editmenu.add_separator()
# editmenu.add_command(label="Cut                 ", command=hello, image=cut_icon, compound=tk.LEFT, accelerator='ctrl+X')
# editmenu.add_command(label="Copy                ", command=hello, image=copy_icon, compound=tk.LEFT, accelerator='ctrl+C')
# editmenu.add_command(label="Paste               ", command=hello, image=paste_icon, compound=tk.LEFT, accelerator='ctrl+V')

helpmenu.add_command(label="About EasyPhotoEditor       ", command=about, image=about_icon, compound=tk.LEFT)
helpmenu.add_command(label="Check for updates           ", command=update, image=updates_icon, compound=tk.LEFT)
helpmenu.add_command(label="Report Bugs to Dev           ", command=report, image=bug_icon, compound=tk.LEFT)


filemenu.bind_all("<Control o>")

#adding theme

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
	thememenu.add_radiobutton(label=i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command=changeTheme)
	count = count + 1


#cascading all menus
menubar.add_cascade(label="File", menu=filemenu)
# menubar.add_cascade(label="Edit", menu=editmenu)
menubar.add_cascade(label="Theme", menu=thememenu)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

#declaring frames

frame = LabelFrame(root,padx=20, pady=20, height=677, width= 944)
frame.place(x=5,y=3)

frameOpenFile = LabelFrame(root, padx=1, pady=1)
frameOpenFile.place(x=950,y=2)

frameTools = LabelFrame(root, padx=7, pady=0)
frameTools.place(x=950,y=116)

frameShare = LabelFrame(root, pady=1)
frameShare.place(x=950,y=560)

framesiteShare = LabelFrame(root, pady=1)
framesiteShare.place(x=950,y=620)

OpenImageButton = ttk.Button(frameOpenFile, text="Click here to open an image ",image=open_icon, compound=tk.TOP, command= file_open,width=62)
OpenImageButton.pack(ipadx=5,ipady=2, padx=5, pady=5)


#Editing Tools Segment

tabControl = ttk.Notebook(frameTools)

crop = ttk.Frame(tabControl)
tabControl.add(crop, text="      Crop      ", image=crop_icon, compound=tk.TOP)
tabControl.grid(row=0,column=0)

rotate = ttk.Frame(tabControl)
tabControl.add(rotate, text="      Rotate      ", image=rotate_icon, compound=tk.TOP)
tabControl.grid(row=0,column=1)

filters = ttk.Frame(tabControl)
tabControl.add(filters, text="      Filters      ", image=effects_icon, compound=tk.TOP)
tabControl.grid(row=0,column=2)

addtext = ttk.Frame(tabControl)
tabControl.add(addtext, text="    Add Text    ", image=text_icon, compound=tk.TOP)
tabControl.grid(row=0,column=3)

# draw = ttk.Frame(tabControl)
# tabControl.add(draw, text="    Draw    ", image=draw_icon, compound=tk.TOP)
# tabControl.grid(row=0,column=3)

adjust = ttk.Frame(tabControl)
tabControl.add(adjust, text="       Adjust       ", image=adjust_icon, compound=tk.TOP)
tabControl.grid(row=0,column=4)


#CROP SEGMENT

ep = Image.open("icons/Test.jpg")
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
emboss = ttk.Button(filters, text="EMBOSS\n", compound=tk.TOP,command=emboss)
emboss.place(x=270,y=232)

ResetButton = ttk.Button(filters, text="Reset", compound=tk.TOP, command=reset_now, image=reset_icon)
ResetButton.pack(ipadx=2,ipady=3, padx=0, pady=5, side=BOTTOM)


#AddText Segment

fontLabel = ttk.Label(addtext,text="                   Font Family")
fontLabel.place(x=95,y=12)
font = ttk.Combobox(addtext,values=('Bahnschrift','BisonBold','Calibri Bold Italic','Calibri Bold','Calibri Italic','Calibri Regular','CascadiaCode','ComicSans','FranklinGothic','Genuine','Impact','Juniorprince Regular','Krinkes Regular','SiyamRupali','TimesNewRoman','Unispace Bold','Unispace Bold Italic','Unispace Italic','Unispace Regular','ValentLovey'), width=35,justify=CENTER,state='readonly')
font.set("Choose a font family")
font.bind("<<ComboboxSelected>>",fontClicked)
font.place(x=98,y=33,height=21,width=180)

fontColorLabel = ttk.Label(addtext,text="                    Font Color")
fontColorLabel.place(x=95,y=71)
fontColor = ttk.Combobox(addtext,values=('Violet','Yellow','Blue','Green','Orange','Black','Brown','White','Indigo','Lime','Gray'), width=35,justify=CENTER,state='readonly')
fontColor.set("Choose a font color")
fontColor.bind("<<ComboboxSelected>>",fontColorClicked)
fontColor.place(x=98,y=92,height=21,width=180)

fontSizeLabel = ttk.Label(addtext,text="                      Font Size")
fontSizeLabel.place(x=95,y=130)
fontSize = ttk.Combobox(addtext,values=('8','9','10','11','12','14','16','18','20','22','24','26','28','36','48','72','94','130'), width=35,justify=CENTER,state='readonly')
fontSize.set("Choose a Font Size")
fontSize.bind("<<ComboboxSelected>>",fontSizeClicked)
fontSize.place(x=98,y=150,height=21,width=180)

MainTextLabel = ttk.Label(addtext,text="                   Adding Text")
MainTextLabel.place(x=95,y=185)

txtLabel = tk.Entry(addtext, width=30,borderwidth=3)
txtLabel.place(x=95,y=205,height=28,width=187)
txtLabel.insert(0, "Enter your Text here")
txtLabel.configure(state=DISABLED)

def on_click(event):
		    txtLabel.configure(state=NORMAL)
		    txtLabel.delete(0, END)
		    txtLabel.unbind('<Button-1>', on_click_id_tX)

on_click_id_tX = txtLabel.bind('<Button-1>', on_click)

TextPosLabel = ttk.Label(addtext,text="        Adjust Text Position (X,Y)")
TextPosLabel.place(x=95,y=243)

txtX1Label = tk.Entry(addtext, width=30,borderwidth=3)
txtX1Label.place(x=95,y=263,height=28,width=187)
txtX1Label.insert(0, "Enter X value here")
txtX1Label.configure(state=DISABLED)

def on_click(event):
		    txtX1Label.configure(state=NORMAL)
		    txtX1Label.delete(0, END)
		    txtX1Label.unbind('<Button-1>', on_click_id_tX1)

on_click_id_tX1 = txtX1Label.bind('<Button-1>', on_click)

txtY1Label = tk.Entry(addtext, width=30,borderwidth=3)
txtY1Label.place(x=95,y=295,height=28,width=187)
txtY1Label.insert(0, "Enter Y value here")
txtY1Label.configure(state=DISABLED)

def on_click(event):
		    txtY1Label.configure(state=NORMAL)
		    txtY1Label.delete(0, END)
		    txtY1Label.unbind('<Button-1>', on_click_id_tY1)

on_click_id_tY1 = txtY1Label.bind('<Button-1>', on_click)

addtextButton = ttk.Button(addtext, text="Add Text", compound=tk.LEFT, image=text_icon2, command=addtextnow)
addtextButton.place(x=137,y=335)

# ResetButton = ttk.Button(addtext, text="Reset", compound=tk.LEFT, command=reset_now, image=reset_icon2)
# ResetButton.place(x=200,y=336)



#Adjust Segment

brightnessLabel = ttk.Label(adjust,text="                       Brightness")
brightnessLabel.place(x=8,y=40)
ApplyBrButton = ttk.Button(adjust, image=adapply_icon, command=br)
ApplyBrButton.place(x=155,y=32)
minusLabel = ttk.Label(adjust,text="-")
minusLabel.place(x=14,y=62)
plusLabel = ttk.Label(adjust,text="+")
plusLabel.place(x=182,y=62)
zeroLabel = ttk.Label(adjust,text="0")
zeroLabel.place(x=100,y=85)
brightness = ttk.Scale(adjust, from_=0, to=10, length=150, orient=HORIZONTAL)
brightness.place(x=30,y=60)
brightness.set(5)




ContrastLabel = ttk.Label(adjust,text="                        Contrast")
ContrastLabel.place(x=190,y=40)
ApplyConButton = ttk.Button(adjust, image=adapply_icon, command=con)
ApplyConButton.place(x=340,y=32)
minusLabel = ttk.Label(adjust,text="-")
minusLabel.place(x=203,y=62)
plusLabel = ttk.Label(adjust,text="+")
plusLabel.place(x=368,y=62)
zeroLabel = ttk.Label(adjust,text="0")
zeroLabel.place(x=285,y=85)
contrast = ttk.Scale(adjust, from_=0, to=10, length=150, orient=HORIZONTAL)
contrast.place(x=215,y=60)
contrast.set(5)



ShadowLabel = ttk.Label(adjust,text="                         Shadow")
ShadowLabel.place(x=8,y=125)
ApplyConButton = ttk.Button(adjust, image=adapply_icon, command=shad)
ApplyConButton.place(x=155,y=120)
minusLabel = ttk.Label(adjust,text="-")
minusLabel.place(x=14,y=147)
plusLabel = ttk.Label(adjust,text="+")
plusLabel.place(x=182,y=147)
zeroLabel = ttk.Label(adjust,text="0")
zeroLabel.place(x=100,y=170)
shadow = ttk.Scale(adjust, from_=0, to=10, length=150, orient=HORIZONTAL)
shadow.place(x=30,y=145)
shadow.set(5)



SaturationLabel = ttk.Label(adjust,text="                         Saturation")
SaturationLabel.place(x=190,y=125)
ApplySatButton = ttk.Button(adjust, image=adapply_icon, command=sat)
ApplySatButton.place(x=340,y=120)
minusLabel = ttk.Label(adjust,text="-")
minusLabel.place(x=203,y=147)
plusLabel = ttk.Label(adjust,text="+")
plusLabel.place(x=368,y=147)
zeroLabel = ttk.Label(adjust,text="0")
zeroLabel.place(x=285,y=170)
saturation = ttk.Scale(adjust, from_=0, to=10, length=150, orient=HORIZONTAL)
saturation.place(x=215,y=145)
saturation.set(5)



SharpnessLabel = ttk.Label(adjust,text="                         Sharpness")
SharpnessLabel.place(x=8,y=210)
ApplySharpButton = ttk.Button(adjust, image=adapply_icon, command=sharp)
ApplySharpButton.place(x=155,y=205)
minusLabel = ttk.Label(adjust,text="-")
minusLabel.place(x=14,y=232)
plusLabel = ttk.Label(adjust,text="+")
plusLabel.place(x=182,y=232)
zeroLabel = ttk.Label(adjust,text="                       0")
zeroLabel.place(x=32,y=255)
sharpness = ttk.Scale(adjust, from_=0, to=10, length=150, orient=HORIZONTAL)
sharpness.place(x=30,y=230)
sharpness.set(5)



EnhancementLabel = ttk.Label(adjust,text="                       Enhancement")
EnhancementLabel.place(x=190,y=210)
ApplyEnButton = ttk.Button(adjust, image=adapply_icon, command=en)
ApplyEnButton.place(x=340,y=205)
minusLabel = ttk.Label(adjust,text="-")
minusLabel.place(x=203,y=232)
plusLabel = ttk.Label(adjust,text="+")
plusLabel.place(x=368,y=232)
zeroLabel = ttk.Label(adjust,text="0")
zeroLabel.place(x=217,y=255)
enhancement = ttk.Scale(adjust, from_=0, to=10, length=150, orient=HORIZONTAL)
enhancement.place(x=215,y=230)

ResetButton = ttk.Button(adjust, text="Reset", compound=tk.LEFT, command=reset_now, image=reset_icon2)
ResetButton.place(x=140,y=330)


#Share Buttons Segment

shareLabel = Label(frameShare, text="PLEASE SAVE THE IMAGE FIRST &  \n        UPLOAD AND SHARE THE IMAGE BY CLICKING BELOW !        ", image=share_icon, compound=tk.LEFT)
shareLabel.pack(side=TOP)
fbButton = ttk.Button(framesiteShare, text="Facebook",image=fb_icon, compound=tk.TOP, command=fb)
fbButton.pack(side=LEFT,padx=2)
igButton = ttk.Button(framesiteShare, text="Instagram",image=insta_icon, compound=tk.TOP, command=ig)
igButton.pack(side=LEFT,padx=2)
twitterButton = ttk.Button(framesiteShare, text="Twitter",image=twitter_icon, compound=tk.TOP, command=tw)
twitterButton.pack(side=LEFT,padx=2)
gdriveButton = ttk.Button(framesiteShare, text="G Drive",image=gdrive_icon, compound=tk.TOP, command=gdr)
gdriveButton.pack(side=LEFT,padx=2)
gmailButton = ttk.Button(framesiteShare, text="Gmail",image=mail_icon, compound=tk.TOP, command=gm)
gmailButton.pack(side=LEFT,padx=2)

root.bind("<Control o>",file_open)
root.bind("<Control s>",save)
root.bind("<Alt s>",save_as)
root.bind("<Control r>",rename)
root.bind("<Control q>",quit)

root.mainloop()