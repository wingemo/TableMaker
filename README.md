# Table Maker Program

## Introduction

The Table Maker Program is a Python utility designed to create stylish text-based tables in terminal from tabular data. This simple yet effective tool allows users to generate aesthetically pleasing tables with automatic column width adjustment.

## Features

- **Create Stylish Tables:** Utilize the `create_stylish_table` function to generate visually appealing text-based tables
  
- **Automatic Column Width Adjustment:** Ensure consistent and aesthetic presentation of data with automatic column width adjustment.

- **Error Handling:** The program includes robust error handling to manage incorrect input formats, providing clear error messages.

## Usage

1. **Import the Module:**

    ```python
    import tablemaker
    ```

2. **Prepare Tabular Data:**

    ```python
    data = [
        ["Name", "Age", "City"],
        ["John Doe", 28, "NY"],
        ["Jane Smith", 35, "LA"],
        ["Bob Johnson", 42, "SF"]
    ]
    ```

3. **Create and Print the Table:**

    ```python
    tablemaker.create_table(data)
    ```

    <table>
  <tr>
    <th>Name</th>
    <th>Age</th>
    <th>City</th>
  </tr>
  <tr>
    <td>John Doe</td>
    <td>30</td>
    <td>New York</td>
  </tr>
  <tr>
    <td>Jane Smith</td>
    <td>25</td>
    <td>San Francisco</td>
  </tr>
  <tr>
    <td>Bob Johnson</td>
    <td>35</td>
    <td>Los Angeles</td>
  </tr>
</table>


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/table-maker.git
    ```

2. Navigate to the project directory:

    ```bash
    cd table-maker
    ```

3. Run the program:

    ```bash
    python your_program_name.py
    ```

## Requirements

- Python 3.x

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This program is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to [OpenAI](https://www.openai.com/) for providing the underlying technology that powers this assistant.

Enjoy creating stylish tables with the Table Maker Program!

