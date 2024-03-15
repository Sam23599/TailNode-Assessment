import requests
import pymongo

# MongoDB Atlas config
mongo_client = pymongo.MongoClient("mongodb+srv://satyamvirat:mnVq8nXwhXZB70mz@cluster0.9flhz7u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = mongo_client["dummy_users"]
users_collection = db["users_list"]
posts_collection = db["users_posts"]

# API endpoint
posts_api_url = "https://dummyapi.io/data/v1/user/{}/post"
headers = {"app-id": "65f3e8b85b40673670e8017e"}

# Fetch users list from the database
users_list = users_collection.find({}, {"_id": 1})

# Iterate over each user to fetch their posts data
for user in users_list:
    user_id = user["_id"]
    user_posts_api_url = posts_api_url.format(user_id)

    # Fetch posts data for the current user
    response = requests.get(user_posts_api_url, headers=headers)
    posts_data = response.json().get('data', [])
    
    # Insert posts data into the database
    for post in posts_data:
        post_info = {
            "id": post["id"],
            "image": post["image"],
            "likes": post["likes"],
            "tags": post["tags"],
            "text": post["text"],
            "publishDate": post["publishDate"],
            "owner": {
                "id": post["owner"]["id"],
                "title": post["owner"]["title"],
                "firstName": post["owner"]["firstName"],
                "lastName": post["owner"]["lastName"],
                "picture": post["owner"]["picture"]
            }
        }
        posts_collection.insert_one(post_info)

print("Posts data fetched and stored in MongoDB.")
