from bokeh.plotting import figure, show, output_file

def plot_scatter(data, xvalue, yvalue, title, xlabel, ylabel, color="#FF0000"):
    """
    "   data:   dataframe
    "   xvalue: x value
    "   yvalue: y value
    "   title:  title of histogram
    "   xlabel: x axis label
    "   ylabel: y axis label
    "   color:  color of scatter points
    """

    x = data[xvalue].values
    y = data[yvalue].values
    
    colors = [color] * len(data)

    p = figure(title=title, x_axis_label=xlabel, y_axis_label=ylabel)

    p.scatter(x, y, fill_color=colors, fill_alpha=0.3, line_color=None)

    show(p)  # open a browser
    
def plot_scatter_variable_color(data, xvalue, yvalue, color_value, title, xlabel, ylabel):
    """
    "   data:   dataframe
    "   xvalue: x value
    "   yvalue: y value
    "   color_value:  value that determines color of scatter points
    "   title:  title of histogram
    "   xlabel: x axis label
    "   ylabel: y axis label
    """
    
    x = data[xvalue].values
    y = data[yvalue].values

    colors = ["#%s0000" % str(hex(abs(int(value*0xFF))))[2:] for value in data[color_value].values]

    p = figure(title=title, x_axis_label='Number of Favorites', y_axis_label='Number of Retweets')

    p.scatter(x, y, fill_color=colors, fill_alpha=0.3,
              line_color=None)
    
    show(p)  # open a browser