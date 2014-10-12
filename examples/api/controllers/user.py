from rima.controllers import BaseController
from api.models import UserModel


class UserController(BaseController):
	model = UserModel