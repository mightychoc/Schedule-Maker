import matplotlib.pyplot as plt
from remainders.calendar_grid import create
from src.calendar.entries import entry


if __name__ == "__main__":
    # Create fundamental structure
    fig, axs = create()

    # Define params
    edge_vl, fill_vl = "#178CA4", "#18B7BE"
    edge_u, fill_u = "#B74803", "#CC6D3D"
    edge_hb, fill_hb = "#9B0000", "#DD4A48"
    edge_train, fill_train = "#2B7A0B", "#5BB318"  # "#7DCE13"
    name = "Stundenplan_HS22"

    # Monday
    axs = entry(8, 10, 0, "Tim?", axs, edge_hb, fill_hb)
    axs = entry(14.25, 16, 0, "Disk Math\nU. Maurer\nETA F 5/ETF E 1", axs, edge_vl, fill_vl)
    axs = entry(20, 22.25, 0, "2. Liga", axs, edge_hb, fill_hb)

    # Tuesday
    axs = entry(8, 10, 1, "Tim?", axs, edge_hb, fill_hb)
    axs = entry(14.25, 16, 1, "Disk Math\nHG E 33.5", axs, edge_u, fill_u)
    axs = entry(18, 19.5, 1, "FU 14", axs, edge_train, fill_train)

    # Wednesday
    axs = entry(8, 10, 2, "Tim?", axs, edge_hb, fill_hb)
    axs = entry(14.25, 16, 2, "Disk Math\nU. Maurer\nETA F 5/ETF E 1", axs, edge_vl, fill_vl)
    axs = entry(20, 22, 2, "2. Liga", axs, edge_hb, fill_hb)

    # Thursday
    axs = entry(7.5, 9.5, 3, "Tim?", axs, edge_hb, fill_hb)
    axs = entry(18, 19.5, 3, "FU 14", axs, edge_train, fill_train)
    axs = entry(21, 22.5, 3, "3. Liga", axs, edge_hb, fill_hb)

    # Friday
    axs = entry(7.5, 9.5, 4, "Tim?", axs, edge_hb, fill_hb)

    # Saturday

    # Sunday

    # plt.savefig("/Users/joaquin/PyCharm_Projects/Stundenplaner/out/" + name, format="pdf")
    plt.show()
