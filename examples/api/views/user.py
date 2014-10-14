from rima.views import BaseView
from controllers.user import UserController


class UserView(BaseView):
	controller = UserController