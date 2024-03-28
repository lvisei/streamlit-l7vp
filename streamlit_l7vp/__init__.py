from typing import Optional

import streamlit.components.v1 as components
from pyl7vp import L7VP


def l7vp_static(
    fig: L7VP,
    height: Optional[int] = None,
    width: Optional[int] = None,
    read_only: Optional[bool] = False,
) -> components.html:
    """
    Renders a `pyl7vp.L7VP` map figure in a Streamlit app.

    This is a static Streamlit component, thus information from browser interaction can not be passed back from
    L7VP to Python.

    Args:
        fig: `pyl7vp.L7VP` map figure.
        height: Fixed pixel height of the map. Optional, might result in non-optimal layout on some devices. By
            default the map height is determined by the l7vp figure height.
        width: Fixed pixel width of the map. Optional, by default the map width adjusts to the streamlit layout.
        read_only: Disables the side panel for map customization, default False.

    Example:
        ```python
            >>> l7vp_map = L7VP()
            >>> l7vp_static(l7vp_map)
        ```
    """
    try:
        html = fig._get_html_str(read_only=read_only)
    except AttributeError:
        raise TypeError(
            "fig argument has to be a l7vp map object of type pyl7vp.L7VP!"
        )

    if height is None:
        height = fig.height
    return components.html(html, height=height + 10, width=width)