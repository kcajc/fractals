import matplotlib.pyplot as plt
import numpy as np


def mandelbrot_set(center=(0, 0), zoom=1, width=800, height=800, max_iter=300):
    """
    Generate and plot the Mandelbrot set.

    :param center: Center point in the complex plane around which to generate the set.
    :param zoom: Zoom level for the visualization.
    :param width: Image width in pixels.
    :param height: Image height in pixels.
    :param max_iter: Maximum number of iterations.
    """
    scale = 2 / zoom
    xlim = (center[0] - scale, center[0] + scale)
    ylim = (center[1] - scale, center[1] + scale)

    x = np.linspace(xlim[0], xlim[1], width)
    y = np.linspace(ylim[0], ylim[1], height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros(C.shape, dtype=complex)
    img = np.zeros(C.shape, dtype=float)

    for _ in range(max_iter):
        mask = np.abs(Z) < 2
        Z[mask] = Z[mask] ** 2 + C[mask]
        img[mask] += 1

    plt.figure(figsize=(10, 10))
    plt.imshow(
        np.log(img + 1),
        extent=(xlim[0], xlim[1], ylim[0], ylim[1]),
        cmap="plasma",
        origin="lower",
    )
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.title(f"Mandelbrot Set (Center: {center}, Zoom: {zoom}x)")
    plt.show()


if __name__ == "__main__":
    center = (-0.5, 0)
    zoom = 1  # Increase to zoom in, decrease to zoom out
    mandelbrot_set(center=center, zoom=zoom)
