from tkinter import *
import socket
import sys













root1 = Tk()
root1.title("Localization Machine")
root1.geometry("700x500")
root = Frame(root1)
root.pack(side=LEFT,fill=X)
section1 = Frame(root1)
section1.pack(side=LEFT,fill=X)



#foo=scrollTxtArea(section1)
foo = Text(section1,height=20,width=40)
foo.pack(fill=Y)
foo.insert(END,"Localization Machine Booted"+"\n")





def UploadExhibit1():
    root.fileName = filedialog.askopenfilename(filetypes = (("Sound Files",".wav"),("All Files","*.*") ))
    print(root.fileName)
    foo.insert(END,"File is uploaded from"+root.fileName+"\n")




def UploadExhibit2():
    root.fileName = filedialog.askopenfilename(filetypes = (("Sound Files",".wav"),("All Files","*.*") ))
    print(root.fileName)
    foo.insert(END,"File is uploaded from"+root.fileName+"\n")




def UploadExhibit3():
    root.fileName = filedialog.askopenfilename(filetypes = (("Sound Files",".wav"),("All Files","*.*") ))
    print(root.fileName)
    foo.insert(END,"File is uploaded from"+root.fileName+"\n")



def UploadExhibit4():
    root.fileName = filedialog.askopenfilename(filetypes = (("Sound Files",".wav"),("All Files","*.*") ))
    print(root.fileName)
    foo.insert(END,"File is uploaded from"+root.fileName+"\n")






def UploadExhibit5():
    root.fileName = filedialog.askopenfilename(filetypes = (("Sound Files",".wav"),("All Files","*.*") ))
    print(root.fileName)
    foo.insert(END,"File is uploaded from"+root.fileName+"\n")




def UploadExhibit6():
    root.fileName = filedialog.askopenfilename(filetypes = (("Sound Files",".wav"),("All Files","*.*") ))
    print(root.fileName)
    foo.insert(END,"File is uploaded from"+root.fileName+"\n")




def UploadExhibit7():
    root.fileName = filedialog.askopenfilename(filetypes = (("Sound Files",".wav"),("All Files","*.*") ))
    print(root.fileName)
    foo.insert(END,"File is uploaded from"+root.fileName+"\n")



def UploadExhibit8():
    root.fileName = filedialog.askopenfilename(filetypes = (("Sound Files",".wav"),("All Files","*.*") ))
    print(root.fileName)
    foo.insert(END,"File is uploaded from"+root.fileName+"\n")




def UploadExhibit9():
    root.fileName = filedialog.askopenfilename(filetypes = (("Sound Files",".wav"),("All Files","*.*") ))
    print(root.fileName)
    foo.insert(END,"File is uploaded from"+root.fileName+"\n")




def UploadExhibit10():
    root.fileName = filedialog.askopenfilename(filetypes = (("Sound Files",".wav"),("All Files","*.*") ))
    print(root.fileName)
    foo.insert(END,"File is uploaded from"+root.fileName+"\n")




def UploadExhibit11():
    root.fileName = filedialog.askopenfilename(filetypes = (("Sound Files",".wav"),("All Files","*.*") ))
    print(root.fileName)
    foo.insert(END,"File is uploaded from"+root.fileName+"\n")



def UploadExhibit12():
    root.fileName = filedialog.askopenfilename(filetypes = (("Sound Files",".wav"),("All Files","*.*") ))
    print(root.fileName)
    foo.insert(END,"File is uploaded from"+root.fileName+"\n")






def UploadExhibit13():
    root.fileName = filedialog.askopenfilename(filetypes = (("Sound Files",".wav"),("All Files","*.*") ))
    print(root.fileName)
    foo.insert(END,"File is uploaded from"+root.fileName+"\n")




def UploadExhibit14():
    root.fileName = filedialog.askopenfilename(filetypes = (("Sound Files",".wav"),("All Files","*.*") ))
    print(root.fileName)
    foo.insert(END,"File is uploaded from"+root.fileName+"\n")




def UploadExhibit15():
    root.fileName = filedialog.askopenfilename(filetypes = (("Sound Files",".wav"),("All Files","*.*") ))
    print(root.fileName)
    foo.insert(END,"File is uploaded from"+root.fileName+"\n")







































#Server Code
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
foo.insert(END,"Starting Server on port 1000"+  "\n")
sock.bind(server_address)


#Running Server Waiting for client to connect and communicate

#while True:
	#payload, client_address = sock.recvfrom(1)
	#print("Echoing data back to " + str(client_address))
	#sent = sock.sendto(payload, client_address)



## Server code end here




#UI stuff
index = Label(root,text="Number")
index.grid(row=1,column=0)
exhibit = Label(root,text="Exhibit Name")
exhibit.grid(row=1,column=1)
filename = Label(root,text="Audio File")
filename.grid(row=1,column=2)
status = Label(root,text="Status")
status.grid(row=1,column=3)
i1=Label(root,text="1")
i2=Label(root,text="2")
i3=Label(root,text="3")
i4=Label(root,text="4")
i5=Label(root,text="5")
i6=Label(root,text="6")
i7=Label(root,text="7")
i8=Label(root,text="8")
i9=Label(root,text="9")
i10=Label(root,text="10")
i11=Label(root,text="11")
i12=Label(root,text="12")
i13=Label(root,text="13")
i14=Label(root,text="14")
i15=Label(root,text="15")
i1.grid(row=2,column=0)
i2.grid(row=3,column=0)
i3.grid(row=4,column=0)
i4.grid(row=5,column=0)
i5.grid(row=6,column=0)
i6.grid(row=7,column=0)
i7.grid(row=8,column=0)
i8.grid(row=9,column=0)
i9.grid(row=10,column=0)
i10.grid(row=11,column=0)
i11.grid(row=12,column=0)
i12.grid(row=13,column=0)
i13.grid(row=14,column=0)
i14.grid(row=15,column=0)
i15.grid(row=16,column=0)

name1 = Label(root,text="School Lunch")
name2 = Label(root,text="Holidays")
name3 = Label(root,text="Restaurants")
name4 = Label(root,text="Formals")
name5 = Label(root,text="Events")
name6 = Label(root,text="Import")
name7 = Label(root,text="Staples")
name8 = Label(root,text="Commissary")
name9 = Label(root,text="Commissary")
name10 = Label(root,text="Construction")
name11 = Label(root,text="Trouble")
name12 = Label(root,text="Meals to go")
name13 = Label(root,text="Cultural")
name14 = Label(root,text="Panama")
name15 = Label(root,text="Unique")


#UI stuff
name1.grid(row=2,column=1)
name2.grid(row=3,column=1)
name3.grid(row=4,column=1)
name4.grid(row=5,column=1)
name5.grid(row=6,column=1)
name6.grid(row=7,column=1)
name7.grid(row=8,column=1)
name8.grid(row=9,column=1)
name9.grid(row=10,column=1)
name10.grid(row=11,column=1)
name11.grid(row=12,column=1)
name12.grid(row=13,column=1)
name13.grid(row=14,column=1)
name14.grid(row=15,column=1)
name15.grid(row=16,column=1)


#Buttons to add Audios- Add Functions to upload
b1 = Button(root,text="Select Audio",command=UploadExhibit1)
b2 = Button(root,text="Select Audio",command=UploadExhibit2)
b3 = Button(root,text="Select Audio",command=UploadExhibit3)
b4 = Button(root,text="Select Audio",command=UploadExhibit4)
b5 = Button(root,text="Select Audio",command=UploadExhibit5)
b6 = Button(root,text="Select Audio",command=UploadExhibit6)
b7 = Button(root,text="Select Audio",command=UploadExhibit7)
b8 = Button(root,text="Select Audio",command=UploadExhibit8)
b9 = Button(root,text="Select Audio",command=UploadExhibit9)
b10 = Button(root,text="Select Audio",command=UploadExhibit10)
b11 = Button(root,text="Select Audio",command=UploadExhibit11)
b12 = Button(root,text="Select Audio",command=UploadExhibit12)
b13 = Button(root,text="Select Audio",command=UploadExhibit13)
b14 = Button(root,text="Select Audio",command=UploadExhibit14)
b15= Button(root,text="Select Audio",command=UploadExhibit15)

#UI placement
b1.grid(row=2,column=2)
b2.grid(row=3,column=2)
b3.grid(row=4,column=2)
b4.grid(row=5,column=2)
b5.grid(row=6,column=2)
b6.grid(row=7,column=2)
b7.grid(row=8,column=2)
b8.grid(row=9,column=2)
b9.grid(row=10,column=2)
b10.grid(row=11,column=2)
b11.grid(row=12,column=2)
b12.grid(row=13,column=2)
b13.grid(row=14,column=2)
b14.grid(row=15,column=2)
b15.grid(row=16,column=2)


#Main Functioanlity 
run = Button(root,text="RUN",bg="green",fg="black")
run.grid(row=18,column=0)

stop = Button(root,text="STOP",bg="red",fg="black")
stop.grid(row=18,column=1)

clear = Button(root,text="CLEAR")
clear.grid(row=18,column=2)

clearall = Button(root,text="CLEAR ALL")
clearall.grid(row=18,column=3)


root.mainloop()
