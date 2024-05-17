#!/usr/bin/env python3
"""
Module for providing statistics about Nginx logs stored in MongoDB.
"""
import pymongo


def print_nginx_stats(nginx_logs):
    """
    Prints stats about Nginx request logs.

    Args:
        nginx_logs (pymongo.collection.Collection): The MongoDB
        collection object.
    """
    total_logs = nginx_logs.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        method_count = nginx_logs.count_documents({'method': method})
        print(f"{method}: {method_count}")

    print("Status Checks:")
    status_checks_count = nginx_logs.count_documents(
        {'method': 'GET', 'path': '/status'}
    )
    print(f"{status_checks_count} status checks")

    print("Top IPs:")
    ips = pymongo.Counter(doc['ip'] for doc in nginx_logs.find())
    for ip, count in ips.most_common(10):
        print(f"{ip}: {count}")
