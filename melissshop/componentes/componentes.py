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

def button() -> rx.Component:
    return rx.center(
        #rx.link(
            rx.vstack(
                rx.link(
                    rx.button(
                        rx.icon(
                            tag="chevrons-right",
                            color="black",
                            margin_x="5px"
                        ),
                        rx.vstack(
                            rx.text("Whatsapp"),
                            rx.text("Comunicate con Melis's Shop"),
                            align="center",
                            spacing="0",
                            color="black",
                            margin="33px"
                        ),
                        bg=rx.color("purple", 11),
                        width="350px",
                        height="50px",
                    ),
                    href="https://wa.me/message/23EIRQUOECRSL1",
                    is_external=True
                ),
                rx.link(
                    rx.button(
                        rx.icon(
                            tag="chevrons-right",
                            color="black",
                            margin_x="5px"
                        ),
                        rx.vstack(
                            rx.text("Grupo de Whatsapp"),
                            rx.text("Unete la comunidad de Melis's Shop"),
                            align="center",
                            spacing="0",
                            color="black",
                            margin="10px"
                        ),
                        bg=rx.color("purple", 11),
                        width="350px",
                        height="50px"
                    ),
                    href="https://chat.whatsapp.com/KIJOt6UrCeGBhWou0eionM",
                    is_external=True
                ),
                rx.link(
                    rx.button(
                        rx.icon(
                            tag="chevrons-right",
                            color="black",
                            margin_x="5px"
                        ),
                        rx.vstack(
                            rx.text("Instagram"),
                            rx.text("Siguenos en nuestro Instagram"),
                            align="center",
                            spacing="0",
                            color="black",
                            margin="28px"
                        ),
                        bg=rx.color("purple", 11),
                        width="350px",
                        height="50px"
                    ),
                    href="https://www.instagram.com/anxuan_oficial/profilecard/?igsh=emNxcWd2OWw2dnNt",
                    is_external=True
                ),
                rx.link(
                    rx.button(
                        rx.icon(
                            tag="chevrons-right",
                            color="black",
                            margin_x="5px",
                        ),
                        rx.vstack(
                            rx.text("Facebook"),
                            rx.text("Siguenos en Facebook"""),
                            align="center",
                            spacing="0",
                            color="black",
                            margin="56px"
                        ),
                        bg=rx.color("purple", 11),
                        width="350px",
                        height="50px"
                    ),
                    href="",
                    is_external=True
                ),
                #align="center"
            ),
        #),
        width="100%",
    )

'''Boton global
def links_button(title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                #rx.center(
                    rx.icon(
                        tag="chevrons-right",
                        color="black",
                        width="32px",
                        height="32px",
                        
                    ),
                    rx.vstack(
                        rx.text(title, size="5", color="black", margin_y="-5px"),
                        rx.text(body, size="2", color="black", margin_y="-5px"),
                        align="center",
                        margin="50px"
                    ),
                    align="center"
                #)
            ),
            width="100%",
            height="55px",
            bg=rx.color("purple", 11)
        ),
        href=url,
        is_external=True,
        width="100%"
    )

Botones que se muestran
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
        #align="center",
        width="100%",
        padding_x="90px"
    )
    '''
    
# Pie de pagina

def footer() -> rx.Component:
    return rx.hstack(
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
        ),
        align="center"
    )