#!/usr/bin/env python3

"""Functions for working with MongoDB collections."""


def list_all(mongo_collection):
    """Return a list of all documents in the MongoDB collection.

    Args:
        mongo_collection (Collection): MongoDB collection to query.

    Returns:
        list: List of documents in the collection.
    """
    return [doc for doc in mongo_collection.find()]
