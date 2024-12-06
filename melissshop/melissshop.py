import reflex as rx
from melissshop.componentes.componentes import head, button, footer


class State(rx.State):
    pass



def index() -> rx.Component:
    return rx.box(
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
                margin_y="32px"
            )   
        ),
        margin_y="32px",
        width="100%"
    )


app = rx.App()
app.add_page(index)