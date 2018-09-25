import unittest
import os
import src.uml_output as uml_out
from src import model
from src.controller import Controller
from src.statistics_creator import StatisticsCreator


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

    """
    #2
    Duplicate Code
    """

    """
    #3
    Bad Smell: Long Method
    """

    def test_model_process_single_class(self):
        """
        Location: 'model.py-FileProcessor-process_class-Lines(126-170)'
        Testing whether the file processor will still process a class
        correctly and return the correct number of modules using one file
        Author: Jake
        """
        expected = 1

        statistics = StatisticsCreator("RefactorTestDB")
        statistics.create_tables()

        file_processor = model.FileProcessor(statistics)
        modules = file_processor.process_files(self.single_file_test)

        actual = modules

        self.assertEqual(expected, actual)

    def test_model_process_multi_class(self):
        """
        Location: 'model.py-FileProcessor-process_class-Lines(126-170)'
        Testing whether the file processor will still process a class
        correctly and return the correct number of modules using multiple files
        Author: Jake
        """
        expected = 2

        statistics = StatisticsCreator("RefactorTestDB")
        statistics.create_tables()

        file_processor = model.FileProcessor(statistics)
        modules = file_processor.process_files(self.multi_file_test)

        actual = modules

        self.assertEqual(expected, actual)

    def test_run_parser_single(self):
        """
        Location: 'model.py-FileProcessor-process_class-Lines(126-170)'
        Testing whether the processed module can be
        used to create a uml diagram with a single file
        Author: Jake
        """
        statistics = StatisticsCreator("RefactorTestDB")
        statistics.create_tables()

        processor = model.FileProcessor(statistics)
        processor.process_files(self.single_file_test)

        extracted_modules = processor.get_modules()

        new_uml = uml_out.MakeUML(False, False)

        expected = new_uml.create_class_diagram(extracted_modules)

        controller = Controller()
        controller.files = self.single_file_test
        actual = controller.run_parser(False, False)

        self.assertEqual(expected, actual)

    def test_run_parser_multi(self):
        """
        Location: 'model.py-FileProcessor-process_class-Lines(126-170)'
        Testing whether the processed module can be
        used to create a uml diagram with multiple files
        Author: Jake
        """
        statistics = StatisticsCreator("RefactorTestDB")
        statistics.create_tables()

        processor = model.FileProcessor(statistics)
        processor.process_files(self.multi_file_test)

        extracted_modules = processor.get_modules()

        new_uml = uml_out.MakeUML(False, False)

        expected = new_uml.create_class_diagram(extracted_modules)

        controller = Controller()
        controller.files = self.multi_file_test
        actual = controller.run_parser(False, False)

        self.assertEqual(expected, actual)

    """
    #4
    Bad Smell: Dead Code
    """


if __name__ == '__main__':
    unittest.main()
