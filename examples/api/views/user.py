from rima.views import BaseView
from controllers.user import UserController

from importlib import import_module
class UserView(BaseView):
    controller = UserController

    # def get(self):
    #     self.write({"message": "ok too"})

        # if isinstance(urlconf_module, six.string_types):
  #       urlconf_module = import_module(urlconf_module)
  #   patterns = getattr(urlconf_module, 'urlpatterns', urlconf_module)