from google.cloud import firestore
from google.oauth2 import service_account

# Replace these values with your actual project details
PROJECT_ID = 'chat-422418'
SERVICE_ACCOUNT_EMAIL = 'chatbot-firestore-impersonate@chat-422418.iam.gserviceaccount.com'
# Create the credentials object
credentials = service_account.IDTokenCredentials.from_service_account_file(
    'chatbot-impresonate-key.json',
    target_audience='https://firestore.googleapis.com/',
)

# Impersonate the service account
impersonated_credentials = credentials.with_target_service_account(
    SERVICE_ACCOUNT_EMAIL
)

# Initialize the Firestore client with the impersonated credentials
db = firestore.Client(project=PROJECT_ID, credentials=impersonated_credentials)

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