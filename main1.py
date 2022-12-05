from tkinter import *
# comes with useful classes for gui

import settings
import utils
from cell import Cell # import cell class from file cell.py

root = Tk() # instantiate Tk and create box

# background color
root.configure(bg = 'black')

# change size of window
# root.geometry('WIDTHxHEIGHT') # don't use space here; i.e. width x height
root.geometry(f'{settings.width}x{settings.height}')
root.title('Minesweeper Game!')

# prevent resizing; maximise greyed out
root.resizable(False, False)

# create frames - divide screen into parts
# define location of top_frame using place method
# top left corner is 0th pixel
# width = 720 = end index
# height = 1440 = end index
top_frame = Frame(
    root, # frame located where
    bg = 'red', # frame color for visibility
    width = settings.width,
    height = utils.height_prct(25)# 180
    )

# specify start location of top frame
top_frame.place(x = 0, y = 0)

left_frame = Frame(
    root,
    bg = 'blue',
    width = utils.width_prct(25), # 25% of width
    height = utils.height_prct(75)# 75% of height # 540 # 720 - 180
)

# specify start location of the frame
left_frame.place(x=0, y = utils.height_prct(25)) # start just below top frame

# add centre frame for game
center_frame = Frame(
    root,
    bg = 'green',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)

# specify top locations of center_frame
center_frame.place(
    x = utils.width_prct(25),
    y=utils.height_prct(25)
    )

# # add buttons to center frame
# this is demo code, to create as class in cell.py
# btn1 = Button(
#     center_frame,
#     bg = 'Purple',
#     text = 'First Button',
# )

# # specify button location
# btn1.place(
#     x = 0,
#     y = 0
# )

# create instance of cell class
c1 = Cell()

# call create_btn_object class and specify location as center frame
c1.create_btn_object(center_frame)

# specify location of button object in center frame
c1.cell_btn_object.place(
    x = 0, y = 0
)

c2 = Cell()
c2.create_btn_object(center_frame)
# need to know  place of 2nd button
c2.cell_btn_object.place(
    x = 55, y = 0
    )

# this is not scalable hence replace place method with grid for buttons in center frame


# tell tk to run the box till we close 
root.mainloop()
