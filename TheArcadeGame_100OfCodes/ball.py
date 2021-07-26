from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.x_direction = 9
        self.y_direction = 9
        self.move_speed = 0.1

    def move(self):
        self.pu()
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_direction *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        self.y_direction *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
