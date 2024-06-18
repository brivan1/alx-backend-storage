#!/usr/bin/env python3
'''
list dbs in mongo using py
'''


def list_all(mongo_collection):
    '''
    lists all colections
    Args:
        mongo_collection a dbs

    Return:
        empty list if no mcollection
        list of all collections if found
    '''
    if mongo_collection.count() == 0:
        return []
    else:
        return mongo_collection.find()
