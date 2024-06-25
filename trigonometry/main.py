import math
import os

import matplotlib.pyplot as plt
import numpy as np


def main():
    X = np.arange(-1 * math.pi * 4, math.pi * 4, 0.05)

    tan = np.tan(X)
    sin = np.sin(X)
    cos = np.cos(X)

    cot = 1 / np.tan(X)
    sec = 1 / np.cos(X)
    cosec = 1 / np.sin(X)

    plt.plot(X, tan, color="C0", label="tan(x)")
    plt.plot(X, sin, color="C1", label="sin(x)")
    plt.plot(X, cos, color="C2", label="cos(x)")

    plt.plot(X, cot, color="C3", label="cot(x)")
    plt.plot(X, sec, color="C4", label="sec(x)")
    plt.plot(X, cosec, color="C5", label="cosec(x)")

    ax = plt.gca()
    ax.set_ylim([-2, 2])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(axis="x")
    plt.legend()

    output_file = os.path.join(os.path.dirname(__file__), "output.png")
    plt.savefig(output_file)
    plt.show()


if __name__ == "__main__":
    main()
