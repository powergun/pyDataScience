import os
import json
import plotly
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.graph_objs import Scatter, Bar, Layout
import re


data_frame = Scatter(x=[1, 3], y=[10, 20], name='timer1', showlegend=True)


def three_dimension():
    data = {
        "original": [15, 23, 32, 10, 23],
        "model_1": [4, 8, 18, 6, 0],
        "model_2": [11, 18, 18, 0, 20],
        "labels":
        ["feature", "question", "bug", "documentation", "maintenance"]
    }
    fig = go.Figure(
        data=[
            go.Bar(
                name="Original",
                x=data["labels"],
                y=data["original"],
                offsetgroup=0,
            ),
            go.Bar(
                name="Model 1",
                x=data["labels"],
                y=data["model_1"],
                offsetgroup=1,
            ),
            go.Bar(
                name="Model 2",
                x=data["labels"],
                y=data["model_2"],
                offsetgroup=1,
                base=data["model_1"],
            )
        ],
        layout=go.Layout(
            title="Issue Types - Original and Models",
            yaxis_title="Number of Issues"
        )
    )
    return fig


def showBar(d):
    animals = [
        'measure 1/there is a silence', 'measure 2 e1m1=iddqd+idkfa',
        'really long really long really'
    ]
    bar = Bar(x=animals, y=[20.1, 14.2, 23.3])
    scatter = Scatter(x=animals, y=[20.1, 14.2, 23.3])
    fig = go.Figure(data=[bar, scatter])

    fig.add_trace(go.Bar(x=animals, y = [13, 15, 19]))
    fig.add_trace(go.Bar(x=animals, y = [16, 20, 26]))

    subf = three_dimension()
    subf.show()
    # fig.show()


if __name__ == '__main__':
    showBar([data_frame])
