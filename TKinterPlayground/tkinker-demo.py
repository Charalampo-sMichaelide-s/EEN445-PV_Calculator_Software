from tkinter import *
# from tkinter.ttk import *
import tkintermapview

## Widgets = GUI elements--> buttons, textboxes, labels, images
## Window = serves as a container to hold or contain these widgets
## Label = an area widget that holds text and/or an image within a window
## Button = you click it, it does stuff
## Entry = textbox that accepts a single line of user input
## Radio Button = like checkbox, but can only select one from a group
## Listbox = a listing of selectable text items within its own container

window = Tk() ## Instantiate an instance of a window - Window constructor
window.geometry("600x600") ## Change the size of the window 420x420
window.title("P/V Calculator DEMO") ## Change the title of the window

icon = PhotoImage(file='./Images/solar-panel-clipart.png') 
window.iconphoto(True, icon)
window.config(background="#D9EDBF") ## Any miscellanious changes to window go here

map_widget = tkintermapview.TkinterMapView(window, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)


label = Label(window, 
              text="Hello World", 
              font=('Arial', 40, 'bold'), 
              fg='#28282B',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              ) ## Instanciate a label. Any label configurations go here
label.pack() ## Add label to window
# label.place(x=100,y=100) ## Add label to coordinates off window

count = 0
## Callback function for the button
def click(): 
    global count
    count+=1
    print(f"You clicked the button {count} times")
checkmark = PhotoImage(file='./Images/checkmark.png')
button = Button(window, 
                text='Click me!',
                command=click,
                font=('Comic Sans', 20),
                fg='#28282B',
                bg="#A1C398",
                activeforeground='#C6EBF9',
                activebackground='#C6EBC5',
                state=ACTIVE,
                # image=checkmark,
                # compound='bottom'
                )
button.pack()

def submit():
    azimuth = entry.get()
    print(f'The azimuth angle given is {azimuth}')
    entry.config(state=DISABLED)
    
def delete():
    entry.delete(0,END)

entry = Entry(window,
              font=('Arial', 25),
              fg='green',
              show='*')
entry.insert(0, 'Spongebob')
entry.pack(side=LEFT)


entry_submit = Button(window, text='Submit', command=submit, )
entry_submit.pack(side=RIGHT)
entry_delete = Button(window, text='Delete', command=delete)
entry_delete.pack(side=RIGHT)

x = IntVar() 
y = StringVar()
def display():
    if(x.get() == 1):
        print("You agree")
    else:
        print("You don't agree")
checkbutton = Checkbutton(window, text='asdf', variable=x, onvalue=1, offvalue=0, command=display, font=('Arial', 20))
checkbutton.pack()

food = ["pizza", "hamburger", "hotdog"]
x = IntVar()
for index in range(len(food)):
    radiobutton = Radiobutton(window, 
                              text=food[index], ## Adds text to radio buttons 
                              variable=x, ## Groups radio buttons together if they share the same variable
                              value=index, ## Assigns each radio button a different value
                              padx=25,
                              font=("Impact", 20)
                            )
    radiobutton.pack(anchor=W)

#### Main ####
window.mainloop() ## Place window on computer screen and listen for events