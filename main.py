# Part C: Michael 
from src.dataLoader import import_package_data, import_address_data, import_distance_data
from src.transportOrganizer import process_delivery, fleet_truck_1, fleet_truck_2, fleet_truck_3
from src.userInterface import display_interface

# Load package data into a custom hash table
import_package_data("project_resources/WGUPS_Package_File.csv")

# Load address information into a list
import_address_data("project_resources/Address_List.csv")

# Load distance metrics into a matrix for processing
import_distance_data("project_resources/WGUPS_Distance_Table.csv")

# Implement delivery process for each truck from transportOrganizer.py
process_delivery(fleet_truck_1)
process_delivery(fleet_truck_2)
process_delivery(fleet_truck_3)

# Launch the user interface from userInterface.py
display_interface()