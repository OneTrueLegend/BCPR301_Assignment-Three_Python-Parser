# Takes input form the command line and initiates the controller 
# passing command line input to the controller which then uses
# the information to initiate the model which parses the require file/files

import sys
import python_controller as pc


def initiate_python_parser(command_line_args):
    controller = pc.Controller(command_line_args)
    #controller.run_parser(command_line_args, True, True)


if __name__ == '__main__' :
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file", nargs="+", help="Multiple file input for parse")

    #Created By Jake Reddock
    parser.add_argument("-s", "--statistics", action='store_true', help="Print Statistics for classes uploaded")

    args = parser.parse_args()
    initiate_python_parser(args)

    import doctest
    doctest.testmod()
