# Part C: Building Truck Class for Delivery Implementation - Michael 
class Truck:
    def __init__(self, parcels, leave_time, identifier):
        # Truck specific identifiers
        self.identifier = identifier
        self.capacity_limit = 16
        self.speed_mph = 18

        # Starting and ending locations
        self.origin = "4001 South 700 East"
        self.current_location = self.origin
        self.destination_hub = "4001 South 700 East"

        # Track delivery metrics and parcels
        self.total_distance = 0.0
        self.pending_parcels = parcels
        self.completed_parcels = []

        # Manage scheduling with timestamps
        self.start_time = leave_time
        self.current_time = leave_time
        self.return_time = None

        # Log for mileage tracking
        self.mileage_log = []

    # Retrieve a summary of truck activity
    def get_log_overview(self):
        log_summary = (
            f" {self.identifier} Log Overview:\n"
            f"  Start: {self.start_time}\n"
            f"  End: {self.current_time}\n"
            f"  Total Distance: {self.total_distance} miles\n"
        )
        return log_summary