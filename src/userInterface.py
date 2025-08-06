# Part D: Intuitive Interface - Michael 
from src.transportOrganizer import fleet_truck_1, fleet_truck_2, fleet_truck_3, package_assignment, package_registry
import datetime

# Helper function to print a line with characters for visual dividers
def draw_line(char='-', length=100):
    print(char * length)

# Function to display a centered message within a banner
def show_banner(text):
    draw_line('=')
    print(text.center(100))
    draw_line('=')

# Convert a time string (HH:MM:SS) into a timedelta object
def parse_time_string(time_string):
    hrs, mins, secs = map(int, time_string.split(":"))
    return datetime.timedelta(hours=hrs, minutes=mins, seconds=secs)

# Main interface function to interact with users
def display_interface():
    # Present a welcome banner
    show_banner("WGUPS Delivery Overview")

    # Calculate and display the total distance traveled by all trucks
    total_miles = round(
        fleet_truck_1.total_distance + fleet_truck_2.total_distance + fleet_truck_3.total_distance, 1
    )
    print(f"\nCombined Miles by Fleet: {total_miles} miles")

    # Show delivered package summaries by truck
    draw_line('-')
    print(f"{fleet_truck_1.identifier} Packages Delivered: {fleet_truck_1.completed_parcels}")
    print(f"{fleet_truck_2.identifier} Packages Delivered: {fleet_truck_2.completed_parcels}")
    print(f"{fleet_truck_3.identifier} Packages Delivered: {fleet_truck_3.completed_parcels}")
    draw_line('-')

    # Menu loop for user interaction
    while True:
        # Display options and take user input in one step
        choice = input("\nPlease Select One Of The Following Options Via The Associated Number:\n (1) VIEW SINGLE PACKAGE STATUS\n (2) VIEW ALL PACKAGES STATUS\n (3) EXIT APPLICATION\n\nYour selection: ").strip()

        # Exit condition
        if choice == "3":
            print("\nThank you for using our application! | Application closed.")
            break

        # View status of a single package
        elif choice == "1":
            check_single_status()

        # View status of all packages at a specified time
        elif choice == "2":
            check_all_status()

        # Invalid selection response
        else:
            print("Invalid selection. Please choose a numerical option correlating to your needs: 1, 2, or 3.")

# Check the status of one package based on user input
def check_single_status():
    try:
        draw_line('~')
        time_input = input("Please enter the time using this format to view a package: (HH:MM:SS): ").strip()
        lookup_time = parse_time_string(time_input)
        pkg_id = int(input("Please enter the package ID: ").strip())
        package_info = package_registry.lookup(pkg_id)

        if package_info:
            truck_id = package_assignment.get(pkg_id, "Unknown")  # Find truck ID
            print(f"Assigned Truck: {truck_id}")
            print(package_info.details_at_time(lookup_time))
        else:
            print(f"Unfortunately, there was no package found with ID {pkg_id}.")
    except (ValueError, AttributeError) as error:
        print(f"Error: {error}. Please try again.")

# Display status of all packages at a given time
def check_all_status():
    try:
        draw_line('~')
        time_input = input("Please enter the time using this format to view packages: (HH:MM:SS): ").strip()
        lookup_time = parse_time_string(time_input)
        print("\n Packages at Requested Time:")
        draw_line('-')

        for pkg_id in range(1, 41):
            package_info = package_registry.lookup(pkg_id)
            if package_info:
                truck_id = package_assignment.get(pkg_id, "Unknown")
                print(f"Assigned Truck: {truck_id}")
                print(package_info.details_at_time(lookup_time))
            else:
                print(f"Package with ID {pkg_id} not found.")
    except ValueError as error:
        print(f"Error: {error}. Please try again.")