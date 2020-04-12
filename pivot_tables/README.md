# Pivot Table

source: <https://datatofish.com/pivot-table-python/>

see also: <https://www.analyticsvidhya.com/blog/2020/03/pivot-table-pandas-python/>

## Matplot display backend issue

Running the salesmen example, I didn't see the pop-up display window
and got this warning:

```text
UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
```

this is due to Matplot by default uses a headless backend `Agg` hence
once supports save-to-file.

I found that `Qt5Agg` is on the supported display backend list so I
decided to poetry-add PyQt5 to the dependency list.

however **I found that I must use a hardcoded version, PyQt5 == 5.14.0**
as the latest version caused virtualenv to stall.

I had to kill the installation process, nuke `.venv` dir and the lock
file, then re-run `poetry install` (with the hardcoded PyQt5 version).

Also in the source code I needed to add `matplotlib.use('Qt5Agg')`.

Despite this gotcha, it inspired me to use more PyQt5 at work (on
Mac OS) as I can localize the virtualenv and ship it as a single
package to give the end user the necessary runtime environment.

To prove that:

```shell
find . -name "*.so"
./.venv/lib/python3.8/site-packages/pandas/io/sas/_sas.cpython-38-x86_64-linux-gnu.so
./.venv/lib/python3.8/site-packages/pandas/_libs/window/aggregations.cpython-38-x86_64-linux-gnu.so
./.venv/lib/python3.8/site-packages/pandas/_libs/window/indexers.cpython-38-x86_64-linux-gnu.so
./.venv/lib/python3.8/site-packages/pandas/_libs/tslibs/parsing.cpython-38-x86_64-linux-gnu.so
./.venv/lib/python3.8/site-packages/pandas/_libs/tslibs/timedeltas.cpython-38-x86_64-linux-gnu.so

....
./.venv/lib/python3.8/site-packages/PyQt5/QtQml.abi3.so
./.venv/lib/python3.8/site-packages/PyQt5/QtNfc.abi3.so
..
```

all the platform-specific dynamic libraries are also installed to
the local `.venv` directory
