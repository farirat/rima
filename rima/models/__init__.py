from mongoengine import connect
# from mondoengine.

import datetime
from uuid import uuid1

from mongoengine import connect, Document
from mongoengine.fields import (
    StringField, IntField, DateTimeField, UUIDField, BooleanField, FloatField,
    DictField
)

# from .settings import MONGO_DBNAME

connect("test_db")


class BaseModel(object):
    """
    Base Model Class.
    """

    uuid = UUIDField(default=uuid1)
    created_at = DateTimeField(default=datetime.datetime.now)
    modified_at = DateTimeField()

    def to_dict(self):
        """
        Converts a document to Dictionary.
        """

        return {
            "uuid": str(self.uuid),
            # "name": self.name,
            
            "created_at": str(self.created_at),
            "modified_at": str(self.modified_at),

        }

    def render_to_response(self):
        """
        Converts a Dictionary to json.
        """

        return {
            str(self.uuid): self.to_dict()
        }

