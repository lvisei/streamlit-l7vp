import streamlit as st
from pyl7vp import L7VP
from streamlit_l7vp import l7vp_static
import pandas as pd

st.set_page_config(page_title="User Guide", page_icon="🌍", layout="wide")

"""
## User Guide
### Prepare data
            
```py
import pandas as pd

df = pd.DataFrame(
  {'longitude': [105.005, 104.602, 103.665, 105.275],
   'latitude': [32.349, 32.067, 31.29, 32.416],
   'mag': [5.2, 3.0, 6.0, 2.0]
  })
``` 
            
### Add dataset
            
```py
from pyl7vp import L7VP

l7vp_map = L7VP(height = 600)

# Add dataset to map
l7vp_map.add_dataset({"id": "my_dataset", "type": 'local', "data": df})
```
            
### Display map
            
```py 
from streamlit_l7vp import l7vp_static
            
# Set config
l7vp_map.set_config({
  "map": {
    "type": "Gaode",
    "config": {
            "zoom": 7,
            "center": [104.615357, 32.068745],
            "style": 'dark',
        },
  },
})

# Display map
l7vp_static(l7vp_map)
```

### Customize Map

![](https://mdn.alipayobjects.com/huamei_qa8qxu/afts/img/A*pAh4TZBM4-0AAAAAAAAAAAAADmJ7AQ/original)


Add layers, filters and popup, More in [Config Map Widget](https://www.yuque.com/antv/l7vp/pyl7vp-user-guide#LQzPy).
"""



