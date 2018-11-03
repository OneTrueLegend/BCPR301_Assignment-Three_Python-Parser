import src.uml_output as uml_out
from src import model
from src.Database.MySQLDatabaseFactory import MySQLDatabaseFactory
from src.Database.SQLiteDatabaseFactory import SQLiteDatabaseFactory
from src.Statistics.PlotlyStatisticsCreator import PlotlyStatisticsCreator
from src.argument_reader import ArgumentReader
from src.command_reader import CommandReader


class Controller:
    def __init__(self):
        # Command line argument variables
        self.files = None
        self.statistics = None
        self.extracted_modules = None
        self.database = None
        self.command_reader = CommandReader(self)
        self.argument_reader = ArgumentReader(self)

    def set_database(self, database_type=None):
        if database_type == 'mysql':
            self.database = MySQLDatabaseFactory("statistics")
            print('MySQL Database Selected')
        else:
            self.database = SQLiteDatabaseFactory("statistics")
            print('SQLite Database Selected')

    def run_console(self):
        self.command_reader.cmdloop('Starting prompt...\n'
                                    'Type "help" for commands')

    def get_command_reader(self):
        return self.command_reader

    # Edited by Jake
    def run_parser(self, hide_attributes, hide_methods):
        if len(self.files) > 0:
            # Initiate processor
            processor = model.FileProcessor(self.statistics)
            processor.process_files(self.files)

            self.extracted_modules = processor.get_modules()

            new_uml = uml_out.MakeUML(hide_attributes, hide_methods)
            return new_uml.create_class_diagram(self.extracted_modules)
        else:
            print("Error: No files were set, use command change_python_files")

    def set_input_files(self, files):
        self.files = files
        if self.files == "":
            print("No input file selected.")
        else:
            print("Input file selected:")
            print(*self.files, sep="\n")

    def enable_statistics(self):
        if self.database is None:
            self.set_database()
        self.statistics = PlotlyStatisticsCreator(self.database)
        self.statistics.create_tables()
        print("Statistics collecting is turned on")
