

from sqlalchemy import create_engine
from pydracula.model.repository.repository import Repository

class SQLiteRepository(Repository):
    def __init__(self, model_cls):
        Repository.__init__(self, model_cls)

    def engine_factory(self):
        return create_engine('sqlite:///notes.db', echo=True)


class MySQLRepository(Repository):
    def __init__(self, model_cls):
        Repository.__init__(self, model_cls)

    def engine_factory(self):
        return create_engine('mysql://scott:tiger@localhost/foo', echo=True)


class PostgresRepository(Repository):
    def __init__(self, model_cls):
        Repository.__init__(self, model_cls)
        
    def engine_factory(self):
        return create_engine('postgresql://scott:tiger@localhost/mydatabase', echo=True)



