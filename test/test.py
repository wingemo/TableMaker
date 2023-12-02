# test_tablemaker.py
import unittest
from tablemaker import create_stylish_table
import xmlrunner
import os

class TestTableMaker(unittest.TestCase):

    def test_create_stylish_table(self):
        input_data = [
            ["Name", "Age", "City"],
            ["John Doe", 28, "NY"],
            ["Jane Smith", 35, "LA"],
            ["Bob Johnson", 42, "SF"]
        ]

        expected_output = (
            "+-------------+--------+-------+\n"
            "| Name        | Age    | City  |\n"
            "+-------------+--------+-------+\n"
            "| John Doe    | 28     | NY    |\n"
            "| Jane Smith  | 35     | LA    |\n"
            "| Bob Johnson | 42     | SF    |\n"
            "+-------------+--------+-------+\n"
        )

        result = create_stylish_table(input_data)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    # Anger sökvägen till den befintliga mappen
    result_dir = "test_results"

    # Konfigurera och kör testerna
    with open(os.path.join(result_dir, "test_results.xml"), "wb") as output:
        runner = xmlrunner.XMLTestRunner(output=output)
        unittest.main(testRunner=runner)
