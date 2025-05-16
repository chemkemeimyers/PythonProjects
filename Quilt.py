import tkinter as tk

# each patch is a square with this width and height:
PATCH_SIZE = 100
CANVAS_WIDTH = PATCH_SIZE * 4
CANVAS_HEIGHT = PATCH_SIZE * 2

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()
    # draw the first row of patches
    draw_square_patch(canvas, 0, 0)
    draw_circle_patch(canvas, PATCH_SIZE, 0)
    draw_square_patch(canvas, PATCH_SIZE*2, 0)
    draw_circle_patch(canvas, PATCH_SIZE*3, 0)
    # draw the second row of patches
    draw_circle_patch(canvas, 0, PATCH_SIZE)
    draw_square_patch(canvas, PATCH_SIZE, PATCH_SIZE)
    draw_circle_patch(canvas, PATCH_SIZE*2, PATCH_SIZE)
    draw_square_patch(canvas, PATCH_SIZE*3, PATCH_SIZE)
    root.mainloop()

"""
Function to draw a circle - special case of an oval with equal dimensions
Requires canvas, start x, start y, end x, end y
pre: No circle at specified coordinates
post: Circle at specified coordinates
""" 
def draw_circle_patch(canvas, start_x, start_y):
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    canvas.create_oval(
        start_x,
        start_y,
        end_x,
        end_y,
        fill="salmon"
    )


def draw_square_patch(canvas, start_x, start_y):
    # draws a purple frame at (start_x, start_y)
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    inset = 20
    # first draw a purple square over the entire patch
    canvas.create_rectangle(start_x, start_y, end_x, end_y, fill='purple')
    # then draw a smaller white square on top
    canvas.create_rectangle(start_x+inset, start_y+inset, 
        end_x-inset, end_y-inset, fill='white')
    
if __name__ == '__main__':
    main()