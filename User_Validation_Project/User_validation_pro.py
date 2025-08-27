from pymongo import MongoClient
from Validation import email_validation_1


url='mongodb+srv://<username>:<password>@cluster0.7kj70bb.mongodb.net/'
client=MongoClient(url)
db=client['sample_mflix']
collection =db.get_collection('EMAILS')

while True :
    u_email=input('Please Enter your email :')
    if email_validation_1(u_email) : 
        if collection.find_one({'email' :u_email}) :
            doc=collection.find_one({'email' :u_email})
            passw=input('and your password :')
            if passw == doc['password'] :
                print('Your access is valid')
            else :
                print('your password is not correct')
        else :
            print('your email is not found')

    else :
        print('your email is not valid')











