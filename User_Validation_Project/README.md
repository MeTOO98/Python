## User Email Validation Project

This is a simple Python project that checks if a user's email is valid and then verifies the email and password from a MongoDB database.

## What It Does

+ Asks the user to enter an email.

+ Checks if the email is in the correct format.

+ Looks for the email in a MongoDB collection.

+ If the email is found, asks for the password.

+ If the password is correct, it prints “Your access is valid”.


## Requirements

+ **Python 3**

+ **pymongo** library

+ A MongoDB database with a collection that has emails and passwords.

+ Function **Email_validation_1** inside Validation module.


## How to Use

1. Install pymongo if you don't have it:
```
pip install pymongo

```

2. Add MongoDB Connection
The script already connects using this format:
```
url='mongodb+srv://<username>:<password>@<cluster-address>/'

 ```
Replace it with your own MongoDB connection string if needed.

3. Make sure your MongoDB database has a collection called EMAILS with documents like:
```
{ "email": "example@example.com", "password": "yourpassword" }

```
4. Run the script:
```
python User_validation_pro.py

```
5. Follow the instructions in the terminal.

## Note

This script uses plain text passwords. For real projects, use hashed passwords.


