# **Useful tools for handling data, using many known data science packages.**

## Basic Usage
Install the package
`pip install convenient-datascience-tools`

Import the package
```
    from convenient_datascience_tools.tools import <TOOL> as <ABBREVIATED_TOOL>_tools
```
For example:
```
    from convenient_datascience_tools.tools import pandas as pd_tools
```
Where 'pandas' is the TOOL nd 'pd' the abbreviated tool.

For more usage cases, please go to `examples` folder.

We have not yet implemented test cases, though it is going to be implemented in a near future.

## Deploy
To deploy a new version, you need:

Versioning is not automated, so you will always need to change it in setup.py.
It will be a future improvement to make it automatic.

In order to install build (dev) dependencies
```
pip install --upgrade build twine
```

In order to build. This will create a `/dist` folder.
```
python -m build
```

In order to upload to PyPa (to be able to fetch via pip)
```
python -m twine upload dist/*
```

