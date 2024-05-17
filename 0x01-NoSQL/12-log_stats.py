#!/usr/bin/env python3
"""
Script to print request logs and statistics from the nginx logs collection.
"""

from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    """
    Print the total number of logs and the number of logs for each HTTP method

    Args:
        nginx_collection (Collection): MongoDB collection
        containing nginx logs
    """
    # Count total number of logs
    print('{} logs'.format(nginx_collection.count_documents({})))

    # Count number of logs for each HTTP method
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))

    # Count number of status checks
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


def run():
    """
    Run the script.
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Print request logs and statistics
    print_nginx_request_logs(client.logs.nginx)


if __name__ == '__main__':
    run()
