from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")

        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)

        self.__running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close())

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while(self.__running):
            self.redraw()
        print("Window Closed")

    def draw_line(self, line, fillcolor="black"):
        line.draw(self.__canvas, fillcolor)

    def close(self):
        self.__canvas.running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Line:
    def __init__(self, point_one, point_two):
        self.point_one = point_one
        self.point_two = point_two

    def draw(self, canvas, fillcolor="black"):
        canvas.create_line(self.point_one.x, self.point_one.y, self.point_two.x, self.point_two.y, fill = fillcolor, width = 2)
        canvas.pack(fill = BOTH, expand = 1)

    

