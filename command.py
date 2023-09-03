class Command:
    def execute(self):
        """
        Execute the command.
        """
        pass


class NewCommand(Command):
    def __init__(self, api, database, args):
        """
        Initialize a command for fetching and saving a new activity.

        :param api: Object for working with the API
        :type api: ApiWrapper
        :param database: Object for working with the database
        :type database: Database
        :param args: Command-line arguments
        :type args: argparse.Namespace
        """
        self.api = api
        self.database = database
        self.args = args

    def execute(self):
        """
        Execute the command for fetching and saving a new activity.
        """
        filters = {
            "type": self.args.type,
            "participants": self.args.participants,
            "price_min": self.args.price_min,
            "price_max": self.args.price_max,
            "accessibility_min": self.args.accessibility_min,
            "accessibility_max": self.args.accessibility_max
        }

        filters = {key: value for key, value in filters.items() if value is not None}
        activity = self.api.get_random_activity(filters=filters)
        self.database.save_activity(activity)


class ListCommand(Command):
    def __init__(self, database):
        """
        Initialize a command for listing recent activities.

        :param database: Object for working with the database
        :type database: Database
        """
        self.database = database

    def execute(self):
        """
        Execute the command for listing recent activities.
        """
        latest_activities = self.database.get_latest_activities()
        for activity in latest_activities:
            print(activity)
