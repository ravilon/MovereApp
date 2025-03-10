from REST import database

def calculate():
    # Test DB
    db = database.get_db()
    collection_ref = db.collection("users")
    docs = collection_ref.stream()
    for doc in docs:
        print(f"Document ID: {doc.id}")
        print(f"Data: {doc.to_dict()}")
    
    return collection_ref