# Takes input form the command line and initiates the controller
# passing command line input to the controller which then uses
# the information to initiate the model which parses the require file/files
from src.command_reader import CommandReader
from src.argument_reader import ArgumentReader
from src.controller import Controller

# from src.python_controller import Controller


def initiate_python_parser():
    command_reader = CommandReader()
    argument_reader = ArgumentReader()
    controller = Controller(command_reader, argument_reader)
    command_reader.set_controller(controller)
    argument_reader.set_controller(controller)
    argument_reader.parse_arguments()
    controller.run_console()


if __name__ == '__main__':
    initiate_python_parser()
    import doctest

    doctest.testmod()
