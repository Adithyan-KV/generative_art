import numpy as np
import matplotlib.pyplot as plt
import warnings
import matplotlib.cbook
import matplotlib.colors
import random

warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)


def main():
    make_streaks_art(200, 1000)


def make_streaks_art(number, steps):
    base_color_hsv = get_random_base_color()
    base_hue = base_color_hsv[0]
    base_value = base_color_hsv[2]
    base_color_rgb = matplotlib.colors.hsv_to_rgb(base_color_hsv)
    sat_array = get_nearby_colors(base_color_hsv, number, 0.3)
    for i in range(number):
        x, y = random_walk(steps)
        color_hsv = [base_hue, sat_array[i], base_value]
        color_rgb = matplotlib.colors.hsv_to_rgb(color_hsv)
        plt.plot(x, y, color=color_rgb)
    ax = plt.axes()
    ax = plt.axes()
    ax.set_facecolor(base_color_rgb)
    plt.axis('off')
    plt.xlim(0, steps)
    plt.ylim(-int(steps / 2), int(steps / 2))
    plt.savefig(f'./test_images/streak.png')


def get_random_base_color():
    hsv = np.random.uniform(0, 1, 3)
    return hsv


def get_nearby_colors(base_color, number, spread):
    saturations = np.random.normal(base_color[1], spread, number)
    saturations = saturations.clip(0, 1)
    return saturations


def random_walk(steps):
    y_start = random.randint(-int(steps / 2), steps / 2)
    x_values = np.arange(0, steps, 1)
    step_values = np.random.choice([-1, 0, 1], size=steps)
    y_values = np.cumsum(step_values) + y_start * np.ones_like(x_values)
    return x_values, y_values


if __name__ == "__main__":
    main()
