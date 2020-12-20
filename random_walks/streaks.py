import numpy as np
import matplotlib.pyplot as plt
import warnings
import matplotlib.cbook
import random

warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)


def main():
    make_streaks_art(300, 1000)


def make_streaks_art(number, steps):
    for _ in range(number):
        x, y = random_walk(steps)
        plt.plot(x, y)
    ax = plt.axes()
    ax = plt.axes()
    ax.set_facecolor('#f8d49d')
    # plt.axis('off')
    plt.xlim(0, steps)
    plt.ylim(-int(steps / 2), int(steps / 2))
    plt.show()


def random_walk(steps):
    y_start = random.randint(-int(steps / 2), steps / 2)
    x_values = np.arange(0, steps, 1)
    step_values = np.random.choice([-1, 0, 1], size=steps)
    y_values = np.cumsum(step_values) + y_start * np.ones_like(x_values)
    return x_values, y_values


if __name__ == "__main__":
    main()
