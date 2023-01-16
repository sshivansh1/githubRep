import numpy as np
import matplotlib.pyplot as plt

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def PlotTest() -> None:
    t = np.arange(0.0, 2.0, 0.01)
    s = np.sin(2 * np.pi * t)
    fig, ax = plt.subplots()
    ax.plot(t, s)
    ax.set(xlabel='Time(s)', ylabel='Voltage(mV)', title='Simple, huh?')
    ax.grid()
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    PlotTest()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
