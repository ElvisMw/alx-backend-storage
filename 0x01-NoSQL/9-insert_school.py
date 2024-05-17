#!/usr/bin/env python3
""" 9-insert_school.py """

def insert_school(mongo_collection, **kwargs):
    """
    Insert a school into the MongoDB collection.

    Args:
        mongo_collection (Collection): MongoDB collection to insert into.
        **kwargs: Keyword arguments representing the school document to insert.

    Returns:
        ObjectId: The ID of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
