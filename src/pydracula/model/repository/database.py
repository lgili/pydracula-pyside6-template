

from sqlalchemy import create_engine
from pydracula.model.repository.repository import Repository
from pathlib import Path
import sys, os

def get_database_path():
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the PyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app 
        # path into variable _MEIPASS'.
        print('is in frozen')
        application_path = sys._MEIPASS
        database_path = application_path + '/build_system/resources/database.db'
    else:    
        application_path = os.path.dirname(Path(os.path.realpath(__file__)).parents[3])
        database_path = application_path + '/build_system/resources/database.db'

    print(application_path)
    print(database_path)
    return database_path


class SQLiteRepository(Repository):
    def __init__(self, model_cls):
        Repository.__init__(self, model_cls)

    def engine_factory(self):
        self.database_path = get_database_path()
        print(self.database_path)
        print("engine")
        return create_engine('sqlite:///' + self.database_path, echo=True)


#class MySQLRepository(Repository):
#    def __init__(self, model_cls):
#        Repository.__init__(self, model_cls)
#
#    def engine_factory(self):
#        return create_engine('mysql://scott:tiger@localhost/foo', echo=True)


#class PostgresRepository(Repository):
#    def __init__(self, model_cls):
#        Repository.__init__(self, model_cls)
#        
#    def engine_factory(self):
#        return create_engine('postgresql://scott:tiger@localhost/mydatabase', echo=True)



