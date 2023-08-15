from lib import Point, Text_
from pathlib import Path

import drawsvg as draw

file_name = Path(__file__).stem

d = draw.Drawing(1000, 800, origin = 'center')

# Draw
circle = draw.Circle(0, 0, 50, fill = 'red', stroke_width=2, stroke='black')
d.append(circle)

d.append(draw.Line(-200, 50, 100, -50,
        stroke='blue', stroke_width=2, fill='none'))

d.append(draw.Line(-200, -50, 100, -50,
        stroke='blue', stroke_width=2, fill='none'))

# Texts

d.append(Text_('AB^2 = AD*AC', 100, 0))

d.append(Text_('A', 103, -50))
d.append(Text_('B', -3, -53))

d.append(Text_('C', 45, -23))
d.append(Text_('D', -57, -2))

# Draw points

d.append(Point(100, -50))   # A
d.append(Point(0, -50))     # B
d.append(Point(40, -30))    # C
d.append(Point(-48, -1))   # D

# Save image
d.save_svg(f"../{file_name}.svg")