# TailNode Database Project

## Project Overview
This project involves using the below APIs to fetch Users and their corresponding posts data, Scrape books data and store it in their respective Databases on MongoDB Atlas, providing access to two different collections: one containing data from the Dummy API and another containing data scraped from a book website. The databases are hosted on MongoDB Atlas and are shared for collaborative purposes.

## Contents
- `users_list.py`: Python script to fetch users data from the Dummy API (https://dummyapi.io/data/v1/user) and store it in a MongoDB database.
- `users_posts.py`: Python script to fetch users post's data from the same Dummy API and store it in a MongoDB database.
- `books_scrape.py`: Python script to scrape books data from http://books.toscrape.com and store it in a MongoDB database.
- `README.md`: This README file providing an overview of the project, instructions for sharing the MongoDB Atlas URI securely, and details about the scripts.

## Getting Started
1. Install the required libraries:
   ```bash
   pip install requests beautifulsoup4 pymongo
   ```

2. Run the `users_list.py` script to fetch users data from the Dummy API and store it in MongoDB Atlas.

3. Run the `users_posts.py` script to fetch posts data from the Dummy API and store it in MongoDB Atlas.

4. Run the `books_scrape.py` script to scrape books data from the website and store it in MongoDB Atlas.

5. After running the scripts, use the MongoDB Atlas URI to view your database.

## Sharing MongoDB Atlas URI
To access the MongoDB Atlas database using the provided URI, follow these steps:

1. **Connect with MongoDB Compass:**
   - Open MongoDB Compass on your local machine.
   - Click on the "New Connection" button.
   - Paste the provided URI into the "Connection String" field.
   - Click "Connect" to establish a connection to the database.
   - You should now be able to view the database and collections in MongoDB Compass.

2. **Connect with MongoDB Shell:**
   - Open a terminal or command prompt.
   - Use the `mongo` command along with the provided URI to connect to the database. For example:
     ```bash
     mongo "mongodb+srv://satyamvirat:mnVq8nXwhXZB70mz@cluster0.9flhz7u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
     ```
   - You will be prompted to enter the password for the MongoDB Atlas user.
   - After successful authentication, you can use MongoDB shell commands to interact with the database.

3. **Share URI with MongoDB Atlas Project Access:**
   - If you have access to a MongoDB Atlas project, you can share the provided URI with other project members.
   - They can use this URI to connect to the database and view collections using MongoDB Atlas web interface.
   - URI : 
   ```bash
      mongodb+srv://satyamvirat:mnVq8nXwhXZB70mz@cluster0.9flhz7u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
   ```

## Potential Duplicate Key Error
If you encounter a `pymongo.errors.DuplicateKeyError` while running the scripts, it means there is already a document with the same `_id` value in the MongoDB collection. This error occurs because MongoDB does not allow multiple documents with the same `_id`.

### How to Handle:
To resolve the duplicate key error, you can:

1. **Add a New URI:** If you're running the script multiple times with the same URI, consider adding a new URI in the script or modifying the existing URI to generate unique `_id` values for each document.

2. **Delete Documents:** Alternatively, you can delete all documents from the affected collections before running the script again. This ensures that there are no duplicate `_id` values in the collection.

Ensure that you handle duplicate key errors appropriately based on your specific use case and requirements.


## Contact
For any questions or assistance regarding this project, feel free to contact Satyam at satyam.virat@outlook.com.
