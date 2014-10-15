from views.user import UserView


urls_map = [
    # ("/user", UserView),
    ("/user", "views.user.UserView"),
]