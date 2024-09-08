from manim import *

class FittingObjects(Scene):
    def construct(self):
        # Create axes
        axes = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=6, y_length=6)
        # Move axes to the left
        axes.to_edge(LEFT,buff=0.5)

        # Create a circle
        circle = Circle(stroke_width=6, stroke_color=YELLOW, fill_color=BLUE, fill_opacity=0.5)
        # Make the diameter of the circle 2 and move it down right
        circle.set_width(2).to_edge(DR,buff=0)
        
        # Create traingle
        triangle = Triangle(stroke_color=RED, stroke_width=10, fill_color=GREEN, fill_opacity=0.5)
        triangle.set_height(2).shift(DOWN*3, RIGHT*3)
        # Make the animation of the axes
        self.play(Write(axes))
        self.play(DrawBorderThenFill(circle))
        self.play(circle.animate.set_width(1))
        self.play(Transform(circle, triangle),run_time=3)
