import matplotlib.pyplot as plt
from utils.read_data import read_data
from log_config.log_config import build_config


class LogPlot:
    def __init__(self, figsize=(15, 10)):
        self.fig, self.ax = plt.subplots(figsize=figsize)
        self.axes = {}
        self.loc = [0, 0]
        self.sharey = None
        self.data = {}
        self.config = None
        self.log_order

    def add_track(self, name, shape=(1, 21), rowspan=1, colspan=3):
        ax = plt.subplot2grid(shape,
                              loc=tuple(self.loc),
                              rowspan=rowspan,
                              colspan=colspan,
                              sharey=self.sharey)
        self.axes[name] = ax
        # Increment loc after adding axes
        self.loc[1] += 3
        # Update sharey after first axes, so all logs share 1 axes
        if self.sharey is None:
            self.sharey = self.axes[name]
        return ax

    def get_ax(self, name):
        return self.axes.get(name)

    def get_data(self, file_name, filepath):
        if file_name in self.data.keys():
            print("Data already added.")
        else:
            self.data[file_name] = read_data(filepath)
            print("Added well log to data dictionary.")

    def build_config(self):
        for value in self.data.values():
            config = build_config(value)
        self.config = config

    def build_data_tracks(self):
        if self.config is None:
            print("Please build config.")
        else:
            # Think about adding dynamic shaping
            for key in self.config.keys():
                self.add_track(key)

    def add_data_to_track(self):
        for key, axes in self.axes.items():
            if key in self.config.keys():
                axes.plot(self.config[key]["data"],
                          self.config['M__DEPTH']["data"],
                          self.config[key]["color"],
                          linewidth=0.5)
                axes.set_xlabel(key)
                axes.xaxis.label.set_color(self.config[key]["color"])
                axes.set_xlim(self.config[key]["xlim"])
                axes.set_ylabel("Depth (m)")
                axes.tick_params(axis='x', colors=self.config[key]["color"])
                axes.spines["top"].set_edgecolor(self.config[key]["color"])
                axes.title.set_color(self.config[key]["color"])
                axes.set_xticks(self.config[key]["xticks"])
                axes.text(0.05, 1.04, 0,
                          color=self.config[key]["color"],
                          horizontalalignment='left',
                          transform=axes.transAxes)
                axes.text(0.95, 1.04, 150,
                          color=self.config[key]["color"],
                          horizontalalignment='right',
                          transform=axes.transAxes)
                axes.set_xticklabels([])

    def set_order(self, log_order):
        self.log_order = log_order

    def save_plot(self, path="output/figure.png"):
        self.fig.delaxes(self.ax)
        self.fig.tight_layout()
        self.fig.subplots_adjust(wspace=0)
        self.fig.savefig(path)

    def show_plot(self):
        self.fig.show()


# my_plot = LogPlot()

my_plot = LogPlot()
my_plot.get_data("WA1", "data/WA1.txt")
my_plot.build_config()
my_plot.build_data_tracks()
my_plot.add_data_to_track()
my_plot.save_plot()
