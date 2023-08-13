import reflex as rx
import requests
from PIL import Image
from typing import Optional


class Friend:

    def __init__(self, id: int, sex: str, name: str, university: Optional[str], faculty: Optional[str],
                 city: Optional[str], school: Optional[str], work: Optional[str], photo_url: str):
        self.id, self.sex, self.name, self.university, self.faculty, self.city, self.school, self.work, self.photo_url = \
            id, sex, name, university, faculty, city, school, work, photo_url

    def getComponent(self) -> rx.Component:
        return rx.hstack(
            rx.image(
                src=self.photo_url,
                width="200px",
                height="auto",
                border_radius="15px",
            ),
            rx.vstack(
                rx.box(
                    self.name,
                    text_align="left"
                ),
                rx.box(
                    height="200px",
                    width="100px"
                ),
                width="500px",
                height="100%",

            ),
            bg="#ededed",
            padding="1em",
            border_radius="0.5em",
            shadow="lg",
        )
        # card: rx.card = rx.card(
        #     rx.text("Body of the Card Component"),
        #     header=rx.heading("Header", size="lg"),
        #     footer=rx.heading("Footer", size="sm")
        # )
        # return card
