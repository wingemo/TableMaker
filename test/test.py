import unittest
import subprocess
from your_module_name import create_stylish_table

class TestWholeProgram(unittest.TestCase):

    def test_whole_program_command_line(self):
        input_data = "Name Age City\nJohn Doe 30 New York\nJane Smith 25 San Francisco\nBob Johnson 35 Los Angeles"
        expected_output = "+----------------+-----+-----------------+\n| Name           | Age | City            |\n+----------------+-----+-----------------+\n| John Doe       | 30  | New York        |\n| Jane Smith     | 25  | San Francisco  |\n| Bob Johnson    | 35  | Los Angeles     |\n+----------------+-----+-----------------+\n"

        # Kör programmet som en separat process och hämta stdout
        result = subprocess.check_output(['python', 'your_script_name.py'] + input_data.split(), universal_newlines=True)

        self.assertEqual(result, expected_output, "Command line program output does not match expected output.")

    def test_whole_program_module_import(self):
        input_data = [['Name', 'Age', 'City'], ['John Doe', '30', 'New York']]
        expected_output = "+---------------+-----+-----------+\n| Name          | Age | City      |\n+---------------+-----+-----------+\n| John Doe      | 30  | New York  |\n+---------------+-----+-----------+\n"

        # Anropa funktionen med den omvandlade listan och få utmatningen
        result = create_stylish_table(input_data)

        self.assertEqual(result, expected_output, "Module output does not match expected output.")

    def test_invalid_input(self):
        invalid_input_data = [['Name', 'Age', 'City'], ['John Doe', '30']]  # Mismatched columns
        with self.assertRaises(ValueError):
            create_stylish_table(invalid_input_data)

    def test_empty_input(self):
        empty_input_data = []  # Empty list
        with self.assertRaises(ValueError):
            create_stylish_table(empty_input_data)

    def test_logging(self):
        # Testa att loggning fungerar som förväntat
        input_data = [['Name', 'Age', 'City'], ['John Doe', '30', 'New York']]
        with self.assertLogs() as log:
            create_stylish_table(input_data)
            self.assertIn("Stylish table created successfully.", log.output)

    def test_column_widths(self):
        # Testa att korrekt beräkning av kolumnbredder görs
        input_data = [['Name', 'Age', 'City'], ['John Doe', '30', 'New York']]
        result = create_stylish_table(input_data)
        self.assertIn("+---------------+-----+-----------+", result)

if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(resultclass=unittest.TextTestResult, stream=open('test_result/test_results.txt', 'w')))
