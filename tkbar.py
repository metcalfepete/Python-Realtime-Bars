from tkinter import *
from random import randint

def timerupdate():
    get_values()
    resize_rect() 
    root.after(5000, timerupdate)

def get_values():
    # Add you RaspPi data update calls here
    # Use random values for testing
    for i in range(numchart):
        bvalue[i] = randint(0,100)

def resize_rect():  # update bar sizes and text
    for i in range(numchart):
        c.itemconfig(text[i],text= btext[i] + str(bvalue[i]) + units[i] )
        x0, y0, x1, y1 = c.coords(bar[i])
        y0 = (c_height - (2*c_margin))*((hrange[i] - bvalue[i])/hrange[i])+ c_margin
        c.coords(bar[i],x0,y0, x1,y1)

# Define the canvas size 
c_width = 900
c_height = 400
c_margin = 20 # top and bottom margin
b_space = 20 # space between bars

root = Tk()
root.geometry(str(c_width) + "x" + str(c_height) + "+100+100")
root.title("Rasp Pi Real Time Bar Graph")

# Adjust the arrays definitions to match the number of charts
numchart = 4
bcols = ["red","blue","purple","yellow"]
btext = ["TI01 - Inside Temp : ","TI02 - Outside Temp : ","PT04 - Atmos Pressure : ","HI04 - Humidity :"]
units = [" °C", " °C", " kPa"," %"]
hrange = [100,100,150,100]
bvalue = [0,0,0,0] # There are the real time values (that come from a Rasp Pi)



c = Canvas(root, width=c_width, height=c_height)
c.pack()

# create the bar and text objects
bar = ['' for i in range(numchart)]
text = ['' for i in range(numchart)]
for i in range(numchart): 
	barwidth = (c_width - c_margin - (numchart-1)*b_space)/4
	x0 = c_margin + i*(barwidth+b_space) - (b_space/2)
	y0 = c_height - c_margin - 3 
	x1 = x0+ barwidth
	y1 = c_height -  c_margin 
	bar[i] = c.create_rectangle(x0, y0, x1, y1, fill=bcols[i])
	text[i] = c.create_text(x0, c_height - c_margin/2, text=btext[i], anchor = "w",font='Arial 9 bold')

c.create_line(0, (c_height - c_margin), c_width, (c_height - c_margin))

root.after(2000, timerupdate)
root.mainloop()
