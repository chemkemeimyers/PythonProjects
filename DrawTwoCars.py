import tkinter as tk

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()
    # draws two cars
    x = 10
    y = 10
    draw_car(canvas, x, y) #Draw the first car

    x = 100
    y = 100
    draw_car(canvas, x, y)

    root.mainloop()

def draw_car(canvas, x, y):#Add canvas argument and coordinates x and y
    # draws a car at the location x, y
    # you can assume that math offsets for the rectangles are correct
    canvas.create_rectangle(x, y, x + 50, y + 20)
    canvas.create_rectangle(x + 10, y - 10, x + 40, y + 20)

if __name__ == '__main__':
    main()