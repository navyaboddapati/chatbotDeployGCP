import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")  # Replace with your file path
firebase_admin.initialize_app(cred)

db = firebase_admin.firestore.client()

# Functions for Firestore operations
def create_document(collection_name, data):
    doc_ref = db.collection(collection_name).document()
    doc_ref.set(data)
    return doc_ref.id

def read_documents(collection_name):
    docs = db.collection(collection_name).stream()
    return [doc.to_dict() for doc in docs]

def update_document(collection_name, doc_id, data):
    doc_ref = db.collection(collection_name).document(doc_id)
    doc_ref.update(data)

def delete_document(collection_name, doc_id):
    doc_ref = db.collection(collection_name).document(doc_id)
    doc_ref.delete()

# Functions for handling user queries
def get_locations():
    return read_documents('LocationCollection')

def get_events():
    return read_documents('NewsEventCollection')

def get_books():
    return read_documents('BookCollection')

def get_research():
    return read_documents('ResearchCollection')

def get_ask_data():
    return read_documents('AskCollection')