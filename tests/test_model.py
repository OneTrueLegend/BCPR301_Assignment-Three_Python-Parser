# import unittest
#
# from src import model
# from src.controller import Controller
# from src.csv_plugin import CSVHandler
# from src.pickle_modules import PickleModules
# from src.python_code_validator import CodeValidator
#
#
# class ModelTestCase(unittest.TestCase):
#     """
#     Tests for 'model.py'
#     """
#
#     individual_file_upload = ["plants.py"]
#
#     def test_individual_file_processed(self):
#         """
#         Is individual module created after processing of file?
#         Author: Braeden
#         """
#         file_processor = model.FileProcessor()
#         modules = file_processor.process_files(self.individual_file_upload)
#
#         self.assertTrue(modules == 1)
#
#     def test_multiple_file_processed(self):
#         """
#         Is multiple modules created after processing of file?
#         Author: Braeden
#         """
#         file_processor = model.FileProcessor()
#         modules = file_processor.process_files(
#             ["plants.py", "controller.py"])
#
#         self.assertTrue(modules == 2)
#
#     def test_class_name(self):
#         """
#         Checks plants.py class names have been appended correctly
#         Author: Braeden
#         """
#         file_processor = model.FileProcessor()
#         file_processor.process_files(self.individual_file_upload)
#
#         self.assertTrue(file_processor.modules['plants'][0].name is 'Orchid')
#
#     def test_output_to_png(self):
#         """
#         Checks if creation of UML diagram and output to PNG file works
#         Author: Braeden
#         """
#         ctrl = Controller
#         self.assertTrue(ctrl.do_output_to_png(None) is 0)
#
#     def test_file_change(self):
#         """
#         Checks if file names that are stored from system
#         arguments can be changed by function
#         Author: Braeden
#         """
#         ctrl = Controller
#         ctrl.do_change_python_files(ctrl, "file_one.py file_two.py")
#
#         self.assertTrue(ctrl.files[0] == "file_one.py")
#
#     def test_public_function_symbol_checker(self):
#         """
#         Checks if the provided method name is
#         private, public or protected
#         Author: Braeden
#         """
#         md = model.FileProcessor()
#         visibility = md.get_visibility_of_string("public_function")
#
#         self.assertTrue(visibility == "+")
#
#     def test_private_function_symbol_checker(self):
#         """
#         Checks if the provided method name is
#         private, public or protected
#         Author: Braeden
#         """
#         md = model.FileProcessor()
#         visibility = md.get_visibility_of_string("__public_function")
#
#         self.assertTrue(visibility == "-")
#
#     def test_protected_function_symbol_checker(self):
#         """
#         Checks if the provided method name is
#         private, public or protected
#         Author: Braeden
#         """
#         md = model.FileProcessor()
#         visibility = md.get_visibility_of_string("_public_function")
#
#         self.assertTrue(visibility == "#")
#
#     def test_create_class_with_name(self):
#         """
#         Checks if class name is equal to one created
#         Author: Braeden
#         """
#         md = model.ClassNode("Class One", [])
#
#         self.assertTrue(md.name == "Class One")
#
#     def test_create_class_with_attributes(self):
#         """
#         Checks if class with attributes
#         tests if correct as created are stored
#         Author: Braeden
#         """
#         md = model.ClassNode("Class One", [])
#         md.add_attribute("Attribute One", "+")
#         md.add_attribute("Attribute Two", "+")
#
#         self.assertTrue(len(md.attributes) == 2)
#
#     def test_create_class_with_methods(self):
#         """
#         Checks if class with methods
#         tests if correct as created are stored
#         Author: Braeden
#         """
#         md = model.ClassNode("Class One", [])
#         md.add_function("Function One", [], "+")
#         md.add_function("Function Two", [], "+")
#
#         self.assertTrue(len(md.functions) == 2)
#
#     def test_create_class_with_super_classes(self):
#         """
#         Checks if class with methods
#         tests if correct as created are stored
#         Author: Braeden
#         """
#         md = model.ClassNode("Class One", [])
#         md.add_super_class(())
#         md.add_super_class(())
#
#         self.assertTrue(len(md.super_classes) == 2)
#
#     def test_create_function_with_name(self):
#         """
#         Checks if function name is equal to one created
#         Author: Braeden
#         """
#         md = model.FunctionNode("Function One", [], "+")
#
#         self.assertTrue(md.name == "Function One")
#
#     def test_create_attribute_with_name(self):
#         """
#         Checks if attribute name is equal to one created
#         Author: Braeden
#         """
#         md = model.AttributeNode("Attribute One", "+")
#
#         self.assertTrue(md.name == "Attribute One")
#
#     # Tests for csv_plugin.py
#     # Author Peter
#
#     def test_01_true_input(self):
#         testclass = CSVHandler()
#         example_type = dict()
#         expected = type(example_type)
#         actual = type(testclass.open_file('linkedlist.csv'))
#         self.assertEqual(expected, actual)
#
#     def test_02_false_input(self):
#         testclass = CSVHandler()
#         expected = False
#         actual = testclass.open_file('dreaming.csv')
#         self.assertEqual(
#             expected,
#             actual,
#             "Expected {} got {}".format(
#                 expected,
#                 actual))
#
#     def test_03_compare_output(self):
#         # Compares plugin output with output generated by model
#         data_for_model = ['linkedlist.py']
#         new_model_data = model.FileProcessor()
#         new_model_data.process_files(data_for_model)
#         model_data_module = new_model_data.get_modules()
#         testclass = CSVHandler()
#         expected = testclass.write_csv_file(
#             model_data_module, 'testdatafile02.csv')
#         test_module = testclass.open_file('test_data_file01.csv')
#
#     def test_04_compare_csv_with_output_file(self):
#         # compares a file already in csv form with a newly generated file based
#         # on the original
#         import filecmp
#         testclass = CSVHandler()
#         input_file = 'linkedlist.csv'
#         output_file = 'test_compare_file.csv'
#         module = testclass.open_file(input_file)
#         testclass.write_csv_file(module, output_file)
#         expected = True
#         actual = filecmp.cmp(input_file, output_file, True)
#         self.assertEqual(expected, actual)
#
#     # Tests for code_validator
#     # Author: Peter
#
#     def test_05_code_validator_true_input(self):
#         testclass = CodeValidator()
#         filename = 'linkedlist.py'
#         expected = True
#         actual = testclass.validate_file(filename)
#         self.assertEqual(expected, actual)
#
#     def test_06_code_validator_false_input(self):
#         testclass = CodeValidator()
#         filename = 'NoSuchPythonFile.py'
#         expected = False
#         actual = testclass.validate_file(filename)
#         self.assertEqual(expected, actual)
#
#     def test_07_code_validator_multiple_correct_files(self):
#         testclass = CodeValidator()
#         input_list = ['linkedlist.py', 'plants.py', 'csv_plugin.py']
#         expected = 3
#         actual = len(testclass.validate_files(input_list))
#         self.assertEqual(expected, actual)
#
#     def test_08_code_validator_multiple_incorrect_files(self):
#         testclass = CodeValidator()
#         input_list = ['linkedlist', 'plants', 'csv_plugin']
#         expected = 0
#         actual = len(testclass.validate_files(input_list))
#         self.assertEqual(expected, actual)
#
#     def test_09_code_validator_multiple_mixed_files(self):
#         testclass = CodeValidator()
#         input_list = ['linkedlist.py', 'plants.py', 'csv_plugin']
#         expected = 2
#         actual = len(testclass.validate_files(input_list))
#         self.assertEqual(expected, actual)
#
#     # Test pickle modules
#
#     def test_10_pickle_save(self):
#         pickler = PickleModules()
#         data = 12345
#         expected = True
#         actual = pickler.save(data)
#         self.assertEqual(expected, actual)
#
#     def test_11_pickle_load(self):
#         pickler = PickleModules()
#         expected = 12345
#         actual = pickler.load()
#         self.assertEqual(expected, actual)
#
#     def test_12_pickle_module(self):
#         data_for_model = ['plants.py']
#         new_model_data = model.FileProcessor()
#         new_model_data.process_files(data_for_model)
#         model_data_module = new_model_data.get_modules()
#         pickler = PickleModules()
#         expected = True
#         actual = pickler.save(model_data_module)
#         self.assertEqual(expected, actual)
#
#     def test_13_pickle_module(self):
#         data_for_model = ['plants.py']
#         new_model_data = model.FileProcessor()
#         new_model_data.process_files(data_for_model)
#         model_data_module = new_model_data.get_modules()
#         pickler = PickleModules()
#         expected = len(model_data_module)
#         actual = len(pickler.load())
#         self.assertEqual(expected, actual)
#
#     def test_14_pickle_module(self):
#         data_for_model = ['plants.py']
#         new_model_data = model.FileProcessor()
#         new_model_data.process_files(data_for_model)
#         pickler = PickleModules()
#         actual = True
#         try:
#             expected = TypeError
#             test = pickler.save()
#         except TypeError:
#             actual = TypeError
#         self.assertEqual(expected, actual)
#
#
# if __name__ == '__main__':
#     unittest.main()
