from tkinter import *
from tkinter.ttk import *
import datetime
import tkintermapview

window = Tk()   ## Instantiate an instance of a window - Window constructor
window.geometry(f"{750}x{700}")    ## Change the size of the window
window.title("EEN445 - P/V Calculator")  ## Change the title of the window

icon = PhotoImage(file='./Images/solar-clipart.png') 
window.iconphoto(True, icon)
window.config(background="#D9EDBF")

## TODO about_menu
def about_menu():
    about_menu = Toplevel()
 
## TODO help_menu
def help_menu():
    help_window = Toplevel()

menu_bar = Menu(window)
window.config(menu=menu_bar)
menu_bar.add_command(label="About", command=about_menu)
menu_bar.add_command(label="Help", command=help_menu)

map_widget = tkintermapview.TkinterMapView(window, width=750,height=300, corner_radius=0)
map_widget.set_position(34.9220, 32.8794)
map_widget.set_zoom(9)
map_widget.pack(anchor=S)

pv_marker_exists = False
marker_coords = None
dt = datetime.datetime.now()
marker = PhotoImage(file="./Images/pv-map-marker.png")
address_input = StringVar()

def marker_pin(coords):
    global pv_marker_exists
    global marker_coords
    global dt 
    global marker
    
    if pv_marker_exists == True:
        map_widget.delete_all_marker()
        pv_marker_exists = False
        
    map_widget.set_marker(coords[0], coords[1], text=f"{dt}", icon=marker)
    pv_marker_exists = True
    print(f"\n{dt}: Marker pinned using map widget @{coords}.")
    marker_coords = coords
    
    coordinates.config(foreground="black")
    coordinates.config(state="normal")
    coordinates.delete(0, END)
    coordinates.insert(0, f"{coords}")
    coordinates.config(state="readonly")
            
def marker_remove():
    map_widget.delete_all_marker()
    coordinates.config(state="normal")
    coordinates.delete(0, END)
    coordinates.config(state="readonly")
    address.delete(0, END)
        
map_widget.add_left_click_map_command(marker_pin)
map_widget.add_right_click_menu_command(label="Clear all markers",
                                        command=marker_remove)

options = Frame(window)
options.pack()

## TODO Try to make font smaller without affecting entry size
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
    
    try:
        if not address.get() == "":
            address_marker = map_widget.set_address(f"{address.get()}", marker=True, icon=marker)
            marker_coords = address_marker.position
            map_widget.delete_all_marker()
            map_widget.set_marker(marker_coords[0], marker_coords[1], text=f"{dt}", icon=marker)
            
            coordinates.config(foreground="black")
            coordinates.config(state="normal")
            coordinates.delete(0, END)
            coordinates.insert(0, f"{marker_coords}")
            coordinates.config(state="readonly")        
    except Exception as e:
        # Handle exceptions here, for example, print an error message
        if e:
            map_widget.delete_all_marker()
            coordinates.config(foreground="red")
            marker_coords = "Undefined"
            print(f"*****Address not found :(*****\nMap is not perfect... Try writing the location differently or clicking the location on the map\n⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄")
                
        coordinates.config(state="normal")
        coordinates.delete(0, END)
        coordinates.insert(0, f"{marker_coords}")
        coordinates.config(state="readonly")
    
address_input.trace_add("read", set_address_callback)                
address.grid(row=0, 
             column=4,
             padx=(2,5),
             pady=(5,5)
             )
    
def read_address_input():
    global marker_coords
    global dt
    print(f"{dt}: Marker pinned using Address entry on {address_input.get()} @{marker_coords}.\n")
    
go = Button(options,
            text="Go!",
            command=read_address_input,
            width=5,
            )
go.grid(row=0, 
        column=5,
        padx=(0, 5))
        
def set_azimuth():
    if azimuth.get() == "":
        azimuth_value = 120
    else:
        azimuth_value = azimuth.get()
    
    return azimuth_value

azimuth_label = Label(options,
                      text="Azimuth [°]:",
                      font=('Arial', 12)
                      )
azimuth_label.grid(row=2, 
                   column=0,
                   padx=(5,0),
                   pady=(5,5)
                   )
azimuth = Entry(options,
                font=('Arial'),
                justify="center",
                validate="focus"
                )
azimuth.insert(0, 
               f"{set_azimuth()}")
azimuth.config(state="readonly")
azimuth.grid(row=2, 
             column=1, 
             padx=(2,5),
             pady=(5,5)
             )

slope_label = Label(options,
                      text="Slope [°]:",
                      font=('Arial', 12)
                      )
slope_label.grid(row=2, 
                 column=3,
                 padx=(5,0),
                 pady=(5,5)
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

slope.grid(row=2, 
           column=4,
           padx=(2,5),
           pady=(5,5)
           )

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