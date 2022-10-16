from CalendarGrid import CalendarGrid
from CalendarEntry import CalendarEntry
from matplotlib.patches import Rectangle

entries = [
    CalendarEntry(start_time=13, stop_time=14, day=0, title='Second'),
    CalendarEntry(start_time=11, stop_time=12, day=0, title='First'),
    CalendarEntry(start_time=7, stop_time=9, day=3, title='Last'),
    CalendarEntry(start_time=9, stop_time=10, day=1, title='Third')
]


sorted_entries = sorted(entries, key=lambda ent: (ent.day, ent.start))

for i in sorted_entries:
    print(i)






