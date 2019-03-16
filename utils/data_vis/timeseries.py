from bokeh.plotting import figure, show, output_file
from bokeh import palettes as bp
from bokeh.models import BasicTicker, ColorBar, ColumnDataSource, LinearColorMapper
from bokeh.models.tools import HoverTool

def plot_timeseries(data, yvalue, color_value, title, ylabel, colors=bp.Reds8):
    """
    "   data:   dataframe
    "   yvalue: y value
    "   color_value:  value that determines color of scatter points
    "   title:  title of histogram
    "   ylabel: y axis label
    "   color:  color of scatter points
    """
    
    source = ColumnDataSource(data = dict (
        date = data["date"].values,
        yvalue = data[yvalue].values,
        color_value = data[color_value].values,
        text = data["text"].values
    ))

    color_mapper = LinearColorMapper(palette=colors, low=0, high=1)

    p = figure(x_axis_type="datetime", sizing_mode='scale_width', plot_height=300, 
               title=title, x_axis_label="date", y_axis_label=ylabel)

    p.circle(x="date", y="yvalue", source=source, color={'field': "color_value", 'transform': color_mapper}, legend='avg')
    
    color_bar = ColorBar(color_mapper=color_mapper, location=(0, 0),
                         ticker=BasicTicker(desired_num_ticks=len(colors)))
    p.add_layout(color_bar, 'right')
    
    p.add_tools(HoverTool(
        tooltips=[
            ( 'date',   '@date{%F}'     ),
            ( yvalue, '@yvalue' ),
            ( color_value, '@color_value'),
            ( 'text', '@text' )
        ],

        formatters={
            'date'      : 'datetime'
        }
    ))
    
    show(p)  # open a browser