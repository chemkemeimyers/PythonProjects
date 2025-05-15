import tkinter as tk
"""
Program to draw a line of boxes at the bottom of a canvas
"""

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()
    #Create as many as N Boxes
    for i in range(N_BOXES):
        #Define left and top corner of the box
        start_x = i * BOX_SIZE
        start_y = CANVAS_HEIGHT - BOX_SIZE

        #Define right and bottom corner of the box
        end_x = i * BOX_SIZE + BOX_SIZE
        end_y = CANVAS_HEIGHT

        #Draw rectangle
        canvas.create_rectangle(
            start_x,
            start_y,
            end_x,
            end_y,
            fill="white",
            outline="black"
        )
    root.mainloop()    


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
    