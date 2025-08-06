# Part B: Description of Each Package Component - Michael 
import datetime  # Import required library for handling time

# Define a Package class for package detail management
class Package:
    def __init__(self, pkg_id, address, city, state, zip_code, deadline, weight, notes, allocated_truck=None):
        self.pkg_id = pkg_id  # Unique identifier for the package
        self.delivery_address = address  # Destination address
        self.delivery_city = city  # Delivery city
        self.delivery_state = state  # Delivery state
        self.delivery_zip = zip_code  # ZIP code for delivery
        self.deadline = deadline  # Scheduled delivery deadline
        self.weight_kg = weight  # Package weight
        self.delivery_notes = notes  # Additional instructions or notes
        self.allocated_truck = allocated_truck  # Assigned truck for delivery
        self.dispatch_time = None  # Time when the package left the hub
        self.delivery_time = None  # Time when delivery was completed
        self.status = "at hub"  # Initial status of the package

    # Return package status at a specified query time
    def details_at_time(self, query_time):
        # Specific update for address corrections in package #9
        if self.pkg_id == 9 and query_time >= datetime.timedelta(hours=10, minutes=20):
            self.delivery_address = "410 S State St"
            self.delivery_city = "Salt Lake City"
            self.delivery_zip = 84111

        # Determine status based on current time in comparison to dispatch and delivery
        if self.delivery_time and query_time >= self.delivery_time:
            state = f"Status: completed | Delivered At: {self.delivery_time}"
        elif self.dispatch_time and self.delivery_time > query_time > self.dispatch_time:
            state = "Status: in transit"
        else:
            state = "Status: at hub"

        # Format and return package details
        return (
            f"Package ID: {self.pkg_id}\t"
            f"Address: {self.delivery_address}\t City: {self.delivery_city}\t State: {self.delivery_state}\t"
            f"ZIP Code: {self.delivery_zip}\t Deadline: {self.deadline}\t"
            f"Weight(kg): {self.weight_kg}\t {state}\t Notes: {self.delivery_notes}"
        )