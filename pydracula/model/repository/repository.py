"""
This is Python implementation of Repository pattern for accessing Data model
in an Object Oriented manner, simulating collection interface and abstracting
persistence operations.
The Repository also has Factory method for dealing with different Databases. Another
approach is to add direct engine string ingestion to the Repository __init__ method.
"""
import abc

from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RepositoryInterface(abc.ABC):
    @abc.abstractmethod
    def create(self, *args, **kwargs):
        raise NotImplemented()

    @abc.abstractmethod
    def list(self):
        raise NotImplemented()

    @abc.abstractmethod
    def get(self, id_):
        raise NotImplemented()

    @abc.abstractmethod
    def update(self, **fields):
        raise NotImplemented()

    @abc.abstractmethod
    def delete(self, id_):
        raise NotImplemented()


class Repository(RepositoryInterface):
    def __init__(self, model_cls):
        engine = self.engine_factory()
        Base.metadata.create_all(engine)
        self.session = Session(bind=engine)
        self.model_cls = model_cls

    def create(self, *args, **kwargs):
        obj = self.model_cls(*args, **kwargs)
        self.session.add(obj)
        self.session.commit()

    def list(self):
        return list(self.session.query(self.model_cls).order_by(self.model_cls.id))

    def get(self, id_):
        return self.session.query(self.model_cls).get(id_)

    def update(self, id_, **fields):
        obj = self.get(id_)
        for field, value in fields.items():
            obj.__setattr__(field, value)
        self.session.commit()

    def delete(self, id_):
        self.session.delete(self.get(id_))

    @abc.abstractmethod
    def engine_factory(self):
        # Factory method
        raise NotImplemented()


