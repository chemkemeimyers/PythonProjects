import tkinter as tk

"""
Simple program to draw a rectangle on a canvas
"""
def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=800, height=200)
    canvas.pack()
    canvas.create_rectangle(20, 20, 100, 100, fill="blue")
    root.mainloop()

if __name__ == '__main__':
    main()