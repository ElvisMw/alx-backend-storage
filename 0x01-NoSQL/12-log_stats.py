#!/usr/bin/env python3
"""
Script to provide stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


def print_stats(logs_collection):
    """
    Print stats about Nginx logs.

    Args:
        logs_collection (Collection): MongoDB collection with logs.
    """
    # Count the total number of logs
    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count the number of logs for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count the number of status checks
    status_check_count = logs_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Get the collection with logs
    logs_collection = client.logs.nginx

    # Print the stats
    print_stats(logs_collection)
