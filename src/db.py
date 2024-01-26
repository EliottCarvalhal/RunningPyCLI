from pymongo.mongo_client import MongoClient
from data import Run, calculate_pace
from decouple import config

uri = config("MONGO_URI")
client = MongoClient(uri)
db = client["run"]
collection = db["runV1"]


def add_to_db(run):
    run_data = {"dist": run.dist, "time": run.time, "date": run.date}
    res = collection.insert_one(run_data)
    if res.inserted_id:
        print(f"Run inserted with ID : {res.inserted_id}")
    else:
        raise ValueError("Failed to insert run")


def query_top5(gte, lte):
    query = {"dist": {"$gte": gte, "$lte": lte}}
    res = collection.find(query).sort("time", 1).limit(5)

    for index, run_data in enumerate(res, start=1):
        run = Run(**run_data)
        pace = calculate_pace(run.dist, run.time)
        print(
            f"{index}. {run.dist} km in {run.time} on {run.date} with pace {pace} min/km"
        )


def query_all():
    res = list(collection.find({}))
    runs = [Run(**run_data) for run_data in res]
    return runs


try:
    client.admin.command("ping")

    print("Successfully connected to MongoDB")
except Exception as e:
    print(e)
