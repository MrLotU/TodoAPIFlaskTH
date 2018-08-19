from peewee import Model, Proxy, SqliteDatabase

REGISTERED_MODELS = []

database = Proxy()

class BaseModel(Model):
    """Base Model class with preset DB"""
    class Meta:
        database = database

    @staticmethod
    def register(cls):
        """Registers new model"""
        REGISTERED_MODELS.append(cls)
        return cls
    
def init_db():
    """Initializes the DB"""
    database.initialize(SqliteDatabase('todos.sqlite'))
    for model in REGISTERED_MODELS:
        model.create_table(True)
        if hasattr(model, 'SQL'):
            database.execute_sql(model.SQL)
