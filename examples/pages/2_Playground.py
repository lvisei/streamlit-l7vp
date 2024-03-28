import streamlit as st
from pyl7vp import L7VP
from streamlit_l7vp import l7vp_static

st.set_page_config(page_title="playground", page_icon="🌍", layout="wide", initial_sidebar_state="collapsed", menu_items={
  'Get Help': 'https://github.com/antvis/L7VP/tree/master/bindings/pyl7vp#user-guide'
})

"""
## Playground
"""

l7vp_map = L7VP(height = 800)
l7vp_map.set_theme("dark")

l7vp_static(l7vp_map)
