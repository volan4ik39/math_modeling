import matplotlib.pyplot as plt
import numpy as np
def circle_plotter(R=10):
    x = np.arange(-1*R, 1*R, 0.1)
    y = np.arange(-2*R, 2*R, 0.1)
    a = 5
    b = 2
     X, Y = np.meshgrid(x, y)
    fxy = ((X**2) / (a**2)) + ((Y**2) / (b**2)) -1
    plt.contour(X, Y, fxy, levels=[0])
    plt.axis('equal')
    plt.savefig('fig_6.png')
if __name__ == '__main__':
    circle_plotter()