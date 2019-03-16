import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_hist(data, value, title, xlabel, ylabel, ylim, colors, bin=10, metrics=True):
    """
    "   data:    list of dataframes
    "   value:   value from dataframes to be plotted
    "   title:   title of histogram
    "   xlabel:  x axis label
    "   ylabel:  y axis label
    "   ylim:    y limits 
    "   colors:  list of colors for each dataframe's bars
    "   bin:     number of histogram bins
    "   metrics: display mean/median on histogram
    """

    metric_txt = ""
    fig, ax = plt.subplots()
    bins = np.linspace(-1, 1, bin)
    patches = []
    for i, d in enumerate(data):
        name = d.name
        mean = "Mean: %.4f" % d[value].mean()
        median = "Median: %.4f" % d[value].median()
        metric_txt = metric_txt + name + "\n  " + mean + "\n  " + median + "\n"

        d.hist(column=value, bins=bins, grid=False, ax=ax, color=colors[i])
        patches.append(mpatches.Patch(color=colors[i], label=name))

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(handles=patches)

    ax.set_ylim([0,ylim])
    ax.text(0.05, 0.95, metric_txt, verticalalignment="top", transform=ax.transAxes)

    plt.savefig("%s_%s.png" % (title, value))