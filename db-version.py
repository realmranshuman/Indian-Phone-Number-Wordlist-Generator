# Import sqlite3 module to work with the database
import sqlite3

# Import itertools module to create product generator
import itertools

# Define a function to generate prefixes from the selected tables
def generate_prefixes(choice, tables):
    # Connect to the database file
    conn = sqlite3.connect("prefix.db")

    # Create a cursor object to execute queries
    cursor = conn.cursor()

    if choice == "0":
        # Use all tables
        for table in tables:
            cursor.execute(f"SELECT value FROM {table[0]}")
            values = cursor.fetchall()
            for value in values:
                yield str(value[0])
    else:
        # Use only the chosen tables
        numbers = choice.split(",")
        for number in numbers:
            # Validate the input
            try:
                index = int(number) - 1
                if index < 0 or index >= len(tables):
                    raise ValueError
            except ValueError:
                print(f"Invalid input: {number}")
                continue
            
            # Get the values from the table
            table = tables[index]
            cursor.execute(f"SELECT value FROM {table[0]}")
            values = cursor.fetchall()
            for value in values:
                yield str(value[0])

    # Close the database connection
    conn.close()

# Define a function to generate suffixes from 0 to 100000
def generate_suffixes():
    for i in range(100001):
        yield str(i).zfill(5)

# Define a function to write the combinations of prefix and suffix in batches
def write_combinations(prefixes, suffixes, batch_size):
    # Create a file named combo.txt and write the combinations of prefix and suffix
    with open("combo.txt", "w") as f:
        batch = []
        # Use itertools.product to create a generator that produces all the combinations of prefixes and suffixes
        for combination in itertools.product(prefixes, suffixes):
            batch.append(combination[0] + combination[1] + "\n")
            if len(batch) == batch_size:
                # Write the batch to the file and clear it
                f.writelines(batch)
                batch.clear()
        # Write any remaining items in the batch
        if batch:
            f.writelines(batch)

# Get the names of the tables in the database
conn = sqlite3.connect("prefix.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
conn.close()

# Print the table names and ask the user to select one or more or all
print("The tables in the database are:")
for i, table in enumerate(tables):
    print(f"{i+1}. {table[0]}")
print("Enter the numbers of the tables you want to use as prefixes, separated by commas, or enter 0 to use all tables.")
choice = input()

# Generate prefixes from the selected tables
prefixes = generate_prefixes(choice, tables)

# Generate suffixes from 0 to 100000
suffixes = generate_suffixes()

# Write the combinations of prefix and suffix in batches of 10000
write_combinations(prefixes, suffixes, 10000)

print("The file combo.txt has been created with the combinations.")
