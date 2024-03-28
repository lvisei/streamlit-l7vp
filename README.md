## streamlit-l7vp

[L7VP](https://github.com/antvis/L7VP) is an geospatial intelligent visual analysis and application development tools.

This project was created to allow us to render [L7VP](https://github.com/antvis/L7VP) maps in streamlit.🌍 [Live Demo]() 🌍

[![Latest Stable Version](https://img.shields.io/pypi/v/streamlit-l7vp.svg)](https://pypi.python.org/pypi/streamlit-l7vp)
[![Test Status](https://github.com/lvisei/streamlit-l7vp/workflows/test/badge.svg)](https://github.com/lvisei/streamlit-l7vp/actions?query=workflow:test)

## Installation

```
pip install streamlit-l7vp
```

## Usage

```py
import streamlit as st
from streamlit_l7vp import l7vp_static
import pandas as pd

df = pd.DataFrame(
    {'id': ['a', 'b', 'c'],
     'point_latitude': [31.2384, 31.2311, 31.2334],
     'point_longitude': [108.30948, 108.30231, 108.30238],
     'value': [5, 11, 9],
     'time': ['2019-08-01 12:00:00', '2019-08-01 12:05:00', '2020-08-01 11:55:00']
     })

l7vp_map = L7VP(height = 600)
# Add dataset to map
l7vp_map.add_dataset({"id": "my_dataset", "type": 'local', "data": df})


l7vp_static(l7vp_map)
```

## API

### l7vp_static parameters

- fig: `pyl7vp.L7VP` map figure.
- height: Fixed pixel height of the map. Optional, might result in non-optimal layout on some devices. By
  default the map height is determined by the l7vp figure height.
- width: Fixed pixel width of the map. Optional, by default the map width adjusts to the streamlit layout.
- read_only: Disables the side panel for map customization, default False.

## Local Development

### Clone code

```shell
git clone https://github.com/lvisei/streamlit-l7vp.git
```

### Install python module

```sh
cd bindings/pyl7vp

# dev install from folder containing setup.py
pip install -e .
```

### Release a new version

Update `version` in `setup.py`

```py
version="0.0.1"
```

Build and publish

```bash
python setup.py upload
```

## License

[Apache-2.0](./LICENSE)
