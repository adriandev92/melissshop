import reflex as rx
import datetime


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            )
    )


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
                        rx.image(
                            src="wha.png",
                            #color="black",
                            #margin_x="5px",
                            width="35px"
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
                        rx.image(
                            src="wha.png",
                            #color="black",
                            #margin_x="5px",
                            width="35px"
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
                        rx.image(
                            src="inst.png",
                            #color="black",
                            #margin_x="5px",
                            width="30px"
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
                        rx.image(
                            src="face.png",
                            #color="black",
                            #margin_x="5px",
                            width="35px"
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
                    href="https://www.facebook.com/profile.php?id=61556559833909&mibextid=ZbWKwL",
                    is_external=True
                ),
                #align="center"
            ),
        #),
        width="100%",
    )

    
# Pie de pagina

def footer() -> rx.Component:
    return rx.hstack(
        rx.image(
            src="dev.png",
            width="3em"
        ),
        rx.text(
            f"© 2024-{datetime.date.today().year} MELIS'SSHOP BY"
        ),
        rx.link(
            "ADRIAN CABRALES BALSA",
            href="https://wa.me/+5353451622",
            is_external="True"
        ),
        align="center",
        spacing="1"
    )