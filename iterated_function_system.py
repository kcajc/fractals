import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np


def transform_point(point, scale, rotation, shift):
    rotation_matrix = np.array(
        [[np.cos(rotation), -np.sin(rotation)], [np.sin(rotation), np.cos(rotation)]]
    )
    scaled_rotation_matrix = scale * rotation_matrix
    transformed_point = np.dot(scaled_rotation_matrix, point) + shift
    return transformed_point


def apply_transformations(vertices, transformation_functions):
    transformed_polygons = []
    for transformation in transformation_functions:
        transformed_polygon = [transformation(vertex) for vertex in vertices]
        transformed_polygons.append(transformed_polygon)
    return transformed_polygons


def iterated_function_system(vertices, transformation_functions, iterations):
    point_count = (len(vertices) * len(transformation_functions)) ** iterations
    if point_count > 1e7:
        print(
            f"Warning: The number of points generated ({point_count}) is very large. "
            "Consider reducing the number of iterations."
        )
    polygons = [vertices]
    for _ in range(iterations):
        new_polygons = []
        for polygon in polygons:
            new_polygons.extend(
                apply_transformations(polygon, transformation_functions)
            )
        polygons = new_polygons
    return polygons


def plot_polygons(polygons, axis=False):
    _, ax = plt.subplots()
    min_x, min_y = np.inf, np.inf
    max_x, max_y = -np.inf, -np.inf

    for polygon in polygons:
        poly_np = np.array(polygon)
        min_x, min_y = min(min_x, poly_np[:, 0].min()), min(min_y, poly_np[:, 1].min())
        max_x, max_y = max(max_x, poly_np[:, 0].max()), max(max_y, poly_np[:, 1].max())

        patch = patches.Polygon(
            polygon,
            closed=True,
            linewidth=1,
            edgecolor="lightblue",
            facecolor="lightblue",
        )
        ax.add_patch(patch)

    ax.set_xlim(min_x - 0.1 * abs(min_x), max_x + 0.1 * abs(max_x))
    ax.set_ylim(min_y - 0.1 * abs(min_y), max_y + 0.1 * abs(max_y))
    ax.set_aspect("equal")
    if not axis:
        plt.axis("off")
    plt.show()


if __name__ == "__main__":

    # Example: Dragon curve
    horizontal_line = np.array([[0, 0], [1, 0]])
    dragon_curve_ifs = [
        lambda p: transform_point(p, 1 / np.sqrt(2), np.pi / 4, [0, 0]),
        lambda p: transform_point(p, 1 / np.sqrt(2), 3 * np.pi / 4, [1, 0]),
    ]

    # Example: Antlers
    vertical_line = np.array([[0, 0], [0, 1]])
    antlers = [
        lambda p: transform_point(p, 0.5, 0, [0, 0]),
        lambda p: transform_point(p, 0.5, np.pi / 4, [0, 1 / 2]),
        lambda p: transform_point(p, 0.5, -np.pi / 4, [0, 1 / 2]),
    ]

    # Example: Sierpinski triangle
    triangle = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) / 2]])
    sierpinski_triangle_ifs = [
        lambda p: transform_point(p, 0.5, 0, [0, 0]),
        lambda p: transform_point(p, 0.5, 0, [0.5, 0]),
        lambda p: transform_point(p, 0.5, 0, [0.25, np.sqrt(3) / 4]),
    ]

    # Example: Sierpinski carpet
    square = np.array(
        [
            [0, 0],
            [1, 0],
            [1, 1],
            [0, 1],
        ]
    )
    sierpinski_carpet_ifs = [
        lambda p: transform_point(p, 1 / 3, 0, [0, 0]),
        lambda p: transform_point(p, 1 / 3, 0, [1 / 3, 0]),
        lambda p: transform_point(p, 1 / 3, 0, [2 / 3, 0]),
        lambda p: transform_point(p, 1 / 3, 0, [0, 1 / 3]),
        lambda p: transform_point(p, 1 / 3, 0, [2 / 3, 1 / 3]),
        lambda p: transform_point(p, 1 / 3, 0, [0, 2 / 3]),
        lambda p: transform_point(p, 1 / 3, 0, [1 / 3, 2 / 3]),
        lambda p: transform_point(p, 1 / 3, 0, [2 / 3, 2 / 3]),
    ]

    # Example: Koch's snowflake
    koch_snowflake_ifs = [
        lambda p: transform_point(p, 1 / 3, 0, [0, 0]),
        lambda p: transform_point(p, 1 / 3, np.pi / 3, [1 / 3, 0]),
        lambda p: transform_point(p, 1 / 3, -np.pi / 3, [0.5, np.sqrt(3) / 6]),
        lambda p: transform_point(p, 1 / 3, 0, [2 / 3, 0]),
    ]

    # Pick the initial vertices, iterated function system and iterations
    initial_vertices = horizontal_line
    transformations = dragon_curve_ifs
    iterations = 9

    final_polygons = iterated_function_system(
        initial_vertices, transformations, iterations
    )
    plot_polygons(final_polygons)
