import argparse
import logging

# Skapa en rotloggare om ingen annan logger skickas in
logger = logging.getLogger(__name__)

def configure_logging(log_level):
    # Konfigurera loggning för rotloggaren om ingen annan logger skickas in
    if not logger.hasHandlers():
        logger.setLevel(log_level)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

def calculate_column_widths(data):
    columns = len(data[0])
    rows = len(data)
    return [max(len(str(data[i][j])) for i in range(rows)) for j in range(columns)]

def generate_top_border(column_widths):
    return "+".join("-" * (width + 2) for width in column_widths) + "+\n"

def generate_data_rows(data, column_widths):
    rows = len(data)
    columns = len(data[0])
    table_output = ""
    
    for i in range(rows):
        for j in range(columns):
            table_output += f"| {data[i][j]:<{column_widths[j]}} "
        table_output += "|\n"
    
    return table_output

def generate_bottom_border(column_widths):
    return generate_top_border(column_widths)

def create_stylish_table(data):
    try:
        # Validate input data
        if not isinstance(data, list) or not data:
            raise ValueError("Invalid input: Please provide a non-empty list of lists.")

        columns = len(data[0])

        # Check if all rows have the same number of columns
        if any(len(row) != columns for row in data):
            raise ValueError("Invalid input: All rows must have the same number of columns.")

        column_widths = calculate_column_widths(data)
        table_output = generate_top_border(column_widths)
        table_output += generate_data_rows(data, column_widths)
        table_output += generate_bottom_border(column_widths)

        # Logga att tabellen har skapats framgångsrikt
        logger.info("Stylish table created successfully.")

        return table_output

    except ValueError as e:
        # Logga ett felmeddelande om ogiltig inmatning
        logger.error(f"Error: {e}")
        return str(e)

if __name__ == "__main__":
    # Skapa en argumentparser med beskrivning och epilog för hjälpmeddelanden
    parser = argparse.ArgumentParser(
        description="Create a stylish table from input data.",
        epilog="Example: python script.py 'Name Age City' 'John Doe 30 New York' 'Jane Smith 25 San Francisco' 'Bob Johnson 35 Los Angeles'"
    )

    # Lägg till argument för listan och loggnivå
    parser.add_argument("data", nargs="+", help="Input data for the table in the format 'item1 item2 ...'.")
    parser.add_argument("--log_level", default="INFO", help="Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL).")

    try:
        # Analysera kommandoradsargumenten
        args = parser.parse_args()

        # Konfigurera loggning med användarens valda loggnivå
        log_level = getattr(logging, args.log_level.upper(), None)
        if not isinstance(log_level, int):
            raise ValueError("Invalid log level. Please choose one of: DEBUG, INFO, WARNING, ERROR, CRITICAL.")
        configure_logging(log_level)

        # Omvandla inmatade strängar till listor
        input_data = [arg.split() for arg in args.data]

        # Anropa funktionen med den omvandlade listan
        stylish_table = create_stylish_table(input_data)
        print(stylish_table)

    except Exception as e:
        # Logga ett generellt felmeddelande om något går fel
        logger.exception(f"An unexpected error occurred: {e}")
