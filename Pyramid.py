import tkinter as tk

"""
Program to build a pyramid of bricks
"""
BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base

CANVAS_WIDTH = BRICKS_IN_BASE *  BRICK_WIDTH     # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels



"""
Function to lay down a row of bricks
Pre: At start of an empty row
Post: At end of a completed row of bricks
"""
def lay_row_of_blocks(canvas, start_x, start_y, width):
    num_bricks = width//BRICK_WIDTH
    for i in range(num_bricks):
        canvas.create_rectangle(
            start_x,
            start_y,
            start_x + BRICK_WIDTH,
            start_y + BRICK_HEIGHT,
            fill = "yellow",
            outline = "black")
        
        start_x = start_x + BRICK_WIDTH

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()
    #Define initial count of bricks
    initial_brick_count = CANVAS_WIDTH // BRICK_WIDTH

    layer_count = initial_brick_count
    
    start_x = 0
    start_y = CANVAS_HEIGHT - BRICK_HEIGHT
    width = CANVAS_WIDTH
    #Lay the first row of bricks
    while(layer_count > 0):
        #Lay the first layer of bricks
        lay_row_of_blocks(canvas, start_x, start_y, width)
        #Update start_x and start_y
        start_x = start_x + BRICK_WIDTH // 2
        start_y = start_y - BRICK_HEIGHT
        width = width - BRICK_WIDTH

        layer_count = layer_count - 1
    
    root.mainloop()

if __name__ == '__main__':
    main()

