import drawsvg as draw

d = draw.Drawing(1000, 800, origin = 'center')

center_x = 10
center_y = 12

x_1 = 10 ; x_2 = 12
y_1 = 12 ; y_2 = 14

# Draw a circle
draw.Circle( center_x, center_y, fill = "color", stroke_width = '<ширина отконтовки>', stroke = "<цвет отконтовки>" )
draw.Rectangle(x_1, y_1, x_2, y_2, fill = 'color')