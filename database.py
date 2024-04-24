import requests
from bs4 import BeautifulSoup
from google.cloud import firestore
# Initialize Firebstore client
db = firestore.Client(project="chatbotdeployGCP", database="library-data")
query = 'cloud computing bible'
# URL of the website to scrape
url = 'https://libraries.uta.edu'
#searchUrl = f'{url}/search?search_field=title&search_param=contains&Bquery={query}'
Header = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'})
# Send a GET request to search URL
response = requests.get(searchUrl,Header)
# Check if the GET request was successful
if response.status_code == 200:
    #Parse the HTML content of the search results page
    soup = BeautifulSoup(response.content, 'html.parser')
    #Extract the links to the book's details page
    bookLinks = soup.find_all('a',{'class':'small text-white'})
    for link in bookLinks:
        print(link)
else:
    print(f'Error {response.status_code} while accessing the search results page.')
# Send a GET request to the URL
response = requests.get(url,Header)
# Check if the GET request was successful
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')
    div = soup.find_all('div',{'id':'api_hours_today_iid5263_lid0'})
    links = soup.find_all('a',{'class':'nav-link'})
    researchLink = url + links[0].get('href')
    researchResponse = requests.get(researchLink,Header)
    if researchResponse.status_code == 200:
        researchSoup = BeautifulSoup(researchResponse.content, 'html.parser')
        researchSoupLinks = researchSoup.find_all('a',{'class':'stretched-link'})
        researchData = {}
        for iterate in range(6):
            research = researchSoupLinks[iterate].get('href')
            if research[0] != 'h':
                research = url + research
            researchData = { 
                'text' : researchSoupLinks[iterate].text, 
                'link' : research
            }
            print(researchData)
        #Creating collection for researchData
        research_ref = db.collection('ResearchCollection').add(researchData)
    locationLink = url + links[3].get('href')
    locationResponse = requests.get(locationLink,Header)
    if locationResponse.status_code == 200:
        locationSoup = BeautifulSoup(locationResponse.content, 'html.parser')
        locationSoupLinks = locationSoup.find_all('a',{'class':'stretched-link'})
        for iterate in range(3):
            locationHours = url + locationSoupLinks[iterate].get('href')
            locResponse = requests.get(locationHours,Header)
            print(locationSoupLinks[iterate].text + " = " + locationHours)
            locationData = { 
                'library' : locationSoupLinks[iterate].text, 
                'link': locationHours
            }
        print(locationData)
        #Creating collection for researchData
        location_ref = db.collection("LocationCollection").add(locationData)
        if locResponse.status_code == 200:
                locSoup = BeautifulSoup(locResponse.content, 'html.parser')
                monthSoup = locSoup.find_all('div',{'id':'s-lc-mhw-m13-661042b62d3cd'})
                for iterate in monthSoup:
                    print(iterate)
        scriptH = locationSoup.find_all('script',{'src':'https://uta.libcal.com/js/hours_month.js?002'})
        for iterate in range(3):
            print(scriptH[iterate].text)
        else:
            print(f'Error {response.status_code} while accessing the website.')
    else:
        print(f'Error {response.status_code} while accessing the website.')
else:
    print(f'Error {response.status_code} while accessing the website.')