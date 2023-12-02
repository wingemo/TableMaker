def create_stylish_table(data):
    try:
        # Validate input data
        if not isinstance(data, list) or not data:
            raise ValueError("Invalid input: Please provide a non-empty list of lists.")

        columns = len(data[0])

        # Check if all rows have the same number of columns
        if any(len(row) != columns for row in data):
            raise ValueError("Invalid input: All rows must have the same number of columns.")

        rows = len(data)
        column_widths = [max(len(str(data[i][j])) for i in range(rows)) for j in range(columns)]

        table_output = ""

        # Add the top border of the table
        for j in range(columns):
            table_output += f"+{'-' * (column_widths[j] + 2)}"
        table_output += "+\n"

        # Add the data rows with vertical borders and column width adjustment
        for i in range(rows):
            for j in range(columns):
                table_output += f"| {data[i][j]:<{column_widths[j]}} "
            table_output += "|\n"

        # Add the bottom border of the table
        for j in range(columns):
            table_output += f"+{'-' * (column_widths[j] + 2)}"
        table_output += "+\n"

        return table_output

    except ValueError as e:
        return str(e)

if __name__ == "__main__":
    # Skapa en argumentparser med beskrivning och epilog för hjälpmeddelanden
    parser = argparse.ArgumentParser(
        description="Create a stylish table from input data.",
        epilog="Example: python script.py '[Name, Age, City]' '[John Doe, 30, New York]' '[Jane Smith, 25, San Francisco]' '[Bob Johnson, 35, Los Angeles]'"
    )

    # Lägg till ett argument för listan
    parser.add_argument("data", nargs="+", help="Input data for the table in the format [item1, item2, ...].")

    try:
        # Analysera kommandoradsargumenten
        args = parser.parse_args()

        # Omvandla inmatade strängar till listor
        input_data = [eval(arg) for arg in args.data]

        # Anropa funktionen med den omvandlade listan
        stylish_table = create_stylish_table(input_data)
        print(stylish_table)

    except Exception as e:
        print(f"Error: {e}")
