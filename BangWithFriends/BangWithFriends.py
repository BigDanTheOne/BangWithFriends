"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
import requests
import vkbottle
import reflex as rx
import json


docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
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

async def getVKFreinds(request):
    print(1)
    try:
        code = request.rel_url.query.get('code')
        print(1)
        data = requests.get("https://oauth.vk.com/access_token?client_id=51724129&client_secret=M7lZNCwJ0IEWWNMhCBu0&redirect_uri=https://skemta.ru/vk-auth/" + code).json()
        vk_token = data['access_token']
        API = vkbottle.API(vk_token)
        vk_id = data['user_id']
        friends = {}
        for friend in (await API.friends.get(user_id=vk_id, order="name", fields=["nickname", "photo_400_orig"])).items:
            if friend.deactivated:
                continue
            friends[friend.id] = {
                "name": friend.first_name + " " + friend.last_name,
                "is_closed": friend.is_closed,
                "photo": friend.photo_400_orig
            }
        pass
    except:
       pass
    raise rx.redirect("/sucess")


app = rx.App()
app.api.add_api_route("/vk-auth/", getVKFreinds)
app.add_page(index)
app.compile()
