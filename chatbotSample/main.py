import re
import sqlite3
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def get_response(user_input):
    user_input = user_input.lower()
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            if pattern == r'events?':
                c.execute("SELECT * FROM NewsEventCollection")
                events = c.fetchall()
                if events:
                    event_info = "<ul>"
                    event_info = "Here are the upcoming events:\n"
                    for event in events:
                        event_info += f"- {event[2]} on {event[1]}, Link: {event[3]}\n"
                    event_info += "</ul>"
                    response = event_info
                else:
                    response = "There are no upcoming events at the moment."
            elif pattern == r'books?':
                c.execute("SELECT * FROM BookCollection")
                books = c.fetchall()
                if books:
                    book_info = "Here are some books available in the library:\n"
                    for book in books[:5]:  # Limit to 5 books
                        book_info += f"- {book[1]} by {book[2]}, Link: {book[5]}\n"
                    response = book_info
                else:
                    response = "No books found in the library database."
            elif pattern == r'locations?':
                c.execute("SELECT * FROM LocationCollection")
                locations = c.fetchall()
                if locations:
                    location_info = "Here are the library locations:\n"
                    for location in locations:
                        location_info += f"- {location[1]}, Link: {location[2]}\n"
                    response = location_info
                else:
                    response = "No library locations found in the database."
            elif pattern == r'research':
                c.execute("SELECT * FROM ResearchCollection")
                research_items = c.fetchall()
                if research_items:
                    research_info = "Here are some research resources:\n"
                    for item in research_items[:5]:  # Limit to 5 items
                        research_info += f"- {item[1]}, Link: {item[2]}\n"
                    response = research_info
                else:
                    response = "No research resources found in the database."
            return response

    conn.close()
    return "I'm sorry, I didn't understand that."

# Define a dictionary of patterns and responses
responses = {
    r'hi|hello': 'Hello!',
    r'how are you?': 'I\'m doing well, thank you!',
    r'what is your name?': 'My name is UTA Library Chatbot.',
    r'events?': '',
    r'books?': '',
    r'locations?': '',
    r'research': '',
    r'quit|exit': 'Goodbye!'
}

@app.route('/get-response', methods=['POST'])
def handle_request():
    user_input = request.get_json().get('message')
    response = get_response(user_input)
    return jsonify({'response': response})

@app.route('/')
def serve_index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)