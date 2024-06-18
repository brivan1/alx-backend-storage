#!/usr/bin/env python3
'''
change topic in a collection
'''


def update_topics(mongo_collection, name, topics):
    '''
    change topics
    '''
    mongo_collection.update_many(
            {'name': name},
            {'$set': {'topics': topics}}
            )
