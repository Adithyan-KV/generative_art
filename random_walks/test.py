import matplotlib.pyplot as plt
import numpy as np
import random
import time


def main():
    steps = 200
    num_walks = 3
    walks = []
    for _ in range(num_walks):
        x, y = random_walk_2d(steps)
        walks.append([x, y])
        colors = ['#fc8621', '#c24914', '#682c0e']
    for i in range(steps):
        for j in range(num_walks):
            walk = walks[j]
            plt.plot(walk[0][:i], walk[1][:i], color=colors[j])
        ax = plt.axes()
        ax.set_facecolor('#f9e0ae')
        plt.axis('off')
        plt.xlim(-100, 100)
        plt.ylim(-100, 100)
        plt.savefig(f'./test_images/walk_{i}.png')


def timer(func):
    def time_it(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        t = end - start
        print(t)
        return result
    return time_it


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
