import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist


a = 1


def pltz1():
    def e(t):
        return np.exp(t)

    fig = plt.figure(figsize=(10, 8), dpi=80)
    ax1 = axisartist.Subplot(fig, 111)
    fig.add_axes(ax1)
    ax1.axis[:].set_visible(False)
    ax1.axis["x"] = ax1.new_floating_axis(0, 0)
    ax1.axis["x"].set_axisline_style("->", size=1.0)
    ax1.axis["y"] = ax1.new_floating_axis(1, 0)
    ax1.axis["y"].set_axisline_style("->", size=1.0)
    ax1.axis["x"].set_axis_direction("top")
    ax1.axis["y"].set_axis_direction("right")

    plt.xlabel("t")
    plt.ylabel("x(t)")

    x = np.arange(-3, 3, 0.1)

    plt.plot(x, e(a * x))
    plt.plot(x, e(-a * x))
    plt.plot(x, e(0 * x))
    plt.show()

def pltz2():
    def x(t):
        return np.exp(-t) * np.cos(8 * t - 200)

    fig = plt.figure(figsize=(10, 8), dpi=80)
    ax1 = axisartist.Subplot(fig, 111)
    fig.add_axes(ax1)

    ax1.axis[:].set_visible(False)
    ax1.axis["x"] = ax1.new_floating_axis(0, 0)

    ax1.axis["x"].set_axisline_style("->", size=1.0)
    ax1.axis["y"] = ax1.new_floating_axis(1, 0)
    ax1.axis["y"].set_axisline_style("->", size=1.0)
    ax1.axis["x"].set_axis_direction("top")
    ax1.axis["y"].set_axis_direction("right")

    plt.xlim(-5, 5)
    plt.ylim(-100, 100)

    t = np.arange(-5, 5, 0.01)
    plt.plot(t, x(t), 'r-')
    plt.title('x(t)=cos(ωt+θ)*e**(σt)')
    plt.xlabel('t')
    plt.show()

def pltz3():
    import math

    fig = plt.figure(figsize=(10, 8), dpi=80)
    ax1 = axisartist.Subplot(fig, 111)
    fig.add_axes(ax1)

    ax1.axis[:].set_visible(False)
    ax1.axis["x"] = ax1.new_floating_axis(0, 0)

    ax1.axis["x"].set_axisline_style("->", size=1.0)
    ax1.axis["y"] = ax1.new_floating_axis(1, 0)
    ax1.axis["y"].set_axisline_style("->", size=1.0)
    ax1.axis["x"].set_axis_direction("top")
    ax1.axis["y"].set_axis_direction("right")

    x = np.arange(-4, 4)

    y = np.sin(x)

    plt.stem(x, y, 'b')
    plt.show()

def pltz4():
    def x(t):
        return np.cos(8 * t - 200)

    fig = plt.figure(figsize=(10, 8), dpi=80)
    ax1 = axisartist.Subplot(fig, 111)
    fig.add_axes(ax1)

    ax1.axis[:].set_visible(False)
    ax1.axis["x"] = ax1.new_floating_axis(0, 0)

    ax1.axis["x"].set_axisline_style("->", size=1.0)
    ax1.axis["y"] = ax1.new_floating_axis(1, 0)
    ax1.axis["y"].set_axisline_style("->", size=1.0)
    ax1.axis["x"].set_axis_direction("top")
    ax1.axis["y"].set_axis_direction("right")

    t = np.arange(-4, 4, 0.01)

    plt.plot(t, x(t))
    plt.show()

def button():
    import tkinter as tk
    from tkinter import ttk

    win = tk.Tk()

    #win.geometry("600x600")
    win.title('GUI004')

    aLabel = ttk.Label(win, text='已有信号类型')
    aLabel.grid(column=0, row=0)

    action1 = ttk.Button(win, text='连续时间复指数信号',command=pltz1)
    action1.grid(column=1, row=0)

    action2 = ttk.Button(win, text='幅度增长的正弦信号', command=pltz2)
    action2.grid(column=1, row=1)

    action3 = ttk.Button(win, text='离散正弦信号', command=pltz3)
    action3.grid(column=1, row=2)

    action4 = ttk.Button(win, text='连续正弦信号', command=pltz4)
    action4.grid(column=1, row=3)

    win.mainloop()

button()