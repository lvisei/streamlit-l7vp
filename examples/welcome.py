import streamlit as st
from pyl7vp import L7VP
from streamlit_l7vp import l7vp_static
import pandas as pd

st.set_page_config(page_title="streamlit-l7vp: AntV L7VP for Streamlit!", page_icon="🌍", layout="wide")

"""
# Welcome to [streamlit-l7vp](https://github.com/lvisei/streamlit-l7vp)!

[L7VP](https://github.com/antvis/L7VP) is an geospatial intelligent visual analysis and application development tools.

This project was created to allow us to render [L7VP](https://github.com/antvis/L7VP) maps in streamlit.
"""


df = pd.DataFrame(
    {'id': ['a', 'b', 'c'],
     'point_latitude': [31.2384, 31.2311, 31.2334],
     'point_longitude': [108.30948, 108.30231, 108.30238],
     'value': [5, 11, 9],
     'time': ['2019-08-01 12:00:00', '2019-08-01 12:05:00', '2020-08-01 11:55:00']
     })

l7vp_map = L7VP(height = 800)
# Add dataset to map
l7vp_map.add_dataset({"id": "my_dataset", "type": 'local', "data": df})
l7vp_map.set_theme("dark")


l7vp_static(l7vp_map)