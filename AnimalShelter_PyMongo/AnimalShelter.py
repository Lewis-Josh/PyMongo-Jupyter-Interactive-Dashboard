from pymongo import MongoClient
from pymongo.errors import OperationFailure
import logging
from bson.objectid import ObjectId

logging.basicConfig(level=logging.INFO, filename="debug.log")

class AnimalShelter(object):
    
    def __init__(self): # Initialize variables
        USER='aacuser'
        PASS=1240
        HOST='nv-desktop-services.apporto.com'
        PORT=30087
        DB='AAC'
        COL='animals'
        
        try:
           
            self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT)) # Initialize Client URL
            self.database = self.client[DB] # Initialize Database from Client Object
            self.collection = self.database[COL] # Initialize Collection from Database Object
            
        except OperationFailure as ex:
            logging.error(f"Error connecting to the database: {ex}")
            raise


    """CRUD operations for Animal collection in MongoDB."""
    
    def create(self, data: dict) -> bool:
        """Create an entry in the collection."""
        if not data:
            logging.info("Nothing to import, because data is empty")
            return False

        try:
            result = self.collection.insert_one(data)
            return result.acknowledged
        except OperationFailure as ex:
            logging.error(f"Error inserting document: {ex}")
            return False

    def read(self, query: dict = None) -> list:
        """Query the collection and return matching entries."""
        if query is None:
            query = {}

        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except OperationFailure as ex:
            logging.error(f"Error retrieving data: {ex}")
            return []

    def update(self, query: dict, newData: dict) -> bool:
        """Update a query with new data in the collection."""
        if not query or not newData:
            logging.error("A query and data are required to update an entry.")
            return False
         
        try:
            result = self.collection.update_one(query, {"$set": newData})
            return result.modified_count > 0
        except OperationFailure as ex:
            logging.error(f"Error updating document: {ex}")
            return False

    def delete(self, query: dict, data: dict = None) -> bool:
        """Delete documents from the collection."""
        if data is None:
            result = self.collection.delete_many(query)
        else:
            result = self.collection.delete_one(data)
        
        if result.deleted_count > 0:
            print("Deletion Complete")
        else:
            print("No matching documents found.")
        
        return result.deleted_count > 0