# Part C: Incorporating Documented Data - Michael 
import csv
from src.package import Package
from src.hashTable import HashTable

# Initialize repository for packages and necessary data lists
package_registry = HashTable()
distance_chart = []
address_entries = []

# Function to import package data from a CSV and populate hash table
def import_package_data(csv_path):
    with open(csv_path) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        # Load and insert each row as package data in the hash table
        for row in csv_reader:
            pkg_id = int(row[0])
            addr = row[1]
            city = row[2]
            state = row[3]
            zip_code = int(row[4])
            deadline = row[5]
            weight = int(row[6])
            notes = row[7]

            # Insert package into hash table using ID as key
            package_registry.add(
                pkg_id,
                Package(pkg_id, addr, city, state, zip_code, deadline, weight, notes)
            )

# Function to load distances from a CSV into a distance matrix
def import_distance_data(csv_path):
    with open(csv_path) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        # Populate the distance matrix from CSV data
        for row in csv_reader:
            distance_chart.append(row)

        # Symmetrically fill distance matrix
        for i in range(len(distance_chart)):
            for j in range(len(distance_chart[i])):
                distance_chart[i][j] = distance_chart[j][i]

# Function to load addresses from a CSV into an address list
def import_address_data(csv_path):
    with open(csv_path) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        # Extract and store address information within list
        for row in csv_reader:
            address_entries.append(row[2])  # Capture relevant address field