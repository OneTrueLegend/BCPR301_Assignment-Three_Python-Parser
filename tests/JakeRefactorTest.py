import unittest
import os

#from src.controller import Controller as Controller
from src.command_reader import CommandReader as Controller


class ModelTestCase(unittest.TestCase):

    def setUp(self):
        if os.path.exists("UnitTest.db"):
            os.remove("UnitTest.db")

    def tearDown(self):
        if os.path.exists("UnitTest.db"):
            os.remove("UnitTest.db")

    def test_cmd_set_input_file_args(self):
        """
        Can you select a file from command arguments?
        Author: Jake
        """
        controller = Controller()
        controller.do_set_input_file("plants.py")

        self.assertEqual(controller.files, ["plants.py"])


if __name__ == '__main__':
    unittest.main()
