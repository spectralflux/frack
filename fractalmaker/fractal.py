import math


class Fractal:
    """ Base class for fractal calculations.
    function f is the function that powers the fractal. """

    def __init__(self, max_iterations):
        self.max_iterations = max_iterations

    def f(self, x, y, scale, center):
        pass


class BurningShip(Fractal):

    def __init__(self, max_iterations):
        Fractal.__init__(self, max_iterations)

    def f(self, x, y, scale, center):
        # TODO use scale and center variables, clean constants up
        midpoint_x = 1.755
        midpoint_y = 0.03
        range_ = 0.04
        N = 800  # TODO this needs to match x or y dimension

        p0x = 0
        p0y = 0

        cx = midpoint_x + 2 * range_ * (x / float(N) - 0.5)
        cy = midpoint_y + 2 * range_ * (y / float(N) - 0.5)

        for n in xrange(self.max_iterations):
            px = p0x*p0x - p0y*p0y - cx
            py = 2 * abs(p0x*p0y) - cy
            p0x = px
            p0y = py
            if (px*px + py*py > 10):
                break
        n = n/100.
        return n


class Mandelbrot(Fractal):

    def __init__(self, max_iterations):
        Fractal.__init__(self, max_iterations)

    def f(self, x, y, scale, center):
        c = complex(x * scale - center[0], y * scale - center[1])
        z = 0
        for n in xrange(self.max_iterations + 1):
            z = z**2 + c
            if abs(z) > 2:
                return n/100.
        return 1


class JuliaSet(Fractal):
    """ A julia set is just a Mandelbrot set with a complex z, but keeping them as
        seperate objects for clarity. """

    def __init__(self, max_iterations):
        Fractal.__init__(self, max_iterations)

    def f(self, x, y, scale, center):
        c = complex(x * scale - center[0], y * scale - center[1])
        z = complex(0.3, 0.6)
        for n in xrange(self.max_iterations + 1):
            z = z**2 + c
            if abs(z) > 2:
                return n/100.
        return 1
