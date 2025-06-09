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

    def add_track(self, name, shape=(1, 21), rowspan=1, colspan=3):
        ax = plt.subplot2grid(shape,
                              loc=tuple(self.loc),
                              rowspan=rowspan,
                              colspan=colspan,
                              sharey=self.sharey)
        self.axes[name] = ax
        # Increment loc after adding axes
        self.loc[1] += 3
        # Update sharey after first axes, always start with depth
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

    def build_data_track(self):
        if self.config is None:
            print("Please build config.")
        else:
            for key in self.config.keys():
                print(key, "key added")
                self.add_track(key)

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
my_plot.build_data_track()
my_plot.save_plot()
print(my_plot.axes)
