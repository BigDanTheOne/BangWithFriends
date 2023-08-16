"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from typing import List

import reflex as rx
import requests
import vkbottle

from rxconfig import config

from .Friends import Friend

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


friends_mock: List[Friend] = [
    Friend(
        *[
            1,
            "m",
            "Даниил Акопян",
            None,
            None,
            None,
            None,
            None,
            "https://sun9-71.userapi.com/impg/CIHN6a0gLTe7QjtYH4U9F0aoexCXCXPgxEYFSg/ecis0a86N50.jpg?size=768x1024&quality=95&sign=fb56c34e6d3ab38bfe00c490b717f35c&type=album",
        ]
    ),
    Friend(
        *[
            2,
            "m",
            "Денис Мазур",
            None,
            None,
            None,
            None,
            None,
            "https://sun9-57.userapi.com/impg/B3us9LpdBYlH2jDH5t0OHnQchg5v4XES6TPxTA/QUpiHgGnyOg.jpg?size=961x1280&quality=95&sign=0ef4a7c045743a9cd3ad7f5f0ef3f249&type=album",
        ]
    ),
]


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            # rx.vstack(
            #     friend.get_component() for friend in friends_mock
            # ),
            friends_mock[0].get_component(),
            rx.link(
                "Log in with vk",
                href="https://oauth.vk.com/authorize?client_id=51724129&redirect_uri=https://skemta.ru/vk-auth/&scope=2",
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
    )


async def get_vk_friends(request):
    print(1)
    try:
        code = request.rel_url.query.get("code")
        print(1)
        data = requests.get(
            "https://oauth.vk.com/access_token?client_id=51724129&client_secret=M7lZNCwJ0IEWWNMhCBu0&redirect_uri=https://skemta.ru/vk-auth/"
            + code
        ).json()
        vk_token = data["access_token"]
        API = vkbottle.API(vk_token)
        vk_id = data["user_id"]
        friends = {}
        for friend in (
            await API.friends.get(user_id=vk_id, order="name", fields=["nickname", "photo_400_orig"])
        ).items:
            if friend.deactivated:
                continue
            friends[friend.id] = {
                "name": friend.first_name + " " + friend.last_name,
                "is_closed": friend.is_closed,
                "photo": friend.photo_400_orig,
            }
        pass
    except:
        pass
    raise rx.redirect("/sucess")


app = rx.App()
app.api.add_api_route("/vk-auth/", get_vk_friends)
app.add_page(index)
app.compile()
