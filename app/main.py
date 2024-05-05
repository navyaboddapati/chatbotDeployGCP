from google.cloud import firestore
# Initialize Firestore client
db = firestore.Client(project="chatbotdeploygcp-419502", database="library-data")

def get_research_links():
    research_ref = db.collection('ResearchCollection')
    research_docs = research_ref.stream()
    research_data = []
    for doc in research_docs:
        research_data.append(doc.to_dict())
    return research_data

def get_location_hours():
    location_ref = db.collection('LocationCollection')
    location_docs = location_ref.stream()
    location_data = []
    for doc in location_docs:
        location_data.append(doc.to_dict())
    return location_data

def main():
    research_data = get_research_links()
    location_data = get_location_hours()

    # Example query: Print out the first 5 research links
    print("Research Links:")
    for i in range(5):
        print(research_data[i]['text'], research_data[i]['link'])

    # Example query: Print out the location hours
    print("\nLocation Hours:")
    for location in location_data:
        print(location['library'], location['link'])

if __name__ == "__main__":
    main()
