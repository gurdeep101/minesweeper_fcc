from tkinter import Button # import only relevant class
# abstract button from main.py
class Cell:
    def __init__(self, is_mine=False):
        # constructor for this class
        self.is_mine = is_mine
        # instantiate button object
        self.cell_btn_object = None
        
    def create_btn_object(self, location):
        # create instance method to create the button 
        # assign to self.cell_btn_object
        # create instance of button class from tkinter
        btn = Button(
            location, # location of button
            text = 'random',
        )
        # assign button object created to cell_btn_object
        self.cell_btn_object = btn