import builtins
import os
import unittest
from pathlib import Path
from unittest import mock

from src.controller import Controller


class ModelTestCase(unittest.TestCase):
    single_file_test = ["../tmp/plants.py"]
    multi_file_test = ["../tmp/plants.py", "../src/model.py"]

    def setUp(self):
        if os.path.exists("UnitTest.db"):
            os.remove("UnitTest.db")

    def tearDown(self):
        if os.path.exists("UnitTest.db"):
            os.remove("UnitTest.db")

    """
    #1
    Bad Smell: Large Class
    """

    def test_cmd_enable_statistics(self):
        """
        Location: 'python_controller.py-Controller-whole file'
        Testing whether statistics can be enabled by the command method
        Author: Jake
        """
        controller = Controller()
        m = mock.MagicMock(name='input')
        m.side_effect = ['enable_statistics', 'quit']
        builtins.input = m
        controller.run_console()
        actual = controller.statistics
        self.assertIsNotNone(actual)

    def test_cmd_set_input_file(self):
        """
        Location: 'python_controller.py-Controller-whole file'
        Testing whether input files can be selected by gui
        Author: Jake
        """
        controller = Controller()
        m = mock.MagicMock(name='input')
        m.side_effect = ['set_input_file', 'quit']
        builtins.input = m
        controller.run_console()
        actual = controller.files
        self.assertIsNotNone(actual)

    def test_cmd_set_input_file_args(self):
        """
        Location: 'python_controller.py-Controller-whole file'
        Testing whether input files can be selected by arguments
        Author: Jake
        """
        expected = ["plants.py"]
        controller = Controller()
        m = mock.MagicMock(name='input')
        m.side_effect = ['set_input_file plants.py', 'quit']
        builtins.input = m
        controller.run_console()
        actual = controller.files
        self.assertEqual(actual, expected)

    def test_output_file(self):
        """
        Location: 'python_controller.py-Controller-whole file'
        Testing whether file will be output to destination
        Author: Jake
        """
        controller = Controller()
        m = mock.MagicMock(name='input')
        m.side_effect = ['output_to_file E:\ARA work', 'quit']
        builtins.input = m
        controller.run_console()
        actual = Path('E:\ARA work\class.png').exists()
        self.assertTrue(actual)

    """
    #2
    Duplicate Code
    """

    def test_cmd_enable_statistics(self):
        """
        Location: 'python_controller.py-Controller-Lines (68-70, 122-139)'
        Testing whether statistics can be enabled by the command method
        Author: Jake
        """
        controller = Controller()
        m = mock.MagicMock(name='input')
        m.side_effect = ['enable_statistics', 'quit']
        builtins.input = m
        controller.run_console()
        actual = controller.statistics
        self.assertIsNotNone(actual)

    def test_cmd_set_input_file(self):
        """
        Location: 'python_controller.py-Controller-Lines (45-60, 122-139)'
        Testing whether input files can be selected by gui
        Author: Jake
        """
        controller = Controller()
        m = mock.MagicMock(name='input')
        m.side_effect = ['set_input_file', 'quit']
        builtins.input = m
        controller.run_console()
        actual = controller.files
        self.assertIsNotNone(actual)

    def test_cmd_set_input_file_args(self):
        """
        Location: 'python_controller.py-Controller-Lines (45-60, 122-139)'
        Testing whether input files can be selected by arguments
        Author: Jake
        """
        expected = ["plants.py"]
        controller = Controller()
        m = mock.MagicMock(name='input')
        m.side_effect = ['set_input_file plants.py', 'quit']
        builtins.input = m
        controller.run_console()
        actual = controller.files
        self.assertEqual(actual, expected)

    """
    #3
    Bad Smell: Long Method
    """

    # def test_model_process_single_class(self):
    #     """
    #     Location: 'model.py-FileProcessor-process_class-Lines(126-170)'
    #     Testing whether the file processor will still process a class
    #     correctly and return the correct number of modules using one file
    #     Author: Jake
    #     """
    #     expected = 1
    #
    #     statistics = StatisticsCreator("RefactorTestDB")
    #     statistics.create_tables()
    #
    #     file_processor = model.FileProcessor(statistics)
    #     modules = file_processor.process_files(self.single_file_test)
    #
    #     actual = modules
    #
    #     self.assertEqual(expected, actual)
    #
    # def test_model_process_multi_class(self):
    #     """
    #     Location: 'model.py-FileProcessor-process_class-Lines(126-170)'
    #     Testing whether the file processor will still process a class
    #     correctly and return the correct number of modules using multiple files
    #     Author: Jake
    #     """
    #     expected = 2
    #
    #     statistics = StatisticsCreator("RefactorTestDB")
    #     statistics.create_tables()
    #
    #     file_processor = model.FileProcessor(statistics)
    #     modules = file_processor.process_files(self.multi_file_test)
    #
    #     actual = modules
    #
    #     self.assertEqual(expected, actual)
    #
    # def test_run_parser_single(self):
    #     """
    #     Location: 'model.py-FileProcessor-process_class-Lines(126-170)'
    #     Testing whether the processed module can be
    #     used to create a uml diagram with a single file
    #     Author: Jake
    #     """
    #     statistics = StatisticsCreator("RefactorTestDB")
    #     statistics.create_tables()
    #
    #     processor = model.FileProcessor(statistics)
    #     processor.process_files(self.single_file_test)
    #
    #     extracted_modules = processor.get_modules()
    #
    #     new_uml = uml_out.MakeUML(False, False)
    #
    #     expected = new_uml.create_class_diagram(extracted_modules)
    #
    #     controller = Controller()
    #     controller.files = self.single_file_test
    #     actual = controller.run_parser(False, False)
    #
    #     self.assertEqual(expected, actual)
    #
    # def test_run_parser_multi(self):
    #     """
    #     Location: 'model.py-FileProcessor-process_class-Lines(126-170)'
    #     Testing whether the processed module can be
    #     used to create a uml diagram with multiple files
    #     Author: Jake
    #     """
    #     statistics = StatisticsCreator("RefactorTestDB")
    #     statistics.create_tables()
    #
    #     processor = model.FileProcessor(statistics)
    #     processor.process_files(self.multi_file_test)
    #
    #     extracted_modules = processor.get_modules()
    #
    #     new_uml = uml_out.MakeUML(False, False)
    #
    #     expected = new_uml.create_class_diagram(extracted_modules)
    #
    #     controller = Controller()
    #     controller.files = self.multi_file_test
    #     actual = controller.run_parser(False, False)
    #
    #     self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
