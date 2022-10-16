from matplotlib.pyplot import figure, show
from matplotlib.patches import Rectangle
from numpy import array, linspace
from helpers import time_formatter


class CalendarGrid:

    # TODO: Doesn't works for half-hour calendar_start/_stop! (linspace needs integers)
    #   Maybe check if it is int or not, if it is float, adjust ticks/labels s.t. it works (i.e. create labels/ticks
    #   from an hour earlier and then slice the array accordingly)

    # TODO: Make all font-sizes adjustable

    def __init__(self, days=7, calendar_start=6, calendar_stop=23, hour_format='full', title='My Week', title_size=24):
        # Necessary information to create calendar
        self.days = days
        self.start = calendar_start
        self.stop = calendar_stop
        self.hour_format = hour_format

        # Create basic figure with no_of_days-many subplots
        fig = figure(figsize=(11.69, 8.27))
        gs = fig.add_gridspec(1, self.days, wspace=0)
        axs = gs.subplots(sharex=False, sharey=True)
        self.fig = fig
        self.axs = axs

        # TODO Style Settings (create style sheet for titles, ticks, background etc?)
        self.fig.suptitle(title, fontsize=title_size)
        self.adjust_axes()

    def adjust_axes(self):

        # Configuration of y-ticks
        self.axs[0].set_ylim(self.stop, self.start)
        hour_linspace = linspace(self.start, self.stop, (self.stop - self.start) + 1)

        if self.hour_format == 'full':
            self.axs[0].set_yticks(hour_linspace, labels=time_formatter(hour_linspace))
            self.axs[0].set_yticks((hour_linspace+0.5)[:-1], minor=True)

        elif self.hour_format == 'half':
            self.axs[0].set_yticks(hour_linspace, labels=time_formatter(hour_linspace))
            self.axs[0].set_yticks((hour_linspace[:-1]+0.5), labels=time_formatter(hour_linspace[:-1]+0.5), minor=True)

        elif self.hour_format == 'quarter':
            # Zip y-tick positions and labels
            half_and_full_hours = array(list(zip(hour_linspace, hour_linspace+0.5))).flatten()[:-1]
            half_and_full_hours_labels = time_formatter(half_and_full_hours)
            quarter_hours = array(list(zip(hour_linspace+0.25, hour_linspace+0.75))).flatten()[:-2]

            self.axs[0].set_yticks(half_and_full_hours, labels=half_and_full_hours_labels)
            self.axs[0].set_yticks(quarter_hours, minor=True)

        else:
            raise ValueError("Hour format is not 'full', 'half' or 'quarter'!")

        days = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
        if self.days != 7:
            days = days[:-(7 - self.days)]

        iter_days = iter(days)
        for ax in self.axs:
            # x-axis configuration
            ax.set_xlabel(next(iter_days))

            # y-axis configuration
            # Remove quarter-hour ticks and x-ticks
            ax.tick_params(axis='y', which='major', labelsize=10)
            ax.tick_params(left=False, bottom=False, labelbottom=False)
            ax.tick_params(axis='y', which='minor', length=0, labelsize=8)
            # Adjust grid
            ax.grid(zorder=5, axis='y')
            ax.grid(zorder=5, axis='y', which='minor', linestyle='--')

            ax.label_outer()

    # TODO: Watch out if figure is closed or not! Also, check which one is correct to use
    @classmethod
    def show(cls):
        show()

    # @staticmethod
    # def show():
        # show()

    # def show(self):
        # self.fig.show()

    def __str__(self):
        return "The Calendar"

