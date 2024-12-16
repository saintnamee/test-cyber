from flask import Flask, render_template
from pymongo import MongoClient


# client = MongoClient('mongodb://192.168.51.11:27017,192.168.51.12:27017,192.168.51.13:27017')  # Adjust the URI as needed
# db = client['mydatabase']  # Replace with your database name
# collection = db['mycollection']  # Replace with your collection name

def connect_mongodb():
    connection_string = ('mongodb://192.168.51.11:27017,192.168.51.12:27017,192.168.51.13:27017')
    cluster = MongoClient(connection_string) #connect to mongo
    return cluster
