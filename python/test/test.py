import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os


while True:
    degree = input("input degree:")
    os.system("clear")
    rad = round(float(degree) / 180 * np.pi, 3)

    print(f"rad: {rad}")
