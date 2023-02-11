

from pydracula.model.repository.repository import Base
from sqlalchemy import Column, Integer, String


class Note(Base):
    __tablename__ = 'note'
    id = Column(Integer, primary_key=True)
    text = Column(String(1000), nullable=False)
    x = Column(Integer, nullable=False, default=0)
    y = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return "<Note(text='%s', x='%s', y='%s')>" % (
            self.text,
            self.x,
            self.y,
        )
