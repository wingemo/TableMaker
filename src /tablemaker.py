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
