import matplotlib.pyplot as plt
import numpy as np
import random
import time


def main():
    x_1, y_1 = random_walk_1d(1000)
    x_2, y_2 = random_walk_1d(1000)
    x_3, y_3 = random_walk_1d(1000)
    plt.plot(x_1, y_1)
    plt.plot(x_2, y_2)
    plt.plot(x_3, y_3)
    plt.show()


@timer
def random_walk_1d(steps):
    x_values = []
    y_values = []
    steps = 10000
    for i in range(steps):
        x_values.append(i)
        step = random.choice([1, -1])
        y_values.append(step)
    y_values = np.array(y_values)
    y_values = np.cumsum(y_values)
    return x_values, y_values


def timer(func):
    def time_it(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        t = end - start
        print(t)
        return result
    return time_it


if __name__ == "__main__":
    main()
