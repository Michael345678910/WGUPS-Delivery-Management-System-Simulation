# Part C: Overseeing Package Deliveries - Michael
import datetime
from src.dataLoader import address_entries, distance_chart, package_registry
from src.truck import Truck

# Initialize trucks with parcel allocations and departure times
# Truck 1 Starting at 8:00 AM
fleet_truck_1 = Truck(
    [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40],
    datetime.timedelta(hours=8, minutes=0), "Truck 1"
)

# Truck 2 Starting at 9:05 AM
fleet_truck_2 = Truck(
    [3, 6, 18, 25, 28, 32, 36, 38, 7, 8, 5, 22, 23, 24, 26],
    datetime.timedelta(hours=9, minutes=5), "Truck 2"
)

# Truck 3 Starting at 10:20 AM
fleet_truck_3 = Truck(
    [2, 4, 9, 10, 11, 12, 17, 21, 27, 33, 35, 39],
    datetime.timedelta(hours=10, minutes=20), "Truck 3"
)

# Map packages to truck identifications
package_assignment = {
    **{pkg_id: "Truck 1" for pkg_id in fleet_truck_1.pending_parcels},
    **{pkg_id: "Truck 2" for pkg_id in fleet_truck_2.pending_parcels},
    **{pkg_id: "Truck 3" for pkg_id in fleet_truck_3.pending_parcels},
}


# Utility function for drawing lines
def draw_line(char='-', length=100):
    print(char * length)


# Locate and return address index within address list
def locate_address_index(address):
    return address_entries.index(address)


# Determine distance between addresses using distance chart
def compute_distance(addr_origin, addr_destination):
    return float(distance_chart[locate_address_index(addr_origin)][locate_address_index(addr_destination)])


# Identify the next closest package to be delivered
def identify_next_package(truck):
    distances = []

    # Evaluate each package for proximity
    for pkg_id in truck.pending_parcels:
        parcel = package_registry.lookup(pkg_id)
        dist = compute_distance(truck.current_location, parcel.delivery_address)
        distances.append(float(dist))

    # Determine minimum distance and associated package index
    closest_distance = min(distances)
    index_closest = distances.index(closest_distance)

    return index_closest, closest_distance


# Orchestrate delivery of packages using closest first approach
def process_delivery(truck):
    # Update packages to "in transit" upon truck departure
    for pkg_id in truck.pending_parcels:
        parcel = package_registry.lookup(pkg_id)
        parcel.status = "in transit"
        parcel.dispatch_time = truck.start_time

    truck.current_time = truck.start_time

    # Deliver until all packages on the truck are completed
    while truck.pending_parcels:
        # Select closest package and its distance
        closest_index, closest_distance = identify_next_package(truck)
        closest_parcel = package_registry.lookup(truck.pending_parcels[closest_index])

        # Update location and mileage
        truck.current_location = closest_parcel.delivery_address
        truck.total_distance += closest_distance
        truck.current_time += datetime.timedelta(hours=closest_distance / truck.speed_mph)

        # Mark package as completed
        closest_parcel.status = "completed"
        closest_parcel.delivery_time = truck.current_time

        # Transfer package to completed list
        truck.completed_parcels.append(truck.pending_parcels.pop(closest_index))

    # Calculate and log the return journey distance back to the hub
    final_parcel = package_registry.lookup(truck.completed_parcels[-1])
    round_trip_distance = compute_distance(final_parcel.delivery_address, truck.destination_hub)

    # Track truck's round-trip mileage and time
    truck.total_distance += round_trip_distance
    truck.total_distance = round(truck.total_distance, 1)
    truck.current_time += datetime.timedelta(hours=round_trip_distance / truck.speed_mph)

    # Print the delivery summary for this truck
    draw_line('-')
    summary_header = f" {truck.identifier} Delivery Recap"
    print(summary_header.center(100))
    draw_line('-')
    print(f"Truck Departed At: {truck.start_time}")
    print(f"Returned To Hub At: {truck.current_time}")
    print(f"Overall Distance: {truck.total_distance} miles")
    draw_line('=')