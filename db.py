from pymongo import MongoClient

# Set up the MongoDB client
client = MongoClient('mongodb://localhost:27017/')

# Connect to the database
db = client['mydatabase']

# Create the units collection
units_collection = db['mycollection']


    
def create_data():
    # Generate 100 units with 10% bad units
    bad_unit_count = 10
    for i in range(1, 101):
        sku_id = "SKU1"
        unit_id = i
        if i <= bad_unit_count:
            status = "Bad"
        else:
            status = "Good"
        unit = {"sku_id": sku_id, "unit_id": unit_id, "status": status}
        units_collection.insert_one(unit)
