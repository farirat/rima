class BaseError(Exception):
    pass


class ResourceNotFoundError(BaseError):
    name = "ResourceNotFoundError"
    status = 404

    def __init__(self, message=None):
        self.body = {
            "error_uuid": self.uuid,
            "message": message or "Resource not found"
        }


class BadParametersError(BaseError):
    name = "BadParametersError"
    status = 400

    def __init__(self, message=None):
        self.body = {
            "error_uuid": self.uuid,
            "message": message or "Bad Parameters"
        }


class MissingParameterError(BaseError):
    name = "MissingParameterError"
    status = 400

    def __init__(self, message=None, missing_params=None):
        self.body = {
            "error_uuid": self.uuid,
            "message": message or "Missing Parameters Error",
            "missing_params": missing_params
        }


class MissingRequiredHeader(BaseError):
    name = "MissingRequiredHeader"
    status = 400
    body = {"message": "Missing Required Header"}

    def __init__(self, message=None):
        self.body = {
            "error_uuid": self.uuid,
            "message": message or "Missing Required Header"
        }


class ForbiddenError(BaseError):
    name = "ForbiddenError"
    status = 403

    def __init__(self, message=None):
        self.body = {
            "error_uuid": self.uuid,
            "message": message or "Forbidden error"
        }


class ConflictError(BaseError):
    name = "ConflictError"
    status = 409
    body = {"message": "Resource Conflict"}


class UnauthorizedError(BaseError):
    name = "UnauthorizedError"
    status = 401

    def __init__(self, message=None):
        self.body = {
            "error_uuid": self.uuid,
            "message": message or "Unauthorized Error"
        }


class RemoteAPIError(BaseError):
    name = "RemoteAPIError"
    status = 502

    def __init__(self, message=None, remote_error=None, remote_message=None, sent_params={}):
        self.body = {
            "error_uuid": self.uuid,
            "message": message or "Remote API Error",
            "remote_error": remote_error,
            "remote_message": remote_message,
            "sent_params": sent_params
        }


class UnknownError(BaseError):
    name = "UnknownError"
    status = 500
    
    def __init__(self, message=None):
        
        self.body = {
            "error_uuid": self.uuid,
            "message": message or "UnknownError",
        }
