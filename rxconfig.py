import reflex as rx


class BangwithfriendsConfig(rx.Config):
    pass


config = BangwithfriendsConfig(
    app_name="BangWithFriends",
    api_url="https://skemta.ru",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)
