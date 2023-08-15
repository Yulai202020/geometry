from lib import Point, Text_
from pathlib import Path

import drawsvg as draw

file_name = Path(__file__).stem

d = draw.Drawing(1000, 800, origin = 'center')

# Draw
d.append(draw.Lines(-80, 50,
                     70, 50,
                     0, -50,
                    close=False,
            fill='#eeee00',
            stroke='blue'))

d.append(draw.Line(-200, 50, 70, 50,
        stroke='blue', stroke_width=2, fill='none'))

d.append(draw.Line(-200, 50, 40, -30,
        stroke='blue', stroke_width=2, fill='none'))

# Texts

d.append(Text_('AC1 * BA1 * CB1 = C1B * A1C * B1A', 100, 0))

d.append(Text_('A', 0, -53))
d.append(Text_('A1', -50, -7))

d.append(Text_('B', 73, 50))
d.append(Text_('B1', -206, 47))

d.append(Text_('C', -80, 60))
d.append(Text_('C1', 16, -27))

# Draw points

d.append(Point(0, -50))     # A
d.append(Point(-38, -4))    # A1

d.append(Point(70, 50))     # B
d.append(Point(-200, 50))   # B1


d.append(Point(-80, 50))    # C
d.append(Point(20, -23))    # C1

# Save image
d.save_svg(f"../{file_name}.svg")