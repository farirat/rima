from functools import wraps
# from pprint import pprint

from tornado.web import HTTPError

from rima.exceptions import (
    ResourceNotFoundError, ConflictError, MissingParameterError,
    UnknownError
)#, FormatError, UnknownError


# def debug(function):

#     @wraps(function)
#     def debug_wrapper(*args, **kwargs):
#         print("IN DEBUG WRAPPER")
#         output = {
#             "function": function.__name__,
#             "args": args,
#             "kwargs": kwargs,
#             }
        
#         result = function(*args, **kwargs)
        
#         output.update({"result": result})
        
#         print("-"*100)
#         pprint(output, indent=4, depth=4)
#         print("-"*100)

#         return result

#     return debug_wrapper

# @debug
def error_handler(method):
    @wraps(method)
    def error_handler_wrapper(self, *args, **kwargs):
        print((self, args, kwargs))
        try:
            result = method(self, *args, **kwargs)
            print("result")
            print(result)
            self.write(result)

        except MissingParameterError as error:
            raise HTTPError(400)
        except KeyError as error:
            raise HTTPError(400)
        except ResourceNotFoundError as error:
            raise HTTPError(404)
        except ConflictError as error:
            raise HTTPError(409)
        except UnknownError as error:
            raise HTTPError(500)
        except Exception as error:
            raise HTTPError(500)

    return error_handler_wrapper
