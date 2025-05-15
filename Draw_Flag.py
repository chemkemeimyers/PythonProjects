import tkinter as tk

"""
Create the flag of Indonesia
"""

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300


def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()
    flag_width = CANVAS_WIDTH
    flag_height = CANVAS_HEIGHT/2

    #define left and top coordinates
    flag_red_strip_start_x = 0
    flag_red_strip_start_y = 0

    #define right and bottom coordinates
    flag_red_strip_end_x = flag_red_strip_start_x + flag_width
    flag_red_strip_end_y = flag_red_strip_start_y + flag_height

    #Draw flag red strip
    canvas.create_rectangle(
        flag_red_strip_start_x,
        flag_red_strip_start_y,
        flag_red_strip_end_x,
        flag_red_strip_end_y,
        fill="red"
    )
    root.mainloop()
    

if __name__ == '__main__':
    main()