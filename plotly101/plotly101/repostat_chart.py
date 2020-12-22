import os
import json
import plotly
import plotly.express as px
import pandas as pd
import numpy as np
from plotly.graph_objs import Scatter, Layout

def read_all_lines(dirp, ext=".txt"):
    for filename in os.listdir(dirp):
        if not filename.endswith(ext):
            continue
        path = os.path.join(dirp, filename)
        with open(path, 'r') as fp:
            for l in fp:
                yield json.loads(l)


def process(d):
    for k, v in d.items():
        # 1/scala/weining-ubuntu/2020-11-05 18:04:52
        _ver, category, hostname, time_stamp = k.split('/')
        loc = v.get('aggregate', dict()).get('total', 0)
        yield category, time_stamp, loc

if __name__ == '__main__':
    it = read_all_lines('/tmp/repo/repoStats')
    
    cxx_ts = []
    cxx_loc = []

    hs_ts = []
    hs_loc = []

    scala_ts = []
    scala_loc = []

    go_ts = []
    go_loc = []

    py_ts = []
    py_loc = []

    rs_ts = []
    rs_loc = []

    for d in it:
        for category, time_stamp, loc in process(d):
            t = pd.Timestamp(time_stamp)
            if category == 'cxx':
                cxx_ts.append(t)
                cxx_loc.append(loc)
            elif category == 'haskell':
                hs_ts.append(t)
                hs_loc.append(loc)
            elif category == 'scala':
                scala_ts.append(t)
                scala_loc.append(loc)
            elif category == 'go':
                go_ts.append(t)
                go_loc.append(loc)
            elif category == 'python':
                py_ts.append(t)
                py_loc.append(loc)
            elif category == 'rust':
                rs_ts.append(t)
                rs_loc.append(loc)


    plotly.offline.plot({
        "data": [
            Scatter(x=cxx_ts, y=cxx_loc, name='c++', showlegend=True),
            Scatter(x=hs_ts, y=hs_loc, name='haskell', showlegend=True),
            Scatter(x=scala_ts, y=scala_loc, name='scala', showlegend=True),
            Scatter(x=go_ts, y=go_loc, name='go', showlegend=True),
            Scatter(x=rs_ts, y=rs_loc, name='rust', showlegend=True),
            Scatter(x=py_ts, y=py_loc, name='python', showlegend=True)

        ],
        "layout": Layout(title="repo stats")
    })