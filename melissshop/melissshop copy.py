import reflex as rx
from melissshop.componentes.componentes import navbar, head, button, footer
import melissshop.styles.styles as styles
from melissshop.styles.styles import Size as Size


class State(rx.State):
    pass



def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                head(),
                button(),
                max_width=styles.MAX_WIDTH,
                align="center",
                width="100%",
                margin_y=Size.BIG.value
            )
        ),
        footer()
    )


app = rx.App(
    style=styles.GLOBAL_STYLES
)
app.add_page(index)