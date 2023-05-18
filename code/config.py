import os
from pymongo import MongoClient
import boto3

def configure_MongoDB():
    """
    This function obtain the credentials to save the classification results in to MongoDB
    Return: username_mongo, password_mongo, hostname_mongo, dbname_mongo
    """
    username_mongo = os.environ.get('MONGO_USERNAME')
    password_mongo = os.environ.get('MONGO_PASSWORD')
    hostname_mongo = os.environ.get('MONGO_HOSTNAME')
    dbname_mongo = os.environ.get('MONGO_DBNAME')

    return username_mongo, password_mongo, hostname_mongo, dbname_mongo

username_mongo, password_mongo, hostname_mongo, dbname_mongo = configure_MongoDB()
mongo_uri = f"mongodb+srv://{username_mongo}:{password_mongo}@{hostname_mongo}/{dbname_mongo}?retryWrites=true&w=majority"

def mongodb_connect():
    """
    This function setup connection and create a mongodb database.
    Return: This function return the database and collection.
    """
    
    client = MongoClient(mongo_uri)
    db = client[dbname_mongo]
    db_collection = db['results']

    return db_collection


def aws_s3():
    """
    This function create a session, and s3 client.
    Return: Session, s3_client
    """

    session = boto3.Session(profile_name='default')
    s3_client = boto3.client('s3')

    return session, s3_client