import reflex as rx
import datetime


# Logo y descripcion

def head() -> rx.Component:
    return rx.vstack(
        rx.avatar(
            name="Melis's Shop",
            size="9",
            src="logo.png",
            radius="full"
        ),
        rx.heading(
            "Melis's Shop",
            size="8",
        ),
        rx.text(
            """Hola, somos Melis's Shop, una agencia de pedidos 
            online donde podras comprar en tiendas como Shein, 
            Temu, Amazon, Ali Express, etc...""",
            align="center",
        ),
        align="center",
    )
    

# Botones

'''Boton global'''
def links_button(title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="chevrons-right",
                    width="32px",
                    height="32px"
                ),
                rx.center(
                    rx.vstack(
                        rx.text(title, size="5", color="black", margin_y="-5px"),
                        rx.text(body, size="2", color="black", margin_y="-5px"),
                        align="center"
                    ),
                    align="center"
                )
            ),
            width="100%",
            height="55px",
            bg=rx.color("purple", 11)
        ),
        href=url,
        is_external=True,
        width="100%"
    )

'''Botones que se muestran'''
def button() -> rx.Component:
    return rx.vstack(
        links_button("Whatsapp",
                     "Escribeme para contactarme",
                     "https://wa.me/message/23EIRQUOECRSL1"
                     ),
        links_button("Grupo de Whatsapp",
                     "Unete la comunidad de Melis's Shop",
                     "https://chat.whatsapp.com/KIJOt6UrCeGBhWou0eionM"
                     ),
        links_button("Instagram",
                     "Siguenos en nuestro Instagram",
                     "https://www.instagram.com/anxuan_oficial/profilecard/?igsh=emNxcWd2OWw2dnNt"
                     ),
        links_button("Facebook",
                     "Siguenos en Facebook",
                     ""
                     ),
        align="center",
        width="100%",
        padding_x="70px"
    )
    
    
# Pie de pagina

def footer() -> rx.Component:
    return rx.center(
        rx.hstack(
            rx.image(
                src="favicon.ico"
            ),
            rx.text(
                f"© 2024-{datetime.date.today().year} MELIS'SSHOP BY"
            ),
            rx.link(
                "ADRIAN CABRALES BALSA",
                href="https://wa.me/message/+5353451622",
                is_external="True"
            )
        )
    )