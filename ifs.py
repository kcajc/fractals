import matplotlib.pyplot as plt
import numpy as np


def transform_point(point, scale, rotation, shift):
    """
    Apply scale, rotation, and shift to a 2D point.

    :param point: The point to transform.
    :param scale: Scaling factor.
    :param rotation_radians: Rotation angle in radians.
    :param shift: Shift vector.
    :return: Transformed point.
    """
    rotation_matrix = np.array(
        [
            [np.cos(rotation), -np.sin(rotation)],
            [np.sin(rotation), np.cos(rotation)],
        ]
    )

    scaled_rotation_matrix = scale * rotation_matrix

    transformed_point = scaled_rotation_matrix @ point + shift
    return transformed_point


def iterated_function_system(functions, initial_points, iterations):
    """
    :param functions: List of functions, each accepting a point as argument.
    :param initial_points: Initial set of points to transform.
    :param iterations: Number of iterations to apply the transformations.
    :return: Final set of points after all transformations.
    """
    points = initial_points
    for _ in range(iterations):
        new_points = []
        for func in functions:
            for point in points:
                new_points.append(func(point))
        points = new_points
    return points


if __name__ == "__main__":
    ifs = [
        lambda p: transform_point(p, 0.5, 0, [0, 0]),
        lambda p: transform_point(p, 0.5, np.pi / 4, [0, 1 / 2]),
        lambda p: transform_point(p, 0.5, -np.pi / 4, [0, 1 / 2]),
    ]

    # Initial space - a square
    # initial_points = np.array([[x, y] for x in np.linspace(0, 1, 100) for y in np.linspace(0, 1, 100)])
    # Initial space - a line segment
    initial_points = np.array([[0, y] for y in np.linspace(0, 1, 1000)])

    iterations = 5
    final_points = iterated_function_system(ifs, initial_points, iterations)

    plt.scatter([p[0] for p in final_points], [p[1] for p in final_points], s=1)
    plt.axis("equal")
    plt.show()
