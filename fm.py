import fractalmaker.fractal as fractal
import fractalmaker.fractal_image as fractal_image

# constants
x_dim = 800
y_dim = 800
scale = 1./(x_dim/3.)
center = [2.0, 1.5]


def main():
    #frac = fractal.Mandelbrot(100)
    #frac = fractal.BurningShip(100)
    frac = fractal.JuliaSet(100)

    frac_image = fractal_image.FractalImage(frac, x_dim, y_dim, scale, center)
    frac_image.draw()
    frac_image.save()


if __name__ == "__main__":
    main()
