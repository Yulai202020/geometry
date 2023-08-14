from lib import Point
import drawsvg as draw

d = draw.Drawing(1000, 800, origin = 'center')

# Draw
circle = draw.Circle(-100, 10, 50, fill = 'red', stroke_width=2, stroke='black')
d.append(circle)

d.append(draw.Line(-200, -40, 50, -40,
        stroke='blue', stroke_width=2, fill='none'))

d.append(draw.Line(-200, 40, 50, -40,
        stroke='blue', stroke_width=2, fill='none'))

# Texts

d.append(draw.Text('AB^2 = AD*AC', 10, -10, 0, fill='blue'))  # 8pt text at (-10, -35)

d.append(draw.Text('A', 10, 52, -40, fill='blue'))  # 8pt text at (-10, -35)
d.append(draw.Text('B', 10, -100, -42, fill='blue'))  # 8pt text at (-10, -35)

d.append(draw.Text('C', 10, -160, 20, fill='blue'))  # 8pt text at (-10, -35)
d.append(draw.Text('D', 10, -50, 0, fill='blue'))  # 8pt text at (-10, -35)

# Draw points
d.append(Point(50, -40, 2)) # A
d.append(Point(-100, -40, 2)) # B
d.append(Point(-148, 23, 2)) # C
d.append(Point(-53, -7, 2)) # D

# save image
d.save_svg('../example.svg')