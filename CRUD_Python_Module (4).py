# This the an class that can create a connection to the aac database,so it can be a 
#crud for the animals collection. After initializing the connection, one method
#inserts a document, and the other reads a document. Both use API calls.
#getNextRecord() generates a new id for create()

from pymongo import MongoClient 
from bson.objectid import ObjectId

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 
        
    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username 
        PASS = password 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d?authSource=admin' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # This method generates a ObjectId for the create method.
    def getNextRecord(self):
        id = ObjectId()
        return id
    
    # This create method to implement the C in CRUD.
    # this method creates and inserts a document 
    #into a collection using API call
    def create(self, data):
        if data is not None:
            id = self.getNextRecord()
            data['_id'] = id
            #1
            result = self.collection.insert_one(data)  # data should be dictionary
            return result
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # This method implements the R in CRUD. This method reads
    #a document using API call
    def read(self, data):
        result = self.collection.find(data)
        return list(result)
    
    #This method updates documents in aac
    #The first argument will be the search key/value pair that will find the document you want to update.
    #The second will be the pair to replace the corrosponding field.
    #this method return the number of modified files
    def update(self, search, data):
        result = self.collection.update_many(search, data)
        return result.modified_count
    
    #This method deletes documents from aac
    #It will search the database using a key/value pair and return the number of deleted documents.
    def delete(self, data):
        result = self.collection.delete_many(data)
        return result.deleted_count
    
    