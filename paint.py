# Import Libs
import tkinter
from tkinter import colorchooser


class PaintApp:

    def __init__(self, rt):

        self.root = rt
        self.root.title("Paint App")
        self.root.geometry("800x600")

        self.canvas = tkinter.Canvas(rt, bg="white")
        self.canvas.pack(fill=tkinter.BOTH, expand=True)

        self.brush_color = "black"
        self.pen_size = 2
        self.setup_tools()

        self.canvas.bind("<Button-1>", self.start_paint)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.stop_paint)

    def setup_tools(self):

        self.tools_frame = tkinter.Frame(tr)
        self.tools_frame.pack(fill=tkinter.X)

        self.color_button = tkinter.Button(self.tools_frame, text="Choose Color", command=self.choose_color)
        self.color_button.pack(side=tkinter.LEFT)

        self.clear_button = tkinter.Button(self.tools_frame, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.pack(side=tkinter.LEFT)

    def choose_color(self):
        color = colorchooser.askcolor()[1]

        if color:
            self.brush_color = color

    def clear_canvas(self):
        self.canvas.delete("all")

    def start_paint(self, event):
        self.prev_x, self.prev_y = event.x, event.y

    def paint(self, event):
        x, y = event.x, event.y
        self.canvas.create_line(self.prev_x, self.prev_y, x, y, fill=self.brush_color,
                                width=self.pen_size, capstyle=tkinter.ROUND, smooth=tkinter.TRUE)
        self.prev_x, self.prev_y = x, y

    def stop_paint(self, event):
        pass


tr = tkinter.Tk()
app = PaintApp(tr)
tr.mainloop()
