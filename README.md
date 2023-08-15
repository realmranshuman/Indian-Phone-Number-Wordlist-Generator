
# Indian Phone Number Wordlist Generator

The **Indian Phone Number Wordlist Generator** is a Python script that allows users, specifically ethical hackers and marketers, to generate wordlists of phone numbers based on various prefixes and suffixes. This tool is particularly useful for generating comprehensive lists of phone numbers for different telephone circles and purposes.

## Features
*   **Customizable Prefix Selection:** The script provides the flexibility to select prefixes from various tables in the provided SQLite database. Users can choose specific tables or use all available tables to generate prefixes.
    
*   **Automatic Suffix Generation:** The generator automatically generates numeric suffixes from 0 to 100,000. These suffixes can be added to the selected prefixes to create a wide range of phone number combinations.
    
*   **Batched Output:** The script writes the generated combinations of prefixes and suffixes to an output file in batches. This approach optimizes memory usage and makes it efficient to handle large datasets.

## Prerequisites


*   Python 3.x
*   SQLite3 module (usually included with Python)
*   A SQLite database file named `prefix.db` containing the necessary prefix tables.


## Usage


1.  Ensure you have the `prefix.db` database file in the same directory as the script.
    
2.  Open a terminal or command prompt.
    
3.  Navigate to the directory containing the script using the `cd` command.
    
4.  Run the script using the command:


```bash
python db-version.py
```

5.  The script will display the names of available tables in the database and prompt you to select the desired prefixes:

```python
The tables in the database are:
1. Andhra_Pradesh_And_Telengana
2. Assam
...
Enter the numbers of the tables you want to use as prefixes, separated by commas, or enter 0 to use all tables.
```
    
6.  Enter the numbers of the tables you want to use as prefixes, separated by commas. You can also enter `0` to use all tables.
    
7.  The script will generate combinations of prefixes and numeric suffixes and write them to a file named `combo.txt`.
    
8.  The output file will be created in the same directory as the script. It will contain phone number combinations in the format `prefix + suffix`.

## Examples

For example, if you select a specific prefix table and choose to generate combinations for the numbers 1, 3, and 5, the script will produce a wordlist similar to the following:

```
prefix1_00000
prefix1_00001
...
prefix1_99999


prefix3_00000
prefix3_00001
...
prefix3_99999


prefix5_00000
prefix5_00001
...
prefix5_99999
```

## Note

This tool is intended for ethical hacking and marketing purposes. Always ensure that you are using such tools responsibly and in compliance with relevant laws and regulations.


## Disclaimer

The tool's creators and maintainers are not responsible for any misuse or illegal activities conducted using the generated wordlists. Use the tool responsibly and ethically.


## License
This project is licensed under the [MIT License](https://github.com/realmranshuman/Indian-Phone-Number-Wordlist-Generator/blob/main/LICENSE).
