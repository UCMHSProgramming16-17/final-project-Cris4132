# import modules
import numpy as np
import pandas as pd
# import graphs from bokeh
from bokeh.plotting import figure, output_file, save
from bokeh.charts import Line, output_file, save
# import csv
import csv
# create dataframe with csv file
df = pd.read_csv('New_York_City_Leading_Causes_of_Death.csv')
# set x and y planes for first graph
x = df["Deaths"]
y = df["Age Adjusted Death Rate"]
# create output file as html
output_file("deathsvsageadjusteddeathrate.html")
# set graph parameters and specifications
graph = figure(width = 2500, height = 300)
graph.circle(x, y, line_color = "red", fill_color = "blue")
# save graph
save(graph)

# set x and y planes for first graph
x1 = df["Deaths"]
y1 = df["Death Rate"]
# create output file as html
output_file("deathsvsdeathrate.html")
# set graph parameters and specifications
graph2 = figure(width = 2500, height = 200)
graph2.circle(x1, y1, line_color = "yellow", fill_color = "green")
# save graph
save(graph2)