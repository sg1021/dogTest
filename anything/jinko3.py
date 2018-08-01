import numpy as np
import matplotlib.pyplot as plt

def plot_function(func):
    x = np.linspace(-6,6,100)
    y = func(x)

    plt.plot(x,y)
    plt.grid()
    plt.show()

def step(x):
    return np.array(x > 0, dtype=np.int)

plot_function(step)

