from matplotlib.patches import Rectangle

def write_entry(start, stop, day, message, axs):
    left, width = 0.05, 0.9
    right = left + width
    # top, height = start, stop-start
    # bottom = top + height

    axs[day].text(0.5 * (left + right), 0.5 * (start + stop), message,
                  horizontalalignment='center', verticalalignment='center',
                  transform=axs[day].transData, zorder=15)
    return axs


def create_rectangle(start, stop, day, axs, edge, fill):
    left, width = 0.05, 0.9
    rect = Rectangle((left, start), width, stop - start,
                     facecolor=fill, edgecolor=edge, lw=2,
                     alpha=0.8, zorder=10)
    rect.set_transform(axs[day].transData)
    rect.set_clip_on(False)
    axs[day].add_patch(rect)
    return axs


def entry(start, stop, day, message, axs, edge="#E59A59", fill="#FFD5AF"):
    axs = create_rectangle(start, stop, day, axs, edge, fill)
    axs = write_entry(start, stop, day, message, axs)
    return axs
