from rima.models import BaseModel
from mongoengine import Document, StringField
# from rima.models


class UserModel(Document, BaseModel):
    """User Model class."""

    name = StringField()
