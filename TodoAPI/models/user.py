from TodoAPI.sql import BaseModel
from peewee import CharField

from argon2 import PasswordHasher
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired

HASHER = PasswordHasher()

@BaseModel.register
class User(BaseModel):
    username = CharField()
    password = CharField()

    @property
    def auth_token(self):
        return self.generate_auth_token()

    @classmethod
    def create_user(cls, username, password, **kwargs):
        try:
            cls.select().where(
                (cls.username**username)
            ).get()
        except cls.DoesNotExist:
            user = cls(username=username)
            user.password = user.hash_password(password)
            user.save()
            return user
        else:
            raise Exception('User with those credentials already exists')

    @staticmethod
    def verify_auth_token(token):
        serializer = Serializer('')
        try:
            data = serializer.loads(token)
        except (SignatureExpired, BadSignature):
            return None
        else:
            user = User.get(User.id==data['id'])
            return user

    @staticmethod
    def hash_password(password):
        return HASHER.hash(password)

    def verify_password(self, password):
        return HASHER.verify(self.password, password)

    def generate_auth_token(self):
        serializer = Serializer('')
        return serializer.dumps({'id': self.id})