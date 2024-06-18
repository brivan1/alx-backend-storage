#!/usr/bin/env python3
'''
function that returns the list of school having a specific topic
'''


def schools_by_topic(mongo_collection, topic):
    '''
    Retrieve schools that have a specific topic in their 'topics' field

    Args:
        mongo_collection (obj): pymongo collection object
        topic (str): Topic to search for in schools

    Returns:
        list: List of school documents matching the topic
    '''
    schools = mongo_collection.find({"topics": {"$in": [topic]}})
    return list(schools)
