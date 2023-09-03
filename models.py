from sqlalchemy import Column, Integer, String, Float, MetaData
from sqlalchemy.orm import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class Activity(Base):
    """
    Represents an activity entity stored in the 'activities' table.

    :param Base: The base class for SQLAlchemy models.
    :type Base: sqlalchemy.ext.declarative.declarative_base
    """

    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    activity = Column(String)
    type = Column(String)
    participants = Column(Integer)
    price = Column(Float)
    link = Column(String, nullable=True)
    key = Column(String)
    accessibility = Column(Float)

    def __str__(self):
        """
        Return a string representation of the Activity object.

        :return: String representation of the Activity object.
        :rtype: str
        """

        return (
            f"Activity(id={self.id}, "
            f"activity='{self.activity}', "
            f"type='{self.type}', "
            f"participants={self.participants}, "
            f"price={self.price}, "
            f"accessibility={self.accessibility}, "
            f"link='{self.link}')")
