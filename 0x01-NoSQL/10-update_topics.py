#!/usr/bin/env python3
""" 10-update_topics.py """


def update_topics(mongo_collection, name, topics):
    """
    Update the topics field for all documents in the MongoDB collection
    where the name matches the given name.

    Args:
        mongo_collection (Collection): MongoDB collection to update.
        name (str): Name to match.
        topics (list): List of topics to update.

    Returns:
        None
    """
    # Update all documents where the name matches the given name
    # by setting the 'topics' field to the given topics list.
    mongo_collection.update_many(
        {'name': name},  # match documents where the name equals the given name
        {'$set': {'topics': topics}}  # update the 'topics' field
    )
