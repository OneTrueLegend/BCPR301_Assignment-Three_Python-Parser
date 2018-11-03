import argparse


class ArgumentReader:
    def __init__(self, controller):
        self.controller = controller
        self.args = self.register_arguments()
        self.parse_arguments()

    # Created by Jake
    @staticmethod
    def register_arguments():
        # Create your commands in here
        parser = argparse.ArgumentParser()
        # Created by Braeden
        parser.add_argument(
            "-f",
            "--file",
            nargs="+",
            help="Multiple file input for parse")
        # Created By Jake Reddock
        parser.add_argument(
            "-s",
            "--statistics",
            action='store_true',
            help="Print Statistics for classes uploaded")
        parser.add_argument(
            "-d",
            "--database",
            help="Selects which database will be used")
        # Created By Michael Huang
        parser.add_argument(
            "-o",
            "--output",
            help="Setting name of the output location")
        return parser.parse_args()

    # Created By Jake Reddock
    def parse_arguments(self):
        if self.args.database is not None:
            self.controller.set_database(self.args.database)

        if self.args.statistics:
            self.controller.enable_statistics()

        if self.args.file is not None:
            self.controller.set_input_files(self.args.file)


