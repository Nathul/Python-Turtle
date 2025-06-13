import turtle as tu
from svgpathtools import svg2paths2
from svg.path import parse_path
from tqdm import tqdm
import re

class sketch_from_svg:

    def __init__(self, path, scale=30, x_offset=400, y_offset=400):
        self.path = path
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.scale = scale

    def hex_to_rgb(self, string):
        strlen = len(string)
        if string.startswith('#'):
            if strlen == 7:
                r = string[1:3]
                g = string[3:5]
                b = string[5:7]
            elif strlen == 4:
                r = string[1]*2
                g = string[2]*2
                b = string[3]*2
        elif strlen == 3:
            r = string[0]*2
            g = string[1]*2
            b = string[2]*2
        else:
            r = string[0:2]
            g = string[2:4]
            b = string[4:6]

        return int(r, 16)/255, int(g, 16)/255, int(b, 16)/255

    def extract_number(self, s):
        """Extract numeric value from strings like '500px' or '300pt'"""
        return int(float(re.findall(r"[\d.]+", s)[0]))

    def load_svg(self):
        print('Loading SVG data...')
        paths, attributes, svg_att = svg2paths2(self.path)

        h = svg_att["height"]
        w = svg_att["width"]
        self.height = self.extract_number(h)
        self.width = self.extract_number(w)

        res = []
        for i in tqdm(attributes):
            path_data = i.get('d')
            if not path_data:
                continue

            path = parse_path(path_data)
            fill = i.get('fill', '#000000')  # Default to black if missing
            if fill in ('none', 'transparent'):
                continue  # Skip paths without fill color

            col = self.hex_to_rgb(fill)
            n = len(list(path)) + 2
            pts = [(
                int((p.real / self.width) * self.scale) - self.x_offset,
                int((p.imag / self.height) * self.scale) - self.y_offset
            ) for p in (path.point(i / n) for i in range(n + 1))]
            res.append((pts, col))
        print('SVG data loaded.')
        return res

    def move_to(self, x, y):
        self.pen.up()
        self.pen.goto(x, y)
        self.pen.down()

    def draw(self, retain=True):
        coordinates = self.load_svg()
        self.pen = tu.Turtle()
        self.pen.speed(0)

        for path_col in coordinates:
            is_first = True
            path = path_col[0]
            col = path_col[1]
            self.pen.color(col)
            self.pen.begin_fill()

            for coord in path:
                x, y = coord
                y *= -1  # Invert Y axis to match SVG origin
                if is_first:
                    self.move_to(x, y)
                    is_first = False
                else:
                    self.pen.goto(x, y)

            self.pen.end_fill()

        if retain:
            tu.done()


# Usage:
pen = sketch_from_svg('iron.svg', scale=80)
pen.draw()
