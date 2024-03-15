import requests
import pymongo

# MongoDB Atlas config
mongo_client = pymongo.MongoClient("mongodb+srv://satyamvirat:mnVq8nXwhXZB70mz@cluster0.9flhz7u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = mongo_client["dummy_users"]
collection = db["users_list"]

# API endpoint
api_url = "https://dummyapi.io/data/v1/user"
headers = {"app-id": "65f3e8b85b40673670e8017e"}

# Fetch user data from the API
response = requests.get(api_url, headers=headers)
user_data = response.json().get('data', [])

# Insert user data into the MongoDB collection
for user in user_data:
    user_info = {
        "_id": user['id'],
        "title": user['title'],
        "firstName": user['firstName'],
        "lastName": user['lastName'],
        "picture": user['picture']
    }
    collection.insert_one(user_info)

print("User data fetched and stored in MongoDB.")
