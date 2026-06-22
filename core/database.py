import pickle

def load_database():

    with open(
        "song_database.pkl",
        "rb"
    ) as f:

        database = pickle.load(f)

    return database