import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filepath = "eq_data/world_fires_1_day.csv"
with open(filepath) as f:
    readable = csv.reader(f)
    header = next(readable)
    # for idx, head in enumerate(header):
    #     print(idx, head)

    lats, longs, brights = [] , [], []
    for row in readable:
        lat = float(row[0])
        long = float(row[1])
        bright = float(row[10])
        lats.append(lat)
        longs.append(long)
        brights.append(bright)
    # print(lats, longs)

data = [ {
    'type' : 'scattergeo',
    'lon' : longs,
    'lat' : lats,
    'marker' : {
        # 'size' : [bright for bright in brights]}
    'color' : brights,
    'colorscale' : 'bluered',
    'colorbar' : {'title' : 'Magnitude'}}
}]
my_layout = Layout(title='Global Fires')

fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename='global_fires.html')
