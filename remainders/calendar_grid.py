import numpy as np
import matplotlib.pyplot as plt


def adjust_x(axs):
    days = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
    iter_days = iter(days)

    for ax in axs:
        ax.grid(zorder=5,axis='y')
        ax.set_xlabel(next(iter_days))
        ax.tick_params(left=False, bottom=False, labelbottom=False)
        ax.label_outer()
    return axs


def adjust_y(axs):
    axs[0].set_ylim(23, 6)
    times = [*range(6, 24)]
    hours = list(map(str, times.copy()))
    half_hours = list(map(str, times.copy()))
    for i in range(len(times)):
        hours[i] += ":00"
        half_hours[i] += ":30"
    spaces = np.full(len(times), "").tolist()
    y_labels = np.array(list(zip(hours, spaces, half_hours, spaces))).flatten()
    axs[0].set_yticks(np.linspace(6, 23, 69), labels=y_labels[:-3])
    return axs


def create():
    fig = plt.figure(figsize=(11.69, 8.27))
    gs = fig.add_gridspec(1, 7, wspace=0)
    axs = gs.subplots(sharex=False, sharey=True)
    axs = adjust_y(axs)
    axs = adjust_x(axs)
    return fig, axs
