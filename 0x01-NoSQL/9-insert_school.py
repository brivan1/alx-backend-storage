#!/usr/bin/env python3
'''
This module houses the script needed to insert a document using pymongo
'''


def insert_school(mongo_collection, **kwargs):
    '''
    function that inserts a new document in a collection based on kwargs
    Args:
        mongo_collection: pymongo collection object
        kwargs: key word arguments given to insert
    Returns:
        the new id for the document
    '''
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
