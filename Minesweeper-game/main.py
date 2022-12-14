from tkinter import *
from cell import Cell
import utils
import settings

root = Tk()

# Overwrite the settings of the window
root.configure(bg = "black")

root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')

root.title("Minesweeper Game")

root.resizable(False, False)

top_frame = Frame(
    root,
    bg = "black", 
    width = settings.WIDTH,
    height = utils.height_prct(25)
)

top_frame.place(x = 0, y = 0)

left_frame = Frame(
    root,
    bg = "black", 
    width = utils.width_prct(25),
    height = utils.height_prct(75)
)

left_frame.place(x = 0, y = utils.height_prct(25))

center_frame = Frame(
    root,
    bg = "black", 
    width = utils.width_prct(75),
    height = utils.height_prct(75)
)

center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)

c1 = Cell()


# Run the window
root.mainloop() 