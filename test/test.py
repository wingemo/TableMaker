import unittest
import subprocess
import json
from your_module_name import create_stylish_table

class TestWholeProgram(unittest.TestCase):

    def setUp(self):
        # Läs in värden från JSON-konfigurationsfilen
        with open('test_config.json', 'r') as config_file:
            self.test_data = json.load(config_file)

    def run_test(self, test_name):
        test_case = self.test_data[test_name]
        input_data = test_case["input_data"]

        if "expected_output" in test_case:
            expected_output = test_case["expected_output"]
            result = subprocess.check_output(['python', 'your_script_name.py'] + input_data.split(), universal_newlines=True)
            self.assertEqual(result, expected_output, f"{test_name} output does not match expected output.")
        elif "error_message" in test_case:
            error_message = test_case["error_message"]
            with self.assertRaises(ValueError) as context:
                create_stylish_table(input_data)
            self.assertEqual(str(context.exception), error_message, f"{test_name} error message does not match expected error message.")

    def test_whole_program_command_line(self):
        self.run_test("command_line_test")

    def test_whole_program_module_import(self):
        self.run_test("module_import_test")

    def test_invalid_input(self):
        self.run_test("invalid_input_test")

    def test_empty_input(self):
        self.run_test("empty_input_test")

    def test_logging(self):
        self.run_test("logging_test")

    def test_column_widths(self):
        self.run_test("column_widths_test")

if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(resultclass=unittest.TextTestResult, stream=open('test_result/test_results.txt', 'w')))
