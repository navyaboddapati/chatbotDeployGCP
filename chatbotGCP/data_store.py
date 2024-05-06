from firestore_service import create_document

def store_research_data(research_data):
    for data in research_data:
        create_document('ResearchCollection', {
            'text': data['text'],
            'link': data['link']
        })

def store_location_data(location_data):
    for data in location_data:
        create_document('LocationCollection', {
            'library': data['library'],
            'link': data['link']
        })

def store_book_data(book_data):
    for data in book_data:
        create_document('BookCollection', {
            'title': data['Title'],
            'publisher': data['Publisher'],
            'identifier1': data.get('Identifier1', ''),
            'identifier2': data.get('Identifier2', ''),
            'link': data['Link']
        })

def store_news_event_data(news_event_data):
    for data in news_event_data:
        create_document('NewsEventCollection', {
            'date': data['date'],
            'title': data['title'],
            'link': data['link']
        })

def store_ask_data(ask_data):
    for data in ask_data:
        create_document('AskCollection', {
            'question': data['question'],
            'link': data['link'],
            'answer': data['answer']
        })