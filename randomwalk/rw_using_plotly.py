import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    df = pd.DataFrame(dict(
        x = rw.x_values,
        y = rw.y_values
    ))
    fig = px.line(df, x="x", y="y", title="A Random Walk")

    fig.add_trace(go.Scatter(
    x=[0],
    y=[0],
    marker=dict(color="green", size=12),
    mode="markers",
    name="start point",
))

    fig.add_trace(go.Scatter(
    x=[rw.x_values[-1]],
    y=[rw.y_values[-1]],
    marker=dict(color="crimson", size=12),
    mode="markers",
    name="end point",
))

    fig.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break


