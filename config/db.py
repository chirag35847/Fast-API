from pymongo import MongoClient
connectionString = 'mongodb+srv://test:test@cluster0.j8ijako.mongodb.net/?retryWrites=true&w=majority'
conn = MongoClient(connectionString) 
db=conn['internship']
users = db['users']

workingHr=db['workingHr']
timezone=db['timezone']
status=db['status']