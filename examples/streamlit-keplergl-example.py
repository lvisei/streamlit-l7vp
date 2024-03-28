import streamlit as st
from streamlit-l7vp import l7vp_static
from pyl7vp import L7VP

st.write("This is a l7vp map in streamlit")

l7vp_map = L7VP(height=600)
l7vp_static(l7vp_map)