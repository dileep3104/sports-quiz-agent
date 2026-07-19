import json
import chromadb

from chromadb.utils import embedding_functions

from src.config import CHROMA_DB_PATH, DATA_PATH


def get_chroma_client():
    """
    Creates or connects to a persistent ChromaDB database.
    """
    return chromadb.PersistentClient(path=CHROMA_DB_PATH)


def get_collection():
    """
    Creates the sports collection if it doesn't exist.
    """
    client = get_chroma_client()

    embedding_function = embedding_functions.DefaultEmbeddingFunction()

    collection = client.get_or_create_collection(
        name="sports_history",
        embedding_function=embedding_function
    )

    return collection

def populate_database():
    """
    Reads sports_facts.json and inserts the facts into ChromaDB.
    """

    collection = get_collection()

    # Don't insert again if already populated
    if collection.count() > 0:
        print(f"Database already contains {collection.count()} facts.")
        return

    # Read JSON file
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        sports_data = json.load(file)

    documents = []
    metadatas = []
    ids = []

    for index, item in enumerate(sports_data):
        documents.append(item["fact"])
        metadatas.append({"sport": item["sport"]})
        ids.append(f"fact_{index}")

    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

    print(f"Successfully inserted {len(documents)} facts into ChromaDB.")


def query_database(sport, query_text, n_results=2):
    """
    Retrieves the most relevant facts for a given sport.
    """

    collection = get_collection()

    results = collection.query(
        query_texts=[query_text],
        n_results=n_results,
        where={"sport": sport}
    )

    return results["documents"][0]