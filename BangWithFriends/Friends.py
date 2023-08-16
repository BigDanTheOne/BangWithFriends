import dataclasses
from typing import Optional

import reflex as rx


@dataclasses.dataclass
class Friend:
    id: int
    sex: str
    name: str
    university: Optional[str]
    faculty: Optional[str]
    city: Optional[str]
    school: Optional[str]
    work: Optional[str]
    photo_url: str

    def get_component(self) -> rx.Component:
        return rx.hstack(
            rx.image(
                src=self.photo_url,
                width="200px",
                height="auto",
                border_radius="15px",
            ),
            rx.vstack(
                rx.box(self.name, text_align="left"),
                rx.box(height="200px", width="100px"),
                width="500px",
                height="100%",
            ),
            bg="#ededed",
            padding="1em",
            border_radius="0.5em",
            shadow="lg",
        )
