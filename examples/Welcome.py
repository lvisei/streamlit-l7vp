import streamlit as st
from pyl7vp import L7VP
from streamlit_l7vp import l7vp_static
import pandas as pd
import numpy as np

st.set_page_config(page_title="streamlit-l7vp: AntV L7VP for Streamlit!", page_icon="🌍", layout="wide")

"""
# Welcome to [streamlit-l7vp](https://github.com/lvisei/streamlit-l7vp)!

[L7VP](https://github.com/antvis/L7VP) is an geospatial intelligent visual analysis and application development tools. This project was created to allow us to render [L7VP](https://github.com/antvis/L7VP) maps in streamlit. API document see [streamlit-l7vp-api](https://github.com/lvisei/streamlit-l7vp#api).
"""

df = pd.DataFrame(
    np.random.randn(1000, 3) + [31.76, 108.4, 20],
    columns=['lat', 'lon', 'value',])

l7vp_map = L7VP(height = 600)
# Add dataset to map
l7vp_map.add_dataset({"id": "my_dataset", "type": 'local', "data": df})
l7vp_map.set_theme("dark")


l7vp_static(l7vp_map)

st.markdown("""
```py
from pyl7vp import L7VP
from streamlit_l7vp import l7vp_static
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1000, 3) + [31.76, 108.4, 20],
    columns=['lat', 'lon', 'value',])

l7vp_map = L7VP(height = 600)
# Add dataset to map
l7vp_map.add_dataset({"id": "my_dataset", "type": 'local', "data": df})
l7vp_map.set_theme("dark")

l7vp_static(l7vp_map)
```
""")