from helpers import day_to_string, time_formatter
from uuid import uuid4
from matplotlib.patches import Rectangle

# TODO: Assert that start_time > stop_time and that time is between 0 and 24


class CalendarEntry:
    def __init__(self, start_time=12, stop_time=13, day=0, title='*No title*', description='*No Description*',
                 color='#ff1e1e', edge='#000000'):
        self.start = start_time
        self.stop = stop_time
        self.day = day

        self.title = title
        self.description = description

        self.color = color
        self.edge = edge

        self.id = uuid4()
        self.plot_rect = None
        self.plot_text = None

    def __str__(self):
        print(self.plot_rect)
        return f"Event title: {self.title} \n" \
               f'Description: "{self.description}"\n' \
               f"Scheduled on {day_to_string(self.day)} " \
               f"from {time_formatter(self.start)} to {time_formatter(self.stop)}\n" \
               f"Color: " + self.color
