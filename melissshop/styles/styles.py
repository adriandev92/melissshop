import reflex as rx
from enum import Enum


# Constantes

MAX_WIDTH = "600px"


# Sizes

class Size(Enum):
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    BIG="2em"


# Estilos globales

GLOBAL_STYLES = {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value
    },
    rx.link: {
        "text_decoration": "none"
    }
}

button_font_style = dict(
    font_size=Size.DEFAULT.value,
    color="black"
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    color="black"
)