# GUI

1. Install dependencies: pip install -r Requirements.txt
2. Uncomment line 262 in app.py to create_data and run python app.py 
3. Now GUI will open, feel free to explore


______________________________________

Additional Info:
Here we have used helper.py to generate multiple copies of images, feel free to run that 
in case you want to create imagery data. for that firstly download any two images from internet 
and name them 1.jpg and 2.jpg then run python helper.py

Please note naming is done based on its unit_id in the database.

If you don't have mongodb installed, do that first and then maybe you need to change 
"mydatabase" "mycollection" 'mongodb://localhost:27017/' strings based on your mongodb setup 
and db name

# Set up the MongoDB client
client = MongoClient('mongodb://localhost:27017/')

# Connect to the database
db = client['mydatabase']

# Create the units collection
units_collection = db['mycollection']