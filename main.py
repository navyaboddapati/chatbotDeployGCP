from google.cloud import firestore

# Initialize Firestore client
db = firestore.Client()

def chatbot_function(request):
  
  # Parsing the incoming request
  request_data = request.get_json()
  user_query = request_data.get('query')
  
  # Processed user query and retrieve response from Firestore
  response = process_query(user_query)
  
  return {
      "response": response
  }
  
def process_query(query):
    
    if "book" in query.lower():
        return get_book_information(query)
    elif "hours" in query.lower():
        return get_library_hours()
    elif "policy" in query.lower():
        return get_library_policies()
    elif "event" in query.lower():
        return get_library_events()
    else:
        return "I'm sorry, I didn't understand your query. Please try rephrasing your question."

def get_book_information(query):
    
    # Parsing the user's query to extract the book title or author
    book_info = query.lower()
    if "title" in book_info:
        book_title = book_info.split("title")[1].strip()
        book_ref = db.collection("books").where("title", "==", book_title).limit(1)
    elif "author" in book_info:
        book_author = book_info.split("author")[1].strip()
        book_ref = db.collection("books").where("author", "==", book_author).limit(1)
    else:
        return "I'm sorry, I couldn't find the book information you requested. Please try again with book title or author."
    
    # Retrieve the book information from Firestore
    book_doc = next(book_ref.stream(), None)
    if book_doc:
        return book_doc.to_dict()
    else:
        return "Sorry, the book information is not available."

def get_library_hours():
    
    library_hours_ref = db.collection("library_hours").document("library_hours")
    library_hours_doc = library_hours_ref.get()
    if library_hours_doc.exists:
        library_hours = library_hours_doc.to_dict()["hours"]
        return f"The library hours are: {library_hours}"
    else:
        return "I'm sorry, I couldn't retrieve the library hours. Please check back later."
    
def get_library_policies():
    
    library_policies_ref = db.collection("library_policies").document("library_policies")
    library_policies_doc = library_policies_ref.get()
    if library_policies_doc.exists:
        library_policies = library_policies_doc.to_dict()["policies"]
        return f"The library policies are: {library_policies}"
    else:
        return "I'm sorry, I couldn't retrieve the library policies. Please check the library website for more information."

def get_library_events():
    
    library_events_ref = db.collection("library_events").document("library_events")
    library_events_doc = library_events_ref.get()
    if library_events_doc.exists:
        library_events = library_events_doc.to_dict()["events"]
        return f"The upcoming library events are: {library_events}"
    else:
        return "I'm sorry, I couldn't retrieve the library events. Please check the library website for more information."
