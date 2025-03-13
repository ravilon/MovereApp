from REST import database

def calculate(params):
    # Test DB
    db = database.get_db()
    collection_ref = db.collection("users")
    docs = collection_ref.stream()
    output = "Results: \n"
        
    for doc in docs:
        print(f"Document ID: {doc.id}")
        print(f"Data: {doc.to_dict()}")
        output += f"Document ID: {doc.id} \n"
        output += f"Data: {doc.to_dict()} \n"
    
    return output