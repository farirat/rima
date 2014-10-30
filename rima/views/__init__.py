from json import loads

from tornado.web import RequestHandler

from rima.decorators import error_handler


class BaseView(RequestHandler):
    """Request handler where requests and responses speak JSON."""

    controller = None
    resource_name = None

    def write_error(self, status_code, **kwargs):
        """
        Overrides HTTPError response to return Json instead of HTML
        """
        self.finish(
            {
                "status_code": status_code,
                "message": self._reason,
            }
        )

    @error_handler
    def get(self, uuid=None):
        """
        Lists all resources view or filter by UUID.
        """
        
        objs = self.controller.list(uuid=uuid)

        objs = {
            str(obj.uuid): obj.to_dict()
            for obj in objs
        }
        self.set_header('Object-Count', len(objs))
        return objs

    @error_handler
    def post(self):
        """
        Creates new resource view.
        """

        data = loads(self.request.body.decode("utf-8"))
        obj = self.controller.create(**data)

        return obj.render_to_response()

    @error_handler
    def patch(self, uuid):
        """
        Updates resource view
        """
        data = loads(self.request.body.decode("utf-8"))

        obj = self.controller.update(uuid, **data)

        return obj.render_to_response()

    @error_handler
    def delete(self, uuid):
        """
        Delete resource view.
        """

        obj = self.controller.delete(uuid=uuid)
        return obj.render_to_response()


# class BaseSearchView(RequestHandler):
#     """Request handler where requests and responses speak JSON."""

#     controller = None

#     def write_error(self, status_code, **kwargs):
#         """
#         Overrides HTTPError response to return Json instead of HTML
#         """
#         self.finish(
#             {
#                 "status_code": status_code,
#                 "message": self._reason,
#              }
#         )
    
#     @error_handler
#     def post(self):
#         """
#         """
        
#         data = loads(self.request.body.decode("utf-8"))
        
#         objs = self.controller.search(**data)
#         self.set_header('Object-Count', len(objs))

#         if len(objs) > 1:
#             _objs = {
#                 str(obj.uuid): obj.to_dict()
#                 for obj in objs
#             }

#             return _objs
#         else:
#             return objs[0].render_to_response()
