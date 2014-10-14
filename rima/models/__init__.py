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
    """

    uuid = UUIDField(default=uuid1)

   
    created_on = DateTimeField(default=datetime.datetime.now)
    modified_on = DateTimeField()
    delete_on = DateTimeField()

    def to_dict(self):
        """
        Converts a document to Dictionary.
        """

        return {
            "uuid": str(self.uuid),
            "name": self.name,
            
            "created_at": str(self.created_on),
            "modified_at": str(self.modified_on),

        }

    def render_to_response(self):
        """
        Converts a Dictionary to json.
        """

        return {
            str(self.uuid): self.to_dict()
        }

