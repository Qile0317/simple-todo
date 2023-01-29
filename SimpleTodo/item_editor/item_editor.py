#class to open the item_editor/adder window
import tkinter as tk
from screeninfo import get_monitors
from src.items import attribute_dict as attribute
from src.items import todo_item as todo

placeholder_item = todo.item()

class item_editor:
    def __init__(self, editing:bool = True, todo_item = placeholder_item):
        self.editing = editing # bool: true = editing, false = adding
        self.item = todo_item #todo.item obj (used for if its editing mode)
        self.dims = get_monitors()[0] # screen dimensions in pixels. has .width and .height field
        self.is_open = False

    def _update(self): #function to update the items with new entries from the self.entries vector.
        print("placeholder")

    #open the window
    def Open(self):
        #initialize
        self.is_open = True
        self.window = tk.Tk()
        self.window.update_idletasks()

        # window title
        if self.editing: 
            self.window.title("edit item")
        else:
            self.window.title("add item")
        
        # set dimensions and place in center (doesnt properly work)
        self.window.geometry("%dx%d" % (
            self.dims.width//2.5, self.dims.height//2.5))
        self.window.eval('tk::PlaceWindow . center')

        # add entry widgets
        self.entries = [] # may be better to initialize in __init__ ? 
        for i in range(1, 8+1):
            tk.Label(self.window, text = attribute.Dict[i]).grid(row = i-1)
            curr_entry = tk.Entry(self.window)
            curr_entry.insert(0, str(self.item.attributes[i-1]))
            self.entries.append(curr_entry)
            curr_entry.grid(row = i-1, column = 1)

        #cancel button - doesn't quit but its there
        cancel_button = tk.Button(self.window, text = "Cancel",
        command = self.window.quit).grid(row = 9, column = 0,
                                         sticky=tk.W, pady = 4)
        cancel_button.pack()
        
        #unfinished complete button - the _update function needs to be finished first
        #AttributeError: 'NoneType' object has no attribute 'pack'
        complete_button = tk.Button(self.window, text ="Complete",
        command = self._update).grid(row = 9, column = 1,
                                            sticky =tk.W,pady = 8)
        complete_button.pack()

        #Loop
        self.window.mainloop()

    #unfinished    
# the gui should also allow opening a calendar and selecting start and end dates, and then convert to datetime