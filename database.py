from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Activity, metadata


class Database:
    def __init__(self, db_name):
        """
        Initialize an object for working with the database.

        :param db_name: SQLite database file name
        :type db_name: str
        """
        # Initializing the database and creating a table
        self.engine = create_engine(f'sqlite:///{db_name}')
        metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def save_activity(self, activity_data):
        """
        Save an activity to the database.

        :param activity_data: Activity data to be saved
        :type activity_data: dict
        """
        # Saving the activity in the database
        session = self.Session()
        new_activity = Activity(**activity_data)
        session.add(new_activity)
        session.commit()
        session.close()

    def get_latest_activities(self, limit=5):
        """
        Get the latest activities from the database.

        :param limit: Maximum number of activities to retrieve
        :type limit: int
        :return: List of the latest activities
        :rtype: list of dict
        """
        # Retrieve recent activity from the database
        session = self.Session()
        latest_activities = session.query(Activity).order_by(Activity.id.desc()).limit(limit).all()
        session.close()
        return latest_activities
