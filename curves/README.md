# Curves

## Notes on Project Set Up

this project is managed by poetry; `poetry new --src curves`

package dependency:

```toml
[tool.poetry.dependencies]
python = "^3.8"
jupyter = "*"
notebook = "*"
```

this assumes virtualenv/poetry has enabled local-env directory `.venv`;

run `poetry install` then `poetry build`; add `.gitignore` file:

```text
.venv
dist
curves.egg-info
```

to run jupyter notebook: `poetry run jupyter notebook`
