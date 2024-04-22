# import os     ## Uncomment to use with resource_path()
from tkinter import *
# from tkinter.ttk import *
from calculator import *
import datetime
import re
import tkintermapview

### For making an .exe instance of the project, uncomment the function resource_path() and extract all the images from the Images folder to project's root folder. 
## Then set the image paths throughout the interface.py like this: "PhotoImage(file=resource_path("solar-clipart.png"))
### Then run "auto-py-to-exe" and include the project folder during its use. 
#
# def resource_path(relative_path):
#     try:
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")

#     return os.path.join(base_path, relative_path)

## Here goes the UI of the app.

##########################
####      Window      ####
##########################

window = Tk()   ## Instantiate an instance of a window - Window constructor
window.geometry(f"{750}x{525}")    ## Change the size of the window
window.title("EEN445 - P/V Calculator")  ## Change the title of the window
window.resizable(0,0) ## Disables maximize window action

icon = PhotoImage(file="./Images/solar-clipart.png") 
window.iconphoto(True, icon)
window.config(background="#D9EDBF")


####################################

##########################
####     Menu Bar     ####
##########################

cut_logo = PhotoImage(file="./Images/cut-logo.png")

def about_menu():
    about_menu = Toplevel()
    about_menu.title("Developed by..")
    about_menu.geometry(f"{300}x{300}")
    about_menu.resizable(0,0)
    
    
    university = Label(about_menu, 
                       image=cut_logo,
                       justify=CENTER
                       )
    university.pack()
    
    about_label = Label(about_menu, 
                        text="""
Lesson: EEI445 - Renewable Energy Sources

Students: 
    Emmanouil Oikonomou -23759-
    Charalambos Michaelides -19652-
    Charalambos Kambourides -20081-             
                             """,
                        # justify=LEFT,
                        anchor=CENTER,
                        font=("Arial", 10)
                        
                        )
    about_label.pack()

    copyright_label = Label(about_menu,
                        text="© 2024. All rights reserved.",
                        anchor=CENTER)
    copyright_label.pack()
 
menu_bar = Menu(window)
window.config(menu=menu_bar)
menu_bar.add_command(label="About", command=about_menu)

####################################

map_widget = tkintermapview.TkinterMapView(window, width=750,height=300, corner_radius=0)
map_widget.set_position(34.9220, 32.8794)
map_widget.set_zoom(9)
map_widget.pack(anchor=S)

## Google normal
# map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22) 
## Google satellite - Beware of the CPU overhead!!!
# map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22) 

##########################
#### Global Variables ####
##########################

pv_marker_exists = False
marker_coords = None
marker = PhotoImage(file="./Images/pv-map-marker.png")
address_input = StringVar()
slope_input = StringVar()
length_input = StringVar()
slope_is_valid = False
length_is_valid = False
results_description = StringVar()
# full_address = StringVar()

####################################

##########################
####    Map Widget    ####
##########################

def marker_pin(coords):
    global pv_marker_exists
    global marker_coords
    global marker
    global results_description
    global full_address
    
    dt = datetime.datetime.now()

    if pv_marker_exists == True:
        map_widget.delete_all_marker()
        pv_marker_exists = False
        
    map_widget.set_marker(coords[0], coords[1], text=f"{dt.strftime('%Y-%m-%d %H:%M:%S')}", icon=marker)
    pv_marker_exists = True
    print(f"\n{dt.strftime('%Y-%m-%d %H:%M:%S')}: Marker pinned using map widget @{coords}.")
    marker_coords = coords
    
    address.delete(0, END)
    coordinates.config(foreground="black")
    coordinates.config(state="normal")
    coordinates.delete(0, END)
    coordinates.insert(0, f"{coords}")
    coordinates.config(state="readonly")
    
    results_description.set("")
    results_label.config(text="")
    
    # adr = map_widget.convert_coordinates_to_address(coords[0],coords[1])
    # full_address.set(adr)
    # address.insert(full_address)
            
def marker_remove():
    map_widget.delete_all_marker()
    coordinates.config(state="normal")
    coordinates.delete(0, END)
    coordinates.config(state="readonly")
    address.delete(0, END)
        
map_widget.add_left_click_map_command(marker_pin)
map_widget.add_right_click_menu_command(label="Clear all markers",
                                        command=marker_remove)

####################################

##########################
####  Parameter Pane  ####
##########################
options = Frame(window)
options.pack()

coords_label = Label(options, 
                     text="Coordinates: ",
                     font=('Arial', 12),
                    )
coords_label.grid(row=0, 
                  column=0,
                  padx=(5,0),
                  pady=(5,5)
                  )

coordinates = Entry(options,
                    font=('Arial'),
                    justify="center",
                    )
coordinates.config(state="readonly")
coordinates.grid(row=0, 
                 column=1,
                 padx=(2,5),
                 pady=(5,5),
                 )
    
address_label = Label(options, 
                     text="Address: ",
                     font=('Arial', 12),
                      )
address_label.grid(row=0, 
                   column=3,
                   padx=(5,0),
                   pady=(5,5)
                   )
address = Entry(options, 
                font=('Arial'), 
                justify="center", 
                textvariable=address_input                 
                )

def set_address_callback(var, index, mode):
    global marker
    global marker_coords
    
    dt = datetime.datetime.now()
    
    try:
        if not address.get() == "":
            address_marker = map_widget.set_address(f"{address.get()}", marker=True, icon=marker)
            marker_coords = address_marker.position
            map_widget.delete_all_marker()
            map_widget.set_marker(marker_coords[0], marker_coords[1], text=f"{dt.strftime('%Y-%m-%d %H:%M:%S')}", icon=marker)
            
            coordinates.config(foreground="black")
            coordinates.config(state="normal")
            coordinates.delete(0, END)
            coordinates.insert(0, f"{marker_coords}")
            coordinates.config(state="readonly")        
    except Exception as e:
        if e:
            map_widget.delete_all_marker()
            coordinates.config(foreground="red")
            marker_coords = "Undefined"
            print(f"\n*****Address not found :(*****\nMap is not perfect... Try writing the location differently or clicking the location on the map\n⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄")
                
        coordinates.config(state="normal")
        coordinates.delete(0, END)
        coordinates.insert(0, f"{marker_coords}")
        coordinates.config(state="readonly")
    
address_input.trace_add("read", set_address_callback) ## Write mode causes CPU overhead due to fetching map from server!!!              
address.grid(row=0, 
             column=4,
             padx=(2,5),
             pady=(5,5)
             )
    
def read_address_input():
    global marker_coords
    
    dt = datetime.datetime.now()
    
    print(f"\n{dt.strftime('%Y-%m-%d %H:%M:%S')}: Marker pinned using Address entry on {address_input.get()} @{marker_coords}.")
    
go = Button(options,
            text="Go!",
            command=read_address_input,
            width=5,
            background="#9999ff"
            )
go.grid(row=0, 
        column=5,
        padx=(0, 5))

        
slope_label = Label(options,
                      text="Slope [°]:",
                      font=('Arial', 12)
                      )
slope_label.grid(row=2, 
                 column=0,
                 padx=(5,0),
                 pady=(5,5)
                 )
slope = Entry(options,
              font=('Arial'),
              justify="center",
              textvariable=slope_input  
              )

def set_slope_callback(var, index, mode):    
    global slope_is_valid
    pattern = r'^[-+]?\d*\.?\d+$'
    slope_input = slope.get()
    valid = re.match(pattern, slope_input)
    slope.config(foreground="black")
    
    if not valid:
        slope_input = ""
        slope_is_valid = False
    else:
        slope_is_valid = True

slope_input.trace_add("write", set_slope_callback)
slope.grid(row=2, 
           column=1,
           padx=(2,5),
           pady=(5,5)
           )

length_label = Label(options,
                      text="Length [m]:",
                      font=('Arial', 12)
                      )
length_label.grid(row=2, 
                 column=3,
                 padx=(5,0),
                 pady=(5,5)
                 )
length = Entry(options,
                font=('Arial'),
                justify="center",
                validate="focus",
                textvariable=length_input
                )

def set_length_callback(var, index, mode):    
    global length_is_valid
    pattern = r'^[-+]?\d*\.?\d+$'
    length_input = length.get()
    valid = re.match(pattern, length_input)
    length.config(foreground="black")
    
    if not valid:
        length_input = ""
        length_is_valid = False
    else:
        length_is_valid = True

length_input.trace_add("write", set_length_callback)
length.grid(row=2, 
           column=4,
           padx=(2,5),
           pady=(5,5)
           )

####################################

##########################
####   Results Pane   ####
##########################
results = Frame(window, background="#808080")
results.pack(pady=(5,5))

results_label = Label(results,
                    #   text=f"{results_description.get()}",
                      font=("Cascadia", 10),
                      height=20,
                      justify=LEFT
                      )
results_label.pack()

def calculator():
    global marker_coords
    global slope_input
    global length_input
    global slope_is_valid
    global length_is_valid
    global results_description
    
    results_label.config(font=("Cascadia", 10, "normal"))
    
    try:
        latitude = marker_coords[0] 
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~\nCalculating for {marker_coords}")
    except TypeError:
        print(f"\nERROR: No coordinates found. Please select a location via clicking on the map or entering a valid address into the address input field.")
        results_description.set(f"{results_description.get()}ERROR: No coordinates found. Please select a location via clicking on the map or entering\n             a valid address into the address input field.\n")
        
    try:
        slope_value = float(slope_input.get())
    except ValueError:
        slope.config(foreground="red")
        if slope_input.get() == "": 
            print(f"\nERROR: Slope input cannot be empty. Please enter a valid number for the slope angle in degrees.")
            results_description.set(f"{results_description.get()}\nERROR: Slope input cannot be empty. Please enter a valid number for the slope angle in degrees.\n")
        else:
            print(f"\nERROR: Inadmissable slope value: {slope_input.get()}. Please enter a valid number for the slope in degrees.")
            results_description.set(f"{results_description.get()}\nERROR: Inadmissable slope value: {slope_input.get()}. Please enter a valid number for the slope in degrees.\n")
           
    try:
        length_value = float(length_input.get())
    except ValueError:
        length.config(foreground="red")
        if length_input.get() == "": 
            print(f"\nERROR: Length input cannot be empty. Please enter a valid number for the length in meters.")
            results_description.set(f"{results_description.get()}\nERROR: Length input cannot be empty. Please enter a valid number for the length in meters.")
        else:
            print(f"\nERROR: Inadmissable length value: {length_input.get()}. Please enter a valid number for the length in meters.")
            results_description.set(f"{results_description.get()}\nERROR: Inadmissable length value: {length_input.get()}. Please enter a valid number for the length in meters.")
    
    if slope_is_valid and length_is_valid and not marker_coords == "":
        results_label.config(font=("Cascadia", 10, "bold"))
        print(f"\nSlope angle set to {slope_input.get()}°.")
        print(f"\nLength value set to {length_input.get()} meters.")

        result = minimum_pv_shadow_length(latitude, slope_value, length_value)
        print(f"\nThe minimum shadow length of each P/V panel is approximately {result:.2f} meters.\n~~~~~~~~~~~~~~~~~~~~~~~~~")
        results_description.set(f"{results_description.get()}\nThe minimum shadow length of each P/V panel is approximately {result:.2f} meters.")
    else:
        print("⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄\nCalculation aborted.\n_________________________")
            
    results_label.config(text=results_description.get())
    results_description.set("")
    
            
calculate = Button(options,
                   text="Calculate",
                   font=('Arial', 12),
                   background="#ffc266",
                   command=calculator
                   )

calculate.grid(row=6,
               column=4, 
               columnspan=1,
               padx=(2,5),
               pady=(5,5)
               )


def clear():
    global marker_coords
    map_widget.delete_all_marker()
    
    marker_coords = None
    coordinates.config(state="normal")
    coordinates.delete(0, END)
    coordinates.config(state="readonly")
    
    address.delete(0, END)
    
    slope.delete(0, END)
    
    length.delete(0, END)
    
    global results_description
    results_description.set("")
    results_label.config(text="")
    
clear = Button(options,
               text="Clear",
               font=('Arial', 12),
               background="#ff6666",
               command=clear
               )

clear.grid(row=6,
           column=1,
           padx=(2,5),
           pady=(5,5)
           )
    
####################################

##########################
####       Main       ####
##########################

window.mainloop()   ## Place window on computer screen and listen for events

####################################

##########################
#### Unused Features ####
##########################

## Azimuth is not needed for the minimum distance between panels to avoid shading in the case of single, double, and or triple panel system. ##
# azimuth_angle = IntVar()
# azimuth_angle.set("120")

# def set_azimuth():
#     if azimuth.get() == "":
#         azimuth_value = 120
#     else:
#         azimuth_value = azimuth.get()
    
#     return azimuth_value

# azimuth_label = Label(options,
#                       text="Azimuth [°]:",
#                       font=('Arial', 12)
#                       )
# azimuth_label.grid(row=2, 
#                    column=0,
#                    padx=(5,0),
#                    pady=(5,5)
#                    )
# azimuth = Entry(options,
#                 font=('Arial'),
#                 justify="center",
#                 validate="focus"
#                 )
# azimuth.insert(0, 
#                f"{set_azimuth()}")
# azimuth.config(state="readonly")
# azimuth.grid(row=2, 
#              column=1, 
#              padx=(2,5),
#              pady=(5,5)
#              )