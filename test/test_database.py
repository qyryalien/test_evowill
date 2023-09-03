import pytest
from database import Database


@pytest.fixture
def database():
    """
    Fixture to create a Database object for testing.

    This fixture initializes a Database object for testing purposes and returns it.

    :return: A Database object for testing.
    :rtype: Database
    """
    database = Database('activities.db')
    return database


def test_save_and_retrieve_activity(database):
    """
    Test the save_activity and get_latest_activities methods of the Database class.

    This test verifies the functionality of the save_activity method for saving an activity to the database and
    the get_latest_activities method for retrieving the latest activities.

    :param database: A Database object for testing.
    :type database: Database
    """
    activity_data = {
        "activity": "Test Activity",
        "type": "test",
        "participants": 3,
        "price": 0.5,
        "accessibility": 0.3
    }

    # Save the test activity to the database
    database.save_activity(activity_data)

    # Retrieve the latest activities from the database
    latest_activities = database.get_latest_activities(limit=1)

    # Assert that there is one latest activity and its attributes match the saved activity
    assert len(latest_activities) == 1
    assert latest_activities[0].activity == "Test Activity"
    assert latest_activities[0].type == "test"
    assert latest_activities[0].participants == 3
    assert latest_activities[0].price == 0.5
    assert latest_activities[0].accessibility == 0.3


def test_get_latest_activities(database):
    """
    Test the get_latest_activities method of the Database class.

    This test verifies the functionality of the get_latest_activities method for retrieving the latest activities.

    :param database: A Database object for testing.
    :type database: Database
    """

    # Add several test activities to the database
    for i in range(1, 10):
        activity_data = {
            "activity": f"Test Activity {i}",
            "type": "test",
            "participants": i,
            "price": i * 0.1,
            "accessibility": i * 0.2
        }
        database.save_activity(activity_data)

    # Retrieve the latest 5 activities from the database
    latest_activities = database.get_latest_activities(limit=5)

    # Assert that there are 3 latest activities with specific attributes and in the correct order
    assert len(latest_activities) == 5
    assert latest_activities[0].activity == "Test Activity 9"
    assert latest_activities[1].activity == "Test Activity 8"
    assert latest_activities[2].activity == "Test Activity 7"

    # Check the order of activities (latest should come first)
    assert latest_activities[0].id > latest_activities[1].id
    assert latest_activities[1].id > latest_activities[2].id
