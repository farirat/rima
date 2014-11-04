from rima.controllers import BaseController
from models.user import UserModel


class UserController(BaseController):
    """
    User Controller Class.
    """
    
    model = UserModel