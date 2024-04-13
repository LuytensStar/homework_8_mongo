from datetime import datetime

from mongoengine import  Document
from mongoengine.fields import ReferenceField, StringField,ListField

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description =  StringField()


class Quote(Document):
    author = ReferenceField(Author)
    quote = StringField(required=True)
    tags = ListField(StringField())

