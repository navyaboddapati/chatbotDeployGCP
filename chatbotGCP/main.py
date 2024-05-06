import re
from flask import Flask, request, jsonify, render_template
from google.cloud import firestore

app = Flask(__name__)

# Initialize Firestore client
db = firestore.Client()

# Define functions for dynamic responses

def get_books_response(search_term=None):
    books_collection = db.collection('BookCollection')
    if search_term:
        query = books_collection.where('title', '>=', search_term.lower()).where('title', '<=', search_term.lower() + '\uf8ff')
        books = query.stream()
    else:
        books = books_collection.stream()
    
    book_info = ""
    for book in books:
        book_data = book.to_dict()
        book_info += f"<b>Title: {book_data.get('title', '')}</b><br>"
        book_info += f"Publisher: {book_data.get('publisher', '')}<br>"
        if book_data.get('identifier1'):
            book_info += f"{book_data.get('identifier1', '')}<br>"
        if book_data.get('identifier2'):
            book_info += f"{book_data.get('identifier2', '')}<br>"
        book_info += f"Link: <a href='{book_data.get('link', '')}'>{book_data.get('link', '')}</a><br><br>"
    
    if book_info:
        return book_info
    else:
        return "No books found in the library database."

def get_bookt_response(search_term):
    books_collection = db.collection('BookCollection')
    query = books_collection.where('title', '>=', search_term.lower()).where('title', '<=', search_term.lower() + '\uf8ff')
    books = query.stream()
    
    book_info = ""
    for book in books:
        book_data = book.to_dict()
        book_info += f"<b>Title: {book_data.get('title', '')}</b><br>"
        book_info += f"Publisher: {book_data.get('publisher', '')}<br>"
        if book_data.get('identifier1'):
            book_info += f"{book_data.get('identifier1', '')}<br>"
        if book_data.get('identifier2'):
            book_info += f"{book_data.get('identifier2', '')}<br>"
        book_info += f"Link: <a href='{book_data.get('link', '')}'>{book_data.get('link', '')}</a><br><br>"
    
    if book_info:
        return book_info
    else:
        return "No books found in the library database."

def get_events_response():
    events_collection = db.collection('NewsEventCollection')
    events = events_collection.stream()
    
    event_info = "<b>Here are the upcoming events:</b><br>"
    for event in events:
        event_data = event.to_dict()
        event_info += f"<b>{event_data.get('title', '')} on {event_data.get('date', '')}</b><br>"
        event_info += f"Link: <a href='{event_data.get('link', '')}'>{event_data.get('link', '')}</a><br>"
    
    if event_info:
        return event_info
    else:
        return "There are no upcoming events at the moment."

def get_locations_response():
    locations_collection = db.collection('LocationCollection')
    locations = locations_collection.stream()
    
    location_info = "<b>Here are the library locations:</b><br>"
    for location in locations:
        location_data = location.to_dict()
        location_info += f"<b>{location_data.get('library', '')}</b><br>"
        location_info += f"Link: <a href='{location_data.get('link', '')}'>{location_data.get('link', '')}</a><br>"
    
    if location_info:
        return location_info
    else:
        return "No library locations found in the database."

def get_central_response():
    locations_collection = db.collection('LocationCollection')
    query = locations_collection.where('library', '>=', 'central').where('library', '<=', 'central\uf8ff')
    central_location = next(query.stream(), None)
    
    if central_location:
        location_data = central_location.to_dict()
        location_info = "<b>Central Library</b><br>"
        location_info += f"Link: <a href='{location_data.get('link', '')}'>{location_data.get('link', '')}</a><br>"
        return location_info
    else:
        return "Central library location not found in the database."

def get_west_response():
    locations_collection = db.collection('LocationCollection')
    query = locations_collection.where('library', '>=', 'west').where('library', '<=', 'west\uf8ff')
    west_location = next(query.stream(), None)
    
    if west_location:
        location_data = west_location.to_dict()
        location_info = "<b>West Campus Library</b><br>"
        location_info += f"Link: <a href='{location_data.get('link', '')}'>{location_data.get('link', '')}</a><br>"
        return location_info
    else:
        return "West Campus library location not found in the database."

def get_science_response():
    locations_collection = db.collection('LocationCollection')
    query = locations_collection.where('library', '>=', 'science').where('library', '<=', 'science\uf8ff')
    science_location = next(query.stream(), None)
    
    if science_location:
        location_data = science_location.to_dict()
        location_info = "<b>Science and Engineering Library</b><br>"
        location_info += f"Link: <a href='{location_data.get('link', '')}'>{location_data.get('link', '')}</a><br>"
        return location_info
    else:
        return "Science and Engineering library location not found in the database."

def get_research_response():
    research_collection = db.collection('ResearchCollection')
    research_items = research_collection.stream()
    
    research_info = "<b>Here are some research resources:</b><br>"
    for item in research_items:
        item_data = item.to_dict()
        research_info += f"<b>{item_data.get('title', '')}</b><br>"
        research_info += f"Link: <a href='{item_data.get('link', '')}'>{item_data.get('link', '')}</a><br>"
    
    if research_info:
        return research_info
    else:
        return "No research resources found in the database."

def get_ask_response():
    ask_collection = db.collection('AskCollection')
    ask_items = ask_collection.stream()
    
    ask_info = "<b>Here are some frequently asked questions:</b><br>"
    for item in ask_items:
        item_data = item.to_dict()
        ask_info += f"<b>{item_data.get('question', '')}</b><br>"
        ask_info += f"{item_data.get('answer', '')}<br><br>"
    
    if ask_info:
        return ask_info
    else:
        return "No frequently asked questions found in the database."

# Define a dictionary of patterns and responses

responses = {
    r'hi|hello': 'Hello!',
    r'how are you?': 'I\'m doing well, thank you!',
    r'who are you?': 'I\'m UTA Library Chatbot.',
    r'what is your name?': 'My name is UTA Library Chatbot.',
    r'events?': get_events_response,
    r'bookt:\s*(.*)': lambda x: get_bookt_response(x.group(1)),
    r'books?': get_books_response,
    r'locations?': get_locations_response,
    r'central library|central|library central|main library|main': get_central_response,
    r'west campus library|west|campus|west library|campus library|west campus': get_west_response,
    r'science and engineering library|science & engineering library|science library|engineering library|science engineering|science engineering library': get_science_response,
    r'research': get_research_response,
    r'ask?': get_ask_response,
    r'quit|exit': 'Goodbye!'
}

# Define main response handling function

def get_response(user_input):
    user_input = user_input.lower()

    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            if callable(response):  # Check if the response is a function
                return response()  # If it is, call the function and return its result
            return response  # Otherwise, return the response string

    # Check if the user input matches a book title
    book_match = re.match(r'^(\w+(\s\w+)*)$', user_input)
    if book_match:
        search_term = book_match.group(1)
        return get_bookt_response(search_term)
    
    return "I'm sorry, I didn't understand that."

# Define Flask routes

@app.route('/get-response', methods=['POST'])
def handle_request():
    user_input = request.get_json().get('message')
    response = get_response(user_input)
    return jsonify({'response': response})

@app.route('/')
def serve_index():
    return render_template('index.html')

# Run the Flask app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)