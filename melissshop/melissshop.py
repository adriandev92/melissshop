import reflex as rx
from melissshop.componentes.componentes import navbar, head, button, footer



class State(rx.State):
    pass



def index() -> rx.Component:
    return navbar(), rx.box(
        rx.center(
            rx.vstack(
                head(),
                button(),
                max_width="600px"
            )
        ),
        rx.center(
            rx.vstack(
                footer(),
                max_width="600px",
                margin_y="32px",
            )
        ),
        margin_y="32px",
        width="100%",
    )

#def launch():
app = rx.App(
    #style=styles.GLOBAL_STYLES
    style= {
        "bg": "purple",
        #"width": "100%"
        "margin_top": "0px"
    }
)
app.add_page(index)