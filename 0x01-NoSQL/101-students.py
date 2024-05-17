#!/usr/bin/env python3
"""
Module for working with MongoDB and PyMongo.
"""
from pymongo import MongoClient


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
        collection object.

    Returns:
        list: A list of dictionaries representing the top students,
        sorted by average score.
              Each dictionary contains the student's ID, name,
              and average score.
    """
    students = []
    for student in mongo_collection.find():
        scores = [topic['score'] for topic in student['topics']]
        average_score = sum(scores) / len(scores) if scores else 0
        student['_id'] = str(student['_id'])
        student['averageScore'] = average_score
        students.append(student)

    return sorted(students, key=lambda x: x['averageScore'], reverse=True)
