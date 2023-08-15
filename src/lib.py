from drawsvg import Circle, Text
def Point(x: int, y: int, r: int = 2, fill: str = "green"):
    return Circle(x, y, r, fill = fill)

def Text_(text: str , x: int, y: int, fill: str = 'blue'):
    return Text(text, 10, x, y, fill = fill)