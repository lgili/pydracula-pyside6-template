import sqlite3
import os

from pydracula import DATABASE_FILE
import pydracula.model.user as user




def createDB():
    """Checks if the file exists and creates the database and soon after inserts the default user"""
    if(not os.path.isfile(DATABASE_FILE)):
        # Create table
        user.UserDAO.createTable()
        # Create default user
        user.UserDAO.add(user.User(name=''))
