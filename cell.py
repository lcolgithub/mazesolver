from graphics import Window
from graphics import Line
from graphics import Point

class Cell:
    def __init__(self, win):
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.__win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited= False

    def draw(self, x1, y1, x2, y2):

        if self.__win is None:
            return

        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(self.get_midpoint(), to_cell.get_midpoint())
        self.__win.draw_line(line, fill_color)

        # x_mid = (self.__x1 + self.__x2) / 2
        # y_mid = (self.__y1 + self.__y2) / 2

        # to_x_mid = (to_cell.__x1 + to_cell.__x2) / 2
        # to_y_mid = (to_cell.__y1 + to_cell.__y2) / 2

        # fill_color = "red"
        # if undo:
        #     fill_color = "gray"

        # # moving left
        # if self.__x1 > to_cell.__x1:
        #     line = Line(Point(self.__x1, y_mid), Point(x_mid, y_mid))
        #     self.__win.draw_line(line, fill_color)
        #     line = Line(Point(to_x_mid, to_y_mid), Point(to_cell.__x2, to_y_mid))
        #     self.__win.draw_line(line, fill_color)

        # # moving right
        # elif self.__x1 < to_cell.__x1:
        #     line = Line(Point(x_mid, y_mid), Point(self.__x2, y_mid))
        #     self.__win.draw_line(line, fill_color)
        #     line = Line(Point(to_cell.__x1, to_y_mid), Point(to_x_mid, to_y_mid))
        #     self.__win.draw_line(line, fill_color)

        # # moving up
        # elif self.__y1 > to_cell.__y1:
        #     line = Line(Point(x_mid, y_mid), Point(x_mid, self.__y1))
        #     self.__win.draw_line(line, fill_color)
        #     line = Line(Point(to_x_mid, to_cell.__y2), Point(to_x_mid, to_y_mid))
        #     self.__win.draw_line(line, fill_color)

        # # moving down
        # elif self.__y1 < to_cell.__y1:
        #     line = Line(Point(x_mid, y_mid), Point(x_mid, self.__y2))
        #     self.__win.draw_line(line, fill_color)
        #     line = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell.__y1))
        #     self.__win.draw_line(line, fill_color)

    def get_midpoint(self):
        print(self.__x1)
        return Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2)
        
