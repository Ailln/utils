from pymongo import MongoClient


def get_db(config):
    mongo_config = config["mongo"]
    user = mongo_config["user"]
    pwd = mongo_config["pwd"]
    host = mongo_config["host"]
    port = mongo_config["port"]
    db_name = mongo_config["db_name"]
    client = MongoClient(f"mongodb://{user}:{pwd}@{host}:{port}/{db_name}")
    return client[db_name]
