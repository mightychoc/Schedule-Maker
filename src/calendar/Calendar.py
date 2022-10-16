from CalendarGrid import CalendarGrid
from matplotlib.patches import Rectangle


# TODO: Make left/width adaptive for multiple entries

class Calendar(CalendarGrid):
    def __init__(self):
        super().__init__(days=7, calendar_start=6, calendar_stop=23, hour_format='full', title='My Week', title_size=24)
        self.entry_list = []

    def add_entry(self, entry):
        left, width = 0.05, 0.9
        rect = Rectangle((left, entry.start), width, entry.stop - entry.start,
                         facecolor=entry.color, edgecolor=entry.edge, lw=2,
                         alpha=0.8, zorder=10)
        rect.set_transform(self.axs[entry.day].transData)
        rect.set_clip_on(False)
        self.axs[entry.day].add_patch(rect)
        self.write_entry_text(entry)

    def remove_entry(self, entry):
        pass

    def write_entry_text(self, entry):
        left, width = 0.05, 0.9
        right = left + width
        # top, height = start, stop-start
        # bottom = top + height

        self.axs[entry.day].text(0.5 * (left + right), 0.5 * (entry.start + entry.stop),
                                 r'$\bf{' + entry.title + '}$\n' + entry.description, fontdict={'family': 'monospace'},
                                 ha='center', va='center',
                                 transform=self.axs[entry.day].transData, zorder=15)

    # Sorts all entries in ascending order by day and within a day by start_time
    def sort_entry_list(self):
        return sorted(self.entry_list, key=lambda ent: (ent.day, ent.start))
