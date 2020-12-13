import matplotlib.pyplot as plt
import numpy as np
import random
import time


def main():
    for _ in range(3):
        x, y = random_walk_1d(10000)
        plt.plot(x, y)
    plt.show()


def timer(func):
    def time_it(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        t = end - start
        print(t)
        return result
    return time_it


@ timer
def random_walk_1d(steps):
    x_values = np.arange(0, steps, 1)
    step_values = np.random.choice([-1, 1], size=steps)
    y_values = np.cumsum(step_values)
    return x_values, y_values


if __name__ == "__main__":
    main()
