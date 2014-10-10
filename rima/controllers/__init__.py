import datetime

from rima.utils.validators import validate
from rima.exceptions import (
    MissingParameterError, ConflictError, ResourceNotFoundError,
    BadParametersError
)


class BaseController(object):

    required_create_fields = []
    search_fields = []
    model = None

    @classmethod
    def check_missing_parameters(cls, params_list, **kwargs):
        """
        """

        if kwargs:
            data = {}
            missing_params = []
            for param in params_list:
                if param in kwargs:
                    data.update({param: kwargs.get(param)})
                else:
                    missing_params.append(param)
                    
            if missing_params:
                raise MissingParameterError(
                    "Missing parameters",
                    missing_params=missing_params
                )
            else:
                return data
        else:
            raise MissingParameterError("No params were passed")

    @classmethod
    def validate_parameters(cls, **kwargs):
        """
        """

        [
            validate(key, value)
            for key, value in kwargs.iteritems()
        ]

    @classmethod
    def check_existence(cls, **kwargs):
        """
        """

        if cls.model.objects.filter(**kwargs):
            raise ConflictError()

    @classmethod
    def pre_create(cls, **kwargs):
        """
        """

        return kwargs

    @classmethod
    def post_create(cls, **kwargs):
        """
        """

        pass
 
    @classmethod
    def create(cls, **kwargs):
        """
        """

        params = cls.check_missing_parameters(
            cls.required_create_fields,
            **kwargs
        )
        cls.validate_parameters(**params)
        cls.check_existence(**params)
        params = cls.pre_create(**params)
        obj = cls.model(**params)
        params["uuid"] = str(obj.uuid)
        obj.save()
        cls.post_create(**params)
        return obj

    @classmethod
    def list(cls, uuid=None):
        """
        """

        if uuid is None:
            objs = cls.model.objects.order_by("-created_on")
        else:
            objs = cls.model.objects.filter(uuid=uuid)

        if len(objs) > 0:
            return objs
        else:
            raise ResourceNotFoundError()

    @classmethod
    def search(cls, **kwargs):
        """
        """
        # will add check params later
        # data = cls.check_parameters(**kwargs)
        obj = cls.model.objects(**kwargs)
        if obj:
            return obj
        else:
            raise ResourceNotFoundError("Object not found")

    @classmethod
    def pre_update(cls, uuid, **kwargs):
        """
        """
        print("in base pre update")
        print(kwargs)

        return kwargs

    @classmethod
    def post_update(cls, **kwargs):
        """
        """

        return kwargs

    @classmethod
    def update(cls, uuid, **kwargs):
        """
        """

        objs = cls.model.objects.filter(uuid=uuid)
        if len(objs) == 1:
            obj = objs[0]
            kwargs = cls.pre_update(uuid, **kwargs)
            for key, value in kwargs.iteritems():
                obj.__setattr__(key, value)
            obj.modified_on = datetime.datetime.now()
            kwargs["uuid"] = str(obj.uuid)
            obj = obj.save()
            cls.post_update(**kwargs)
            return obj
        else:
            raise BadParametersError("Bad uuid")

    @classmethod
    def pre_delete(cls, uuid):
        """
        """
        
        pass

    @classmethod
    def post_delete(cls, uuid):
        """
        """
        
        pass

    @classmethod
    def delete(cls, uuid):
        """
        """

        objs = cls.model.objects.filter(uuid=uuid)
        if len(objs) == 1:
            obj = objs[0]
            cls.pre_delete(uuid)
            obj.delete()
            cls.post_delete(uuid)
            return obj
        else:
            raise ResourceNotFoundError("uuid not found")
