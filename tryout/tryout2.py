from Calendar import Calendar
from CalendarEntry import CalendarEntry
from matplotlib.patches import Rectangle

entries = [
    CalendarEntry(start_time=13, stop_time=14, day=0, title='Second'),
    CalendarEntry(start_time=11, stop_time=12, day=0, title='First'),
    CalendarEntry(start_time=7, stop_time=9, day=3, title='Last'),
    CalendarEntry(start_time=9, stop_time=10, day=1, title='Third')
]


# We can add and remove entries -> part of GUI application!
calendargrid = Calendar()

for entry in entries:
    calendargrid.add_entry(entry)

calendargrid.remove_entry(calendargrid.entry_list[entries[0].id])
calendargrid.show()
