#will redo in kivy
import tkinter as tk
from screeninfo import get_monitors

## initialize window
window = tk.Tk()
window.title("To do list")

## geometry (assumes 1 monitor)
m = get_monitors()[0]
w, h = m.width, m.height

#app width = 1/5 of the screen
app_width = w//5
window.geometry("%dx%d" % (app_width, h))

## Add to todo list button
#label
add_item_label = tk.Label(window, text = "add item")
add_item_label.pack(pady=20)

#button
def add_item_btn():
    add_item_window = tk.Tk()
    add_item_window.title("add item")
    #need button for "done", and 2 bars to type in name and end date


add_item_btn = tk.Button(window, text = "add item", command = add_item_btn)
add_item_btn.pack(pady=20)

"""
future of this app:
- implement button to add item
- add on screen gui for each item to be clicked away as finished
- in addition, add option to modify due date and name.
- add timeline of things to do
- potential integration with google calendar (have it on the side in a web window)
- to do items could be sorted by priority AND alphabetical order(optional)

- the todo.txt file structure should be:
index(int)
name(str)
end date(posicxt)

and it can be accessed by the API to display the items and display when its due
"""


    
