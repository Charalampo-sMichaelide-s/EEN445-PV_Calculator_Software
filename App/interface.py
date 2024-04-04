from tkinter import *
from tkinter.ttk import *
from PIL import Image
import datetime
import re
import tkintermapview

window = Tk()   ## Instantiate an instance of a window - Window constructor
window.geometry(f"{700}x{700}")    ## Change the size of the window
window.title("EEN445 - P/V Calculator")  ## Change the title of the window

icon = PhotoImage(file='./Images/solar-clipart.png') 
window.iconphoto(True, icon)
window.config(background="#D9EDBF")

## TODO about_menu
def about_menu():
    pass
## TODO help_menu
def help_menu():
    pass

menu_bar = Menu(window)
window.config(menu=menu_bar)
menu_bar.add_command(label="About", command=help_menu)
menu_bar.add_command(label="Help", command=help_menu)

map_widget = tkintermapview.TkinterMapView(window, width=700,height=300, corner_radius=0)
map_widget.set_position(34.9220, 32.8794)
# map_widget.set_address("Corner Athinon and Nikola Xiouta, Limassol, Cyprus")
map_widget.set_zoom(9)
map_widget.pack(anchor=S)

pv_marker_exists = False
marker_coords = None

def marker_pin(coords):
    image = Image.open("./Images/pv-map-marker.png")
    width, height = 64, 64
    resized_image = image.resize((width, height))
    resized_image.save("./Images/pv-map-marker.png")
    
    dt = datetime.datetime.now()
    
    global pv_marker_exists
    global marker_coords
    
    if pv_marker_exists == True:
        map_widget.delete_all_marker()
        pv_marker_exists = False
        
    marker = PhotoImage(file="./Images/pv-map-marker.png")
    map_widget.set_marker(coords[0], coords[1], text=f"{dt}", icon=marker)
    pv_marker_exists = True
    print(f"{dt}: Marker pinned on coordinates {coords}.")
    marker_coords = coords

def marker_remove():
    map_widget.delete_all_marker()
    
map_widget.add_left_click_map_command(marker_pin)
map_widget.add_right_click_menu_command(label="Clear markers",
                                        command=marker_remove)

options = Frame(window)
options.pack()

coords_label = Label(options, 
                     text="Coordinates: ",
                     font=('Arial', 12),
                    )
coords_label.grid(row=0, 
                  column=0,
                  padx=(5,5),
                  pady=(5,5)
                  )
coordinates = Entry(options,
                    font=('Arial'),
                    justify="center",
                    validate="focus",
                    state="readonly",
                    )
coordinates.grid(row=0, 
                 column=1,
                 padx=(5,5),
                 pady=(5,5))

address_label = Label(options, 
                     text="Address: ",
                     font=('Arial', 12),
                      )
address_label.grid(row=0, 
                   column=3,
                   padx=(5,5),
                   pady=(5,5)
                   )
address = Entry(options, 
                font=('Arial'), 
                justify="center", 
                validate="focus",                    
                )
address.grid(row=0, 
             column=4
             )

azimuth_label = Label(options,
                      text="Azimuth [°]:",
                      font=('Arial', 12)
                      )
azimuth_label.grid(row=1, 
                   column=0
                   )
# azimuth_angle = IntVar()
# azimuth_angle.set("120")
azimuth = Entry(options,
                font=('Arial'),
                justify="center",
                validate="focus",
                # textvariable=azimuth_angle.get(),
                # state="readonly",
                )
azimuth.config(state="readonly")
azimuth.grid(row=1, column=1)

slope_label = Label(options,
                      text="Slope [°]:",
                      font=('Arial', 12)
                      )
slope_label.grid(row=1, 
                   column=3
                   )
# azimuth_angle = IntVar()
# azimuth_angle.set("120")
slope = Entry(options,
                font=('Arial'),
                justify="center",
                validate="focus",
                # textvariable=azimuth_angle.get(),
                # state="readonly",
                )
# slope.config(state="readonly")
slope.grid(row=1, column=4)

results = Frame(window)
results.pack(pady=(50,0))

results_label = Label(results, 
                      text=f"The optional angle for the P/V panels \nto not shadow each other is: ", 
                      font=("Arial", 20, "bold"),
                      )
results_label.pack()

    
    
    

# With the label argument you set the text inside the menu, and if pass_coords is True, the clicked coordinates will be passed to the command function as a tuple.


#### Main ####
window.mainloop()   ## Place window on computer screen and listen for events