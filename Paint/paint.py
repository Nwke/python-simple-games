from tkinter import *


class Paint:
    def __init__(self, width, height, brush_size, brush_color):
        self.width = width
        self.height = height
        self.brush_size = brush_size
        self.brush_color = brush_color

        self.root = Tk()
        self.root.title = 'My Paint'
        self.ctx = Canvas(self.root, width=self.width, height=self.height, bg='white')

    def go_paint(self, event):
        x1 = event.x - self.brush_size
        x2 = event.x + self.brush_size
        y1 = event.y - self.brush_size
        y2 = event.y + self.brush_size

        self.ctx.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color)

    def brush_size_change(self, new_size):
        self.brush_size = new_size

    def color_change(self, new_color):
        self.brush_color = new_color

    def main(self):
        self.ctx.bind('<B1-Motion>', self.go_paint)

        set_red_color = self.create_btn_color('red')
        set_blue_color = self.create_btn_color('blue')
        set_black_color = self.create_btn_color('black')
        set_white_color = self.create_btn_color('white')

        set_clear_color = Button(text='Очистить полотно', width=20, command=lambda: self.ctx.delete('all'))
        btn_size = Button(text='5', width=10, command=lambda: self.brush_size(5))

        self.ctx.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E + W + S + N)
        self.ctx.columnconfigure(6, weight=1)
        self.ctx.rowconfigure(2, weight=1)

        set_red_color.grid(row=0, column=2)
        set_blue_color.grid(row=0, column=3)
        set_black_color.grid(row=0, column=4)
        set_white_color.grid(row=0, column=5)
        set_clear_color.grid(row=1, column=5)
        btn_size.grid(row=1, column=2)

        self.root.mainloop()

    def create_btn_color(self, color):
        return Button(text=color, width=10, command=lambda: self.color_change(color))


paint = Paint(700, 500, 3, 'black')
paint.main()
