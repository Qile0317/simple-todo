#class to open the item_editor/adder window
import tkinter as tk
from screeninfo import get_monitors

class item_editor:
    def __init__(self, editing:bool, todo_item = "placeholder"):
        self.editing = editing # bool: true = editing, false = adding
        self.item = todo_item #todo.item obj (used for if its editing mode)
        self.dims = get_monitors()[0] # screen dimensions in pixels. has .width and .height field
        self.is_open = False
    
    #open the window
    def open_editor(self):
        self.is_open = True
        self.window = tk.Tk()
        self.window.update_idletasks()

        if self.editing: # window title
            self.window.title("edit item")
        else:
            self.window.title("add item")
        
        # set dimensions
        self.window.geometry("%dx%d" % (
            self.dims.width//2.5, self.dims.height//2.5))
        self.window.eval('tk::PlaceWindow . center')
    
    #unfinished




            

            


        


# the gui should also allow opening a calendar and selecting start and end dates, and then convert to datetime