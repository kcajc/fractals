import matplotlib.pyplot as plt
import numpy as np


# Define the function for iteration: x_n+1 = x_n^2 + c
class JuliaFunction:
    def __init__(self, c):
        self.c = c

    def __call__(self, z):
        # Safeguard to avoid overflow
        threshold = 1e10
        return np.where(np.abs(z) < threshold, z**2 + self.c, z)


def julia_set(func, xlim=(-2, 2), ylim=(-2, 2), width=800, height=800, max_iter=300):
    """
    :param func: Function to apply in the iteration x_n+1 = func(x_n, c).
    :param xlim: x-axis limits as a tuple (min, max).
    :param ylim: y-axis limits as a tuple (min, max).
    :param width: Image width in pixels.
    :param height: Image height in pixels.
    :param max_iter: Maximum number of iterations.
    """
    x = np.linspace(xlim[0], xlim[1], width)
    y = np.linspace(ylim[0], ylim[1], height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    img = np.zeros(Z.shape, dtype=float)
    for _ in range(max_iter):
        Z = func(Z)
        mask = np.abs(Z) < 1000
        img += mask

    plt.figure(figsize=(10, 10))
    plt.imshow(img, extent=(xlim[0], xlim[1], ylim[0], ylim[1]), cmap="plasma")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.title("Julia Set")
    plt.show()


if __name__ == "__main__":
    # Change this value to explore different Julia sets
    c = complex(-0.4, -0.6)
    Q_c = JuliaFunction(c)
    julia_set(Q_c)
