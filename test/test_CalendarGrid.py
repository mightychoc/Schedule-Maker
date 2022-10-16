from CalendarEntry import CalendarEntry
from CalendarGrid import CalendarGrid


def test_create_grid():
    calendar = CalendarGrid(days=5, hour_format='full')
    # print(calendar)
    calendar.show()


def test_create_entry():
    calendar = CalendarGrid()
    entry = CalendarEntry(start_time=9, stop_time=11, day=1,
                        title='Title', description='Some Text\nand more text\nand more text',
                        color='#FFD5AF')

    calendar.add_entry(entry)
    calendar.show()

#test_create_grid()
test_create_entry()
