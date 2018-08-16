from peewee import Model, Proxy, SqliteDatabase
import psycogreen.gevent; psycogreen.gevent.patch_psycopg()

REGISTERED_MODELS = []

database = Proxy()

class BaseModel(Model):
    class Meta:
        database = database

    @staticmethod
    def register(cls):
        REGISTERED_MODELS.append(cls)
        return cls
    
def init_db():
    database.initialize(SqliteDatabase('todos.sqlite'))
    for model in REGISTERED_MODELS:
        model.create_table(True)
        if hasattr(model, 'SQL'):
            database.execute_sql(model.SQL)
