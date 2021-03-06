from manim import *


class PointMovingOnShapes(Scene):
	def construct(self):
	
		# create a square
		square = Square(color=BLUE)
		square.flip(RIGHT)
		square.rotate(-3 * TAU / 8)
		
		# create a circle
		circle = Circle()
		circle.set_fill(PINK, opacity=0.5) # set the color and transparency
		
		# create animations
		self.play(GrowFromCenter(square))
		self.play(Transform(square, circle))
		
		self.wait() # wait for some seconds


class MovingFrame(Scene):
	def construct(self):
	
		# write equations
		equation = MathTex("(1-x^2)y''-2xy'+6y", "=", "0")
		
		# create animation
		self.play(Write(equation))
		
		# add moving frames
		framebox1 = SurroundingRectangle(equation[0], buff=.1)
		framebox2 = SurroundingRectangle(equation[2], buff=.1)
		
		# create animations
		self.play(Create(framebox1))
		self.wait
		self.play(ReplacementTransform(framebox1, framebox2))
		self.wait


class MathematicalEquation(Scene):
	def construct(self):
		
		# write equations
		equation1 = MathTex("(1-x^2)y''-2xy'+6y")
		eq_sign_1 = MathTex("=")
		equation2 = MathTex("0")
		eq_sign_2 = MathTex("=")
		equation3 = MathTex("(1-x^2)y''-2xy'+n(n+1)y")
		
		# put each equation or sign in the appropraite positions
		equation1.next_to(eq_sign_1, LEFT)
		equation2.next_to(eq_sign_1, RIGHT)
		
		eq_sign_2.shift(DOWN)
		equation3.shift(DOWN)
		
		# align bottom equations with the top equations
		eq_sign_2.align_to(eq_sign_1, LEFT)
		equation3.align_to(equation2, LEFT)
		
		# group equations and sign
		eq_group = VGroup(equation1, eq_sign_1, equation2, eq_sign_2, equation3)
		
		# create animation
		self.play(Write(eq_group))
		
		self.wait()


# class Graph(GraphScene):
	# def __init__(self, **kwargs):
		# GraphScene.__init__(
			# self,
			# x_min=-3.5,
			# x_max=3.5,
			# y_min=-5,
			# y_max=5,
			# graph_origin=ORIGIN,
			# axes_color=BLUE,
			# x_labeled_nums=range(-4, 4, 2),
			# y_labeled_nums=range(-5, 5, 2),
			# **kwargs
		# )
		
	# def construct(self):
		# self.setup_axes(animate=True)
		
		##draw graphs
		# func_graph_cube = self.get_graph(lambda x: x**3, RED)
		# func_graph_ncube = self.get_graph(lambda x: -x**3, GREEN)
		
		##create lables
		# graph_lab = self.get_graph_label(func_graph_cube, label="x^3")
		# graph_lab2 = self.get_graph_label(func_graph_ncube, label="-x^3", x_val=-3)
		
		##create a verticle line
		# vert_line = self.get_vertical_line_to_graph(1.5, func_graph_cube, color=YELLOW)
		# label_coord = self.input_to_graph_point(1.5, func_graph_cube)
		# text = MathTex(r"x=1.5")
		# text.next_to(label_coord)
		
		# self.add(func_graph_cube, func_graph_ncube, graph_lab, graph_lab2, vert_line, text)
		# self.wait()


class GoatProblem(Scene):
	def construct(self):
		
		# create nodes
		node1 = Circle(z_index=1)
		node1.set_fill(RED, opacity=1)
		node2 = Circle(z_index=1)
		node2.set_fill(BLUE, opacity=1).set_color(BLUE)
		node3 = Circle(z_index=1)
		node3.set_fill(GREEN, opacity=1).set_color(GREEN)
		
		# set initial positions
		node3.shift(DOWN)
		
		## add nodes with text
		# node 1
		self.play(Create(node1))
		self.play(node1.animate.shift(LEFT, UP).scale(.6))
		node1_text = Text("Wolf", font_size=23).next_to(node1, UP)
		self.play(Write(node1_text))
		
		# node 2
		self.play(Create(node2))
		self.play(node2.animate.shift(RIGHT, UP).scale(.6))
		node2_text = Text("Goat", font_size=23).next_to(node2, UP)
		self.play(Write(node2_text))
		
		# node 3
		self.play(Create(node3))
		self.play(node3.animate.scale(.6))
		node3_text = Text("Cabbage", font_size=23).next_to(node3, DOWN)
		self.play(Write(node3_text))
		
		# add lines connecting nodes
		line1 = Line(node1.get_center(), node2.get_center(), z_index=0)
		self.play(Create(line1))
		line2 = Line(node2.get_center(), node3.get_center(), z_index=0)
		self.play(Create(line2))
		
		# remove text
		self.play(FadeOut(node1_text, node2_text, node3_text))
		
		# create group and move nodes to left side
		left_group = VGroup(node1, node2, node3, line1, line2)
		self.play(left_group.animate.shift(LEFT*5))
		
		# create 'river' rectangle
		river = Rectangle(color=BLUE, height=10, width=4)
		river.set_fill(BLUE, opacity=1)
		self.play(DrawBorderThenFill(river))
		
		# wait at end
		self.wait()
		
