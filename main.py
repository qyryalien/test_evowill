import argparse

from api_wrapper import ApiWrapper, HttpRequestHandler
from command import NewCommand, ListCommand
from database import Database


def main(api, db):
    """
    Main application function.

    :param api: Object for working with the API
    :type api: ApiWrapper
    :param db: Object for working with the database
    :type db: Database
    """

    # Create a command-line argument parser with program description
    parser = argparse.ArgumentParser(description="Bored API Command Line Program")

    # Add subparsers for available commands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command to fetch and save a new activity
    new_parser = subparsers.add_parser("new", help="Fetch and save a new activity")
    new_parser.add_argument("--type", help="Filter by activity type")
    new_parser.add_argument("--participants", type=int, help="Number of participants")
    new_parser.add_argument("--price_min", type=float, help="Minimum price")
    new_parser.add_argument("--price_max", type=float, help="Maximum price")
    new_parser.add_argument("--accessibility_min", type=float, help="Minimum accessibility")
    new_parser.add_argument("--accessibility_max", type=float, help="Maximum accessibility")

    # Command to list recent activities
    subparsers.add_parser("list", help="List recent activities")

    # Parse command-line arguments
    args = parser.parse_args()

    # Create a dictionary of commands to execute
    commands = {
        "new": NewCommand(api, db, args),
        "list": ListCommand(db)
    }

    # Check which command the user requested and execute the corresponding command
    if args.command in commands:
        commands[args.command].execute()
    else:
        # Print help if an invalid command is specified
        parser.print_help()


if __name__ == "__main__":
    http_handler = HttpRequestHandler()
    api = ApiWrapper(http_handler)
    database = Database('activities.db')
    main(api, database)
