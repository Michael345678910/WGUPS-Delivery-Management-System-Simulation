# Part A: Designing a Hash Table - Michael 
# Part B: Create a Lookup Feature - Michael 
# Simple HashTable using chaining with lists
class HashTable:
    # Constructor to initialize with specified capacity
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]  # Create empty buckets for data

    # Add new data or update existing data with a key-value pair
    def add(self, key, value):
        index = self._get_index(key)  # Get bucket index
        bucket = self.buckets[index]  # Select corresponding bucket

        # Update existing key-value, if present
        for i in range(len(bucket)):
            if bucket[i][0] == key:  # Match key and update
                bucket[i][1] = value
                return True

        # If key not found, add new key-value entry
        bucket.append([key, value])
        return True

    # Retrieve value for a given key with lookup
    def lookup(self, key):
        index = self._get_index(key)  # Determine index
        bucket = self.buckets[index]  # Access associated bucket

        # Locate and return value for the provided key
        for k, v in bucket:
            if k == key:
                return v  # Return value if key is identified

        # Return None if key does not exist in hash table
        return None

    # Internal method to compute index for a key
    def _get_index(self, key):
        return hash(key) % self.size  # Ensure index remains within bounds of table