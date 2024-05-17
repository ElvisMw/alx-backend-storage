#!/usr/bin/env python3
"""
Module for providing statistics about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient
from collections import Counter


def print_nginx_request_logs(nginx_collection):
    """
    Prints stats about Nginx request logs.

    Args:
        nginx_collection (pymongo.collection.Collection): The MongoDB
        collection object.
    """
    # Count total logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count request methods
    print("Methods:")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = nginx_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {req_count}")

    # Count status checks
    status_checks_count = nginx_collection.count_documents(
        {'method': 'GET', 'path': '/status'}
    )
    print(f"{status_checks_count} status check")

    # Count IP addresses
    print("IPs:")
    ips = Counter(doc['ip'] for doc in nginx_collection.find())
    for ip, count in ips.most_common(10):
        print(f"\t{ip}: {count}")
