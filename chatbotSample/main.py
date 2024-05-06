import re
import sqlite3
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Define functions for dynamic responses

def get_books_response(search_term=None):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    if search_term:
        c.execute("SELECT * FROM BookCollection WHERE LOWER(title) LIKE ? OR isbn1 LIKE ? OR isbn2 LIKE ?",
                  ('%' + search_term.lower() + '%', '%' + search_term + '%', '%' + search_term + '%'))
        books = c.fetchall()
    else:
        c.execute("SELECT * FROM BookCollection")
        books = c.fetchall()

    conn.close()

    if books:
        book_info = ""
        for book in books[:5]:  # Limit to 5 books
            book_info += f"<b>Title: {book[1]}</b><br>"
            book_info += f"Publisher: {book[2]}<br>"
            book_info += f"ISBN: {book[3]}<br>"
            if book[4]:
                book_info += f"ISBN: {book[4]}<br>"
            book_info += f"Link: <a href='{book[5]}'>{book[5]}</a><br><br>"
        return book_info
    else:
        return "No books found in the library database."

def get_events_response():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("SELECT * FROM NewsEventCollection")
    events = c.fetchall()
    conn.close()

    if events:
        event_info = "<b>Here are the upcoming events:</b><br>"
        for event in events[:5]:  # Limit to 5 events
            event_info += f"<b>{event[2]} on {event[1]}</b><br>"
            event_info += f"Link: <a href='{event[3]}'>{event[3]}</a><br>"
        return event_info
    else:
        return "There are no upcoming events at the moment."

def get_locations_response():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("SELECT * FROM LocationCollection")
    locations = c.fetchall()
    conn.close()

    if locations:
        location_info = "<b>Here are the library locations:</b><br>"
        for location in locations:
            location_info += f"<b>{location[1]}</b><br>"
            location_info += f"Link: <a href='{location[2]}'>{location[2]}</a><br>"
        return location_info
    else:
        return "No library locations found in the database."

def get_research_response():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("SELECT * FROM ResearchCollection")
    research_items = c.fetchall()
    conn.close()

    if research_items:
        research_info = "<b>Here are some research resources:</b><br>"
        for item in research_items[:5]:  # Limit to 5 items
            research_info += f"<b>{item[1]}</b><br>"
            research_info += f"Link: <a href='{item[2]}'>{item[2]}</a><br>"
        return research_info
    else:
        return "No research resources found in the database."

def get_ask_response():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("SELECT * FROM AskCollection")
    ask_items = c.fetchall()
    conn.close()

    if ask_items:
        ask_info = "<b>Here are some frequently asked questions:</b><br>"
        for item in ask_items[:5]:  # Limit to 5 items
            ask_info += f"<b>{item[1]}</b><br>"
            ask_info += f"{item[3]}<br><br>"  # Assuming item[2] contains HTML formatted answer
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
    r'books?': get_books_response,
    r'locations?': get_locations_response,
    r'research': get_research_response,
    r'ask?': get_ask_response,
    r'quit|exit': 'Goodbye!'
}

# Define main response handling function

def get_response(user_input):
    user_input = user_input.lower()
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            if callable(response):  # Check if the response is a function
                return response()  # If it is, call the function and return its result
            return response  # Otherwise, return the response string

    # Check if the user input matches a book title
    book_match = re.match(r'^(\w+(\s\w+)*)$', user_input)
    if book_match:
        search_term = book_match.group(1)
        return get_books_response(search_term)
    
    conn.close()
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
    app.run(debug=True)