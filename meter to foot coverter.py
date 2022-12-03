from tkinter import *
root = Tk()
root.title('converter')

#display
display = Entry(root , width=20 ,  borderwidth=5 ,font=8  )
meters=0
display.grid(row=0 , columnspan=3 )
#button funtions
def button_click(number):
    last = display.get()
    display.delete(0,END)
    display.insert(0,last + str(number))

def button_clear():
    display.delete(0,END)

def feet():
    global foot
    foot = display.get()
    display.delete(0, END)
    display.insert(0, foot + 'feet')
def meter():
    global  meters
    meters = display.get()
    display.delete(0, END)
    display.insert(0,meters + 'm')

def convert_feet():
    display.delete(0, END)
    display.insert(0,str(float(meters) *3.280) + ' feet' )

def convert_meter():
    display.delete(0, END)
    display.insert(0, str( float(foot)/3.280  ) + 'm')


#button declarations
button0 = Button(root, text='0', padx=37, pady=10, bg='#308be6', command=lambda: button_click(0)  )
button1 = Button(root, text='1', padx=37, pady=10, bg='#308be6',command=lambda: button_click(1)  )
button2 = Button(root, text='2', padx=38, pady=10, bg='#308be6',command=lambda: button_click(2)  )
button3 = Button(root, text='3', padx=38, pady=10, bg='#308be6',command=lambda: button_click(3)  )
button4 = Button(root, text='4', padx=37, pady=10, bg='#308be6', command=lambda: button_click(4) )
button5 = Button(root, text='5', padx=38, pady=10, bg='#308be6',command=lambda: button_click(5)  )
button6 = Button(root, text='6', padx=38, pady=10, bg='#308be6',command=lambda: button_click(6)  )
button7 = Button(root, text='7', padx=37, pady=10, bg='#308be6', command=lambda: button_click(7) )
button8 = Button(root, text='8', padx=38, pady=10, bg='#308be6',command=lambda: button_click(8)  )
button9 = Button(root, text='9', padx=38, pady=10, bg='#308be6', command=lambda: button_click(9) )
button_feet = Button(root, text='feet', padx=30, pady=10, bg='#c0d7ed',command=feet  )
button_convert_f = Button(root, text='To feet', padx=25, pady=10, bg='#283f57',command=convert_feet  )
button_m = Button(root, text='m', padx=37, pady=10, bg='#c0d7ed',command=meter  )
button_convert_m = Button(root, text='To meters', padx=14, pady=10, bg='#283f57',command= convert_meter )
button_clear = Button(root, text='clear', padx=28, pady=10, bg='#283f57',command=button_clear  )

#buttons display on window
button7.grid(row=1 , column=0)
button8.grid(row=1 , column=1)
button9.grid(row=1 , column=2)
button4.grid(row=2 , column=0)
button5.grid(row=2 , column=1)
button6.grid(row=2 , column=2)
button1.grid(row=3 , column=0)
button2.grid(row=3 , column=1)
button3.grid(row=3 , column=2)
button0.grid(row=4, column=0)
button_m.grid(row=4, column=1)
button_feet.grid(row=4, column=2)
button_convert_m.grid(row=5, column=2)
button_clear.grid(row=5, column=0)
button_convert_f.grid(row=5, column=1)



root.mainloop()