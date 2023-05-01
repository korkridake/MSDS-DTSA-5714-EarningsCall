import requests
import io
import json

# Make a GET request to the Seeking Alpha API endpoint
url = "https://seeking-alpha.p.rapidapi.com/transcripts/v2/list"
querystring = {"id":"aapl","size":"20","number":"1"} # Set query parameters
headers = {
	"X-RapidAPI-Key": "a2d702a09bmshb89eec70e7c02edp173778jsnc274b366bb28",
	"X-RapidAPI-Host": "seeking-alpha.p.rapidapi.com"
} # Set headers
response = requests.get(url, headers=headers, params=querystring) # Send GET request
print(json.dumps(response.json(), indent = 1)) # Pretty-print the JSON response

# Extract the JSON data from the response
data = response.json()

# Connect to a MongoDB Atlas cluster
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://koak2789:oCge9tsmX9AozHKH@clustertesting-msds.bvcccni.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Get the database and collection objects
db = client.sample_earningcall # Get the database named "sample_earningcall"
collection = db.companylist # Get the collection named "companylist"

# Insert the JSON data into the collection
collection.insert_many(data["data"])

# Find and print the first document in the collection
print(collection.find_one())
