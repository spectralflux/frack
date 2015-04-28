from PIL import Image, ImageDraw
import colorsys


class FractalImage():

    def __init__(self, fractal, x_dim, y_dim, scale, center):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.scale = scale
        self.image = Image.new("RGB", (x_dim, y_dim))
        self.palette_file_path = "resources/dawn_256_rgb.txt"
        gen_palette = self.load_palette()
        self.palette = gen_palette["palette"]
        self.max_colours = gen_palette["palette_size"]
        self.fractal = fractal
        self.center = center

    def draw(self):
        d = ImageDraw.Draw(self.image)

        for y in xrange(self.y_dim):
            for x in xrange(self.x_dim):
                n = self.fractal.f(x, y, self.scale, self.center)
                d.point((x, y),
                        fill=self.palette[int(n * (self.max_colours-1))])

    def load_palette(self):
        palette = []
        with open(self.palette_file_path) as palette_file:
            colours = [x.strip().split(' ') for x in palette_file.readlines()]
            for i, colour in enumerate(colours):
                palette.append(tuple(map(int, colour)))
        palette = palette[::-1]
        return {"palette": palette, "palette_size": len(palette)}

    def save(self):
        self.image.save("result.png")
