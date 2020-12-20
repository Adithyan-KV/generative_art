import matplotlib.pyplot as plt
import matplotlib.cbook
import numpy as np
import random
import time
import warnings

warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)


def main():
    generate_walk_image_seq(6, 1000)
    # generate_multiple_walk_image(10, 10000)


def timer(func):
    def time_it(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        t = end - start
        print(f'time taken:{t}s')
        return result
    return time_it


def generate_multiple_walk_image(num_walks, steps):
    for _ in range(num_walks):
        x, y = random_walk_2d(steps)
        plt.plot(x, y)
    plt.axis('off')
    plt.show()


@timer
def generate_walk_image_seq(num_walks, steps):
    walks = []
    for _ in range(num_walks):
        x, y = random_walk_2d(steps)
        walks.append([x, y])
        colors = ['#efb08c', '#d35d6e', '#5aa469']
    for i in range(steps):
        if (i % 100) == 0:
            print(f'{(i/steps)*100}% completed')

        for j in range(num_walks):
            walk = walks[j]
            plt.plot(walk[0][:i], walk[1][:i])
        ax = plt.axes()
        ax.set_facecolor('#f8d49d')
        plt.axis('off')
        plt.xlim(-100, 100)
        plt.ylim(-100, 100)
        plt.savefig(f'./test_images/walk_{i}.png')
        plt.cla()


def random_walk_1d(steps):
    x_values = np.arange(0, steps, 1)
    step_values = np.random.choice([-1, 1], size=steps)
    y_values = np.cumsum(step_values)
    return x_values, y_values


def random_walk_2d(steps):
    step_choices = [-1, 0, 1]
    x_steps = np.random.choice(step_choices, size=steps)
    y_steps = np.random.choice(step_choices, size=steps)
    x_values = x_steps.cumsum()
    y_values = y_steps.cumsum()
    return x_values, y_values


if __name__ == "__main__":
    main()
