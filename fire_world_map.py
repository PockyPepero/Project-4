import csv
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from datetime import datetime

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get the latitudes, longitudes, and brightness values from the file.
    dates, lats, lons, brights, hover_texts = [],[],[],[],[]
    row_num = 0
    num_rows = 1000
    for row in reader:
        try:
            date = datetime.strptime(row[5], '%Y-%m-%d').date() 
            # the .date() will eliminate the time part from the date.
            # otherwise it will display 00:00:00 for all dates.
            lat = float(row[0])
            lon = float(row[1])
            bright = float(row[2])
        except ValueError:
            print(f"Missing data for {date}.")
        else:
            dates.append(date)
            lats.append(lat)
            lons.append(lon)
            brights.append(bright)
        row_num += 1
        if row_num == num_rows: # breaks the loop after 1,000 rows.
            break

# Map the fires.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': brights,
    'marker': {
        'size': [bright/20 for bright in brights],
        'color': brights,
        'colorscale': 'YlOrRd', # red/yellow color scheme, good for fire data.
        'reversescale': True,
        'colorbar': {'title': 'Brightness'}
    },
}]

my_layout = Layout(title='Global Fires Across the Last 24 hrs')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')

