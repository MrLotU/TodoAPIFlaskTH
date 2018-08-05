import datetime

from argon2 import PasswordHasher
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer,
                          BadSignature, SignatureExpired)
from peewee import CharField, BooleanField, IntegerField
from TodoAPI.sql import BaseModel

@BaseModel.register
class Todo(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    edited = BooleanField(default=False)
    completed = BooleanField(default=False)