import os
import json
import plotly
import plotly.express as px
import pandas as pd
import numpy as np
from plotly.graph_objs import Scatter, Layout
import re

# useful articles:
# https://towardsdatascience.com/how-to-plot-time-series-86b5358197d6


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


class ProgressCollector:
    def __init__(self):
        self.projs = dict()
        self.loc = 0

    def collect(self, d):
        for k, v in d.items():
            _ver, name, _hostname, time_stamp = k.split('/')
            if name not in self.projs:
                self.projs[name] = ProjectStatCollector(name)
            self.projs[name].collect(v, time_stamp)

    def to_panda(self, wanted=None, subs_only=False):
        for name in self.projs:
            self.loc += self.projs[name].loc[-1]
        ds = []
        wanted = wanted or [(r'.*', r'.*')]
        for key in sorted(self.projs.keys()):
            for proj_filter, sub_filter in wanted:
                if re.match(proj_filter, key):
                    ds.extend(self.projs[key].to_panda(sub_filter, subs_only=subs_only))
        return ds


class ProjectStatCollector:
    def __init__(self, name):
        self.name = name
        self.subcs = dict()
        self.loc = list()
        self.ts = list()

    def collect(self, d, time_stamp):
        loc = d.get('aggregate', dict()).get('total')
        if not loc:
            return
        self.loc.append(loc)
        self.ts.append(time_stamp)
        for proj in d.get('projects', []):
            proj_name = proj[0]
            proj_data = proj[2]
            if proj_name not in self.subcs:
                self.subcs[proj_name] = SubProjectStatCollector(proj_name)
            self.subcs[proj_name].collect(proj_data, time_stamp)

    def to_panda(self, wanted=None, subs_only=False):
        ds = []
        if not subs_only:
            ds.append(Scatter(x=self.ts, y=self.loc, name=self.name, showlegend=True))
        wanted = wanted or r'.*'
        for k in sorted(self.subcs.keys()):
            if re.match(wanted, k):
                subc = self.subcs[k]
                ds.append(subc.to_panda())
        return ds

class SubProjectStatCollector:
    def __init__(self, name):
        self.name = name
        self.loc = list()
        self.ts = list()

    def collect(self, d, time_stamp):
        loc = d.get('total')
        if not loc:
            return
        self.loc.append(loc)
        self.ts.append(time_stamp)

    def to_panda(self):
        return Scatter(x=self.ts, y=self.loc, name=self.name, showlegend=True)


def test_show_project_progress():
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
        "layout":
        Layout(title="repo stats")
    })



if __name__ == '__main__':
    diter = read_all_lines('/tmp/repo/repoStats')
    coll = ProgressCollector()
    for d in diter:
        coll.collect(d)
    ds = coll.to_panda(wanted=[(r'cxx|py|rust|haskell|scala|go', r'----')])
    plotly.offline.plot({"data": ds, "layout": Layout(title="repo stats, loc: {}".format(coll.loc))})
