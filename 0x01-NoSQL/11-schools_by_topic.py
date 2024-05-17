#!/usr/bin/env python3
""" 11-schools_by_topic.py """


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of documents from the MongoDB collection where the given topic
    exists in the 'topics' field.

    Args:
        mongo_collection (Collection): MongoDB collection to query.
        topic (str): Topic to match.

    Returns:
        list: List of documents where the given topic exists in the 'topics' field.
    """
    # Create a filter to match documents where the given topic exists in the 'topics' field
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    # Use the filter to find matching documents in the MongoDB collection
    return [doc for doc in mongo_collection.find(topic_filter)]
