import requests
from bs4 import BeautifulSoup
from data_store import (
    store_research_data,
    store_location_data,
    store_book_data,
    store_news_event_data,
    store_ask_data
)

def scrape_data():
    url = 'https://libraries.uta.edu'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'}

    # Scrape research data
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', {'class': 'nav-link'})
        research_link = url + links[0].get('href')
        research_response = requests.get(research_link, headers=header)
        if research_response.status_code == 200:
            research_soup = BeautifulSoup(research_response.content, 'html.parser')
            research_soup_links = research_soup.find_all('a', {'class': 'stretched-link'})
            research_data = []
            for link in research_soup_links[:6]:
                research = link.get('href')
                if research[0] != 'h':
                    research = url + research
                research_data.append({
                    'text': link.text,
                    'link': research
                })
        else:
            print(f'Error {research_response.status_code} while accessing the website.')
    else:
        print(f'Error {response.status_code} while accessing the website.')

    # Scrape location data
    location_link = url + links[3].get('href')
    location_response = requests.get(location_link, headers=header)
    if location_response.status_code == 200:
        location_soup = BeautifulSoup(location_response.content, 'html.parser')
        location_soup_links = location_soup.find_all('a', {'class': 'stretched-link'})
        location_data = []
        for link in location_soup_links[:3]:
            location_hours = url + link.get('href')
            location_data.append({
                'library': link.text,
                'link': location_hours
            })
    else:
        print(f'Error {location_response.status_code} while accessing the website.')

    # Insert book data
    book_data = [
        {
            "Title": "2024 16th International Conference on Knowledge and Smart Technology (KST)",
            "Publisher": "IEEE",
            "Identifier1": "ISBN : 9798350370737",
            "Identifier2": "ISBN : 9798350370737",
            "Link": "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51246481050004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "2024 Second International Conference on Emerging Trends in Information Technology and Engineering (ICETITE)",
            "Publisher" : "IEEE",
            "Identifier1" : "ISBN : 9798350328202",
            "Identifier2" : "ISBN : 9798350328219",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51246480390004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "2024 International Conference on Computer, Electrical & Communication Engineering (ICCECE)",
            "Publisher" : "IEEE",
            "Identifier1" : "ISBN : 9798350386479",
            "Identifier2" : "ISBN : 9798350386486",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51246481080004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "2023 5th International Workshop on Artificial Intelligence and Education (WAIE)",
            "Publisher" : " IEEE Computer Society",
            "Identifier1" : "ISBN : 9798350307061",
            "Identifier2" : "ISBN : 9798350307078",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51246480840004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "2023 Global Reliability and Prognostics and Health Management Conference (PHM-Hangzhou)",
            "Publisher" : "IEEE",
            "Identifier1" : "ISBN : 9798350301359",
            "Identifier2" : "ISBN : 9798350301366",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51246480900004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "2024 10th International Conference on Artificial Intelligence and Robotics (QICAR)",
            "Publisher" : "IEEE",
            "Identifier1" : "ISBN : 9798350348873",
            "Identifier2" : "ISBN : 9798350348880",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51246481140004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "2023 International Conference on Artificial Intelligence and Automation Control (AIAC)",
            "Publisher" : "IEEE Computer Society",
            "Identifier1" : "ISBN : 9798350383805",
            "Identifier2" : "ISBN : 9798350383812",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51246480630004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "2024 IEEE 4th International Conference in Power Engineering Applications (ICPEA)",
            "Publisher" : "IEEE",
            "Identifier1" : "ISBN : 9798350344578",
            "Identifier2" : "ISBN : 9798350318142",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51246480720004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "2024 7th International Conference on Development in Renewable Energy Technology (ICDRET)",
            "Publisher" : "IEEE",
            "Identifier1" : "ISBN : 9798350373394",
            "Identifier2" : "ISBN : 9798350373400",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51246480480004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "2023 7th International Conference on Electrical, Mechanical and Computer Engineering (ICEMCE)",
            "Publisher" : "IEEE",
            "Identifier1" : "ISBN : 9798350382877",
            "Identifier2" : "ISBN : 9798350382884",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51246480660004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "The age of magical overthinking : notes on modern irrationality ",
            "Publisher" : "New York : One Signal Publishers/Atria",
            "Identifier1" : "ISBN : 9781668007976",
            "Identifier2" : "ISBN : 1668007975",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D21246548510004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&Force_direct=false"
        },
        {
            "Title" : "General relativity : the theoretical minimum",
            "Publisher" : "New York, NY : Basic Books",
            "Identifier1" : "ISBN : 9781541601772",
            "Identifier2" : "ISBN : 1541601777",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D21246440910004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&rft.series=The%20theoretical%20minimum&Force_direct=false"
        },
        {
            "Title" : "Neuroexistentialism : meaning, morals, and purpose in the age of neuroscience ",
            "Publisher" : "New York, NY, United States of America : Oxford University Press",
            "Identifier1" : "ISBN : 9780190460723",
            "Identifier2" : "ISBN : 0190460725",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D21246440780004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&Force_direct=false"
        },
        {
            "Title" : "Marathon - 2,500 Years : Proceedings of The Marathon Conference 2010 ",
            "Publisher" : "London, England : University of London Press",
            "Identifier1" : "ISBN : 1-905670-52-4",
            "Identifier2" : "ISBN : 1-905670-81-8",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51246533120004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "Small States in EU Policy-Making : Strategies, Challenges, Opportunities",
            "Publisher" : "Routledge",
            "Identifier1" : "ISBN : 9781003380641",
            "Identifier2" : "ISBN : 9781032462233",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51246533020004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "A New Approach to Wind Energy",
            "Publisher" : "Stanford Woods Institute for the Environment",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51246533150004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "Innovations in Journalism : Comparative Research in Five European Countries",
            "Publisher" : "Routledge",
            "Identifier1" : "ISBN : 9781032630410",
            "Identifier2" : "ISBN : 9781032630397",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51246533070004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "How Migrants Choose Their Destinations : Factors Influencing Post-EU Accession Choices and Decisions to Remain",
            "Publisher" : "Routledge",
            "Identifier1" : "ISBN : 9781003382720",
            "Identifier2" : "ISBN : 9781032466620",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51246532940004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "IGF-WIMOWA WORKSHOP: GENDER AND MINING GOVERNANCE: ENHANCING WOMEN’S VOICES AND PARTICIPATION IN WEST AFRICA",
            "Other Title" : "IGF-WIMOWA WORKSHOP",
            "Publisher" : "International Institute for Sustainable Development IISD",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51246533210004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "Cripping Girlhood",
            "Publisher" : "University of Michigan Press",
            "Identifier1" : "ISBN : 9780472904426",
            "Identifier2" : "ISBN : 9780472076741",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51246532880004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "Cloud Computing - CLOUD 2023 : 16th International Conference, Held As Part of the Services Conference Federation, SCF 2023, Shenzhen, China, December 17-18, 2023, Proceedings ",
            "Publisher" : "Cham, Switzerland : Springer",
            "Identifier1" : "ISBN : 3-031-51709-1",
            "Identifier2" : "ISBN : 9783031517082",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51244421810004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&rft.series=Lecture%20Notes%20in%20Computer%20Science%20Series"
        },
        {
            "Title" : "Cloud computing - CLOUD 2022 : 15th international conference, held as part of the Services Conference Federation, SCF 2022, Honolulu, Hi, USA, December 10-14 2022, proceedings",
            "Publisher" : "Cham, Switzerland : Springer",
            "Identifier1" : "ISBN : 3-031-23498-7",
            "Identifier2" : "ISBN : 9783031234972",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51219478940004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&rft.series=Lecture%20Notes%20in%20Computer%20Science"
        },
        {
            "Title" : "Cloud computing : principles and paradigms",
            "Publisher" : "Hoboken, N.J. : Wiley",
            "Identifier1" : "ISBN : 9780470887998 (hardback)",
            "Identifier2" : "ISBN : 0470887990 (hardback)",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D2197603400004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&Force_direct=false"
        },
        {
            "Title" : "Cloud computing - CLOUD 2021 : 14th international conference, held as part of the Services Conference Federation, SCF 2021, virtual event, December 10-14, 2021, proceedings",
            "Publisher" : "Cham, Switzerland : Springer",
            "Identifier1" : "ISBN : 3-030-96326-8",
            "Identifier2" : "ISBN : 9783030963255",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51193951270004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&rft.series=Lecture%20Notes%20in%20Computer%20Science"
        },
        {
            "Title" : "Essentials of Cloud Computing A Holistic, Cloud-Native Perspective",
            "Publisher" : "Cham : Springer International Publishing : Imprint: Springer",
            "Identifier1" : "ISBN : 3-031-32044-1",
            "Identifier2" : "ISBN : 9783031320439",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51239810420004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&rft.series=Texts%20in%20Computer%20Science"
        },
        {
            "Title" : "Cloud computing -- CLOUD 2020 : 13th International Conference, held as part of the Services Conference Federation, SCF 2020, Honolulu, HI, USA, September 18-20, 2020, proceedings",
            "Publisher" : "Cham, Switzerland : Springer",
            "Identifier1" : "ISBN : 3-030-59635-4",
            "Identifier2" : "ISBN : 3-030-59634-6",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51178291340004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&rft.series=Information%20Systems%20and%20Applications,%20incl.%20Internet%2FWeb,%20and%20HCI"
        },
        {
            "Title" : "Cloud computing : theory and practice",
            "Publisher" : "Boston : Morgan Kaufmann",
            "Identifier1" : "ISBN : 978-0-12-404627-6",
            "Identifier2" : "ISBN : 0-12-404641-X",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51186173280004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&rft.series=Gale%20eBooks"
        },
        {
            "Title" :  "White Paper - Cybersecurity in Agile Cloud Computing - Cybersecurity Guidelines for Cloud Access",
            "Publisher" : "New York : IEEE",
            "Identifier1" : "ISBN : 1-5044-8996-9",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51214942020004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "Cloud Computing and Services Sciences International Conference in Cloud Computing and Services Sciences, CLOSER 2014 Barcelona Spain, April 3–5, 2014 Revised Selected Papers",
            "Publisher" : "Cham : Springer International Publishing : Imprint: Springer",
            "Identifier1" : "ISBN : 3-319-25414-6",
            "Identifier2" : "ISBN : 3-319-25413-8",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51178712010004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&rft.series=Communications%20in%20Computer%20and%20Information%20Science"
        },
        {
            "Title" : "Service-Oriented and Cloud Computing 8th IFIP WG 2.14 European Conference, ESOCC 2020, Heraklion, Crete, Greece, September 28–30, 2020, Proceedings",
            "Publisher" : "Cham : Springer International Publishing : Imprint: Springer",
            "Identifier1" : "ISBN : 3-030-44769-3",
            "Identifier2" : "ISBN : 3-030-44768-5",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51178769120004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&rft.series=Programming%20and%20Software%20Engineering"
        },
        {
            "Title" : "Cloud Computing with AWS Everything You Need to Know to be an AWS Cloud Practitioner",
            "Publisher" : "Berkeley, CA : Apress : Imprint: Apress",
            "Identifier1" : "ISBN : 9781484291726",
            "Identifier2" : "ISBN : 9781484291719",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51237150870004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "Cloud computing : principles, systems and applications",
            "Publisher" : "London : Springer",
            "Identifier1" : "ISBN : 9781849962407 (hbk.)",
            "Identifier2" : "ISBN : 1849962413 (ebk.)",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D2197864180004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&rft.series=Computer%20communications%20and%20networks&Force_direct=false"
        },
        {
            "Title" : "Cloud computing : 10th EAI International Conference, CloudComp 2020, Qufu, China, December 11-12, 2020 : proceedings",
            "Publisher" : "Cham, Switzerland : Springer",
            "Identifier1" : "ISBN : 3-030-69992-7",
            "Identifier2" : "ISBN : 3-030-69991-9",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51182430900004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&rft.series=Lecture%20Notes%20of%20the%20Institute%20for%20Computer%20Sciences,%20Social%20Informatics,%20and%20Telecommunications%20Engineering"
        },
        {
            "Title" : "Python Debugging for AI, Machine Learning, and Cloud Computing A Pattern-Oriented Approach",
            "Publisher" : "Berkeley, CA : Apress : Imprint: Apress",
            "Identifier1" : "ISBN : 1-4842-9745-8",
            "Identifier2" : "ISBN : 1-4842-9744-X",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51244390030004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "Cloud computing : methodology, systems, and applications",
            "Publisher" : "Boca Raton, FL : CRC Press",
            "Identifier1" : "ISBN : 9781439856413 (hardcover : alk. paper)",
            "Identifier2" : "ISBN : 1439856419 (hardcover : alk. paper)",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D2197680520004911,ie%3D51175788320004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "Cloud computing with security and scalability : concepts and practices",
            "Publisher" : "Cham, Switzerland : Springer Nature Switzerland AG",
            "Identifier1" : "ISBN : 3-031-07242-1",
            "Identifier2" : "ISBN : 9783031072413",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51222456230004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "Cloud computing : methodology, systems, and applications",
            "Publisher" : "Boca Raton, FL : CRC Press",
            "Identifier1" : "ISBN : 9781439856413 (hardcover : alk. paper)",
            "Identifier2" : "ISBN : 1439856419 (hardcover : alk. paper)",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D2197680520004911,ie%3D51175788320004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "Cloud computing with security and scalability : concepts and practices",
            "Publisher" : "Cham, Switzerland : Springer Nature Switzerland AG",
            "Identifier1" : "ISBN : 3-031-07242-1",
            "Identifier2" : "ISBN : 9783031072413",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51222456230004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "Green, Pervasive, and Cloud Computing 18th International Conference, GPC 2023, Harbin, China, September 22–24, 2023, Proceedings; Part II",
            "Publisher" : "Singapore : Springer Nature Singapore : Imprint: Springer",
            "Identifier1" : "ISBN : 981-9998-96-4",
            "Identifier2" : "ISBN : 9789819998951",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51245209190004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&rft.series=Lecture%20Notes%20in%20Computer%20Science"
        },
        {
            "Title" : "Green, Pervasive, and Cloud Computing 18th International Conference, GPC 2023, Harbin, China, September 22–24, 2023, Proceedings, Part I",
            "Publisher" : "Singapore : Springer Nature Singapore : Imprint: Springer",
            "Identifier1" : "ISBN : 981-9998-93-X",
            "Identifier2" : "ISBN : 9789819998920",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51245209230004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&rft.series=Lecture%20Notes%20in%20Computer%20Science"
        },
        {
            "Title" : "Big Data and Cloud Computing Select Proceedings of ICBCC 2022",
            "Publisher" : "Singapore : Springer Nature Singapore : Imprint: Springer",
            "Identifier1" : "ISBN : 981-9910-51-X",
            "Identifier2" : "ISBN : 9789819910502",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51239129600004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&rft.series=Lecture%20Notes%20in%20Electrical%20Engineering"
        },
        {
            "Title" : "Big data, cloud computing and IoT : tools and applications",
            "Publisher" : "Boca Raton, FL : CRC Press, Taylor & Francis Group, LLC",
            "Identifier1" : "ISBN : 1-00-329833-8",
            "Identifier2" : "ISBN : 1-003-29833-8",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51221774270004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "Cloud Computing, Big Data & Emerging Topics 11th Conference, JCC-BD&ET 2023, La Plata, Argentina, June 27–29, 2023, Proceedings",
            "Publisher" : "Cham : Springer Nature Switzerland : Imprint: Springer",
            "Identifier1" : "ISBN : 3-031-40942-6",
            "Identifier2" : "ISBN : 9783031409417",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51240602250004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&rft.series=Communications%20in%20Computer%20and%20Information%20Science"
        },
        {
            "Title" : "Service-Oriented and Cloud Computing 5th IFIP WG 2.14 European Conference, ESOCC 2016, Vienna, Austria, September 5-7, 2016, Proceedings",
            "Publisher" : "Cham : Springer International Publishing : Imprint: Springer",
            "Identifier1" : "ISBN : 3-319-44482-4",
            "Identifier2" : "ISBN : 3-319-44481-6",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51179063990004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&rft.series=Programming%20and%20Software%20Engineering"
        },
        {
            "Title" : "Cloud computing, big data and emerging topics : 10th conference, JCC-BD&ET 2022, La Plata, Argentina, June 28-30, 2022, proceedings",
            "Publisher" : "Cham, Switzerland : Springer",
            "Identifier1" : "ISBN : 3-031-14599-2",
            "Identifier2" : "ISBN : 9783031145988",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51206556020004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&rft.series=Communications%20in%20computer%20and%20information%20science"
        },
        {
            "Title" : "Cloud-computing : data-intensive computing and scheduling",
            "Publisher" : "Boca Raton : CRC Press",
            "Identifier1" : "ISBN : 0-429-11257-2",
            "Identifier2" : "ISBN : 1-4665-0783-7",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51173931810004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&rft.series=Chapman%20%26%20Hall%2FCRC%20Numerical%20Analysis%20%26%20Scientific%20Computing%20Series"
        },
        {
            "Title" : "Security and Risk Analysis for Intelligent Cloud Computing: Methods, Applications, and Preventions",
            "Publisher" : "CRC Press Unlimited",
            "Identifier1" : "ISBN : 1-003-32994-2",
            "Identifier2" : "ISBN : 9781032360300",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51242861170004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "Hybridization of blockchain and cloud computing : overcoming security issues in IOT",
            "Publisher" : "Palm Bay, FL : Apple Academic Press",
            "Identifier1" : "ISBN : 1-00-333662-0",
            "Identifier2" : "ISBN : 1-000-77972-6",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51240420860004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "Fintech Fundamentals : Big Data / Cloud Computing / Digital Economy.",
            "Publisher" : "Bloomfield : Mercury Learning & Information",
            "Identifier1" : "ISBN : 9781683928379",
            "Identifier2" : "ISBN : 9781683928386",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51240137000004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services"
        },
        {
            "Title" : "Algorithmic Aspects of Cloud Computing 7th International Symposium, ALGOCLOUD 2022, Potsdam, Germany, September 6, 2022, Revised Selected Papers",
            "Publisher" : "Cham : Springer International Publishing : Imprint: Springer",
            "Identifier1" : "ISBN : 3-031-33437-X",
            "Identifier2" : "ISBN : 9783031334368",
            "Link" : "https://uta.alma.exlibrisgroup.com/discovery/openurl?institution=01UTAR_INST&rfr_id=info:sid%2Fsummon&rft_dat=ie%3D51237131330004911,language%3DEN&svc_dat=CTO&u.ignore_date_coverage=true&vid=01UTAR_INST:Services&rft.series=Lecture%20Notes%20in%20Computer%20Science"
        }
    ]

    # Scrape news and events data
    news_link = "https://libraries.uta.edu/news-events/news"
    news_response = requests.get(news_link, headers=header)
    if news_response.status_code == 200:
        news_soup = BeautifulSoup(news_response.content, 'html.parser')
        news_events = news_soup.find_all('div', {'class': 'card-body'})
        news_event_data = []
        for event in news_events:
            news_time = event.find('p', {'class': 'eyebrow'}).text.strip()
            news_title = event.find('a', {'class': 'stretched-link'}).text.strip()
            news_link = event.find('a', {'class': 'stretched-link'})['href']
            news_event_data.append({
                'date': news_time,
                'title': news_title,
                'link': news_link
            })
    else:
        print(f'Error {news_response.status_code} while accessing the website.')

    # Scrape question and answer data
    uta_ask = "https://ask.uta.edu/"
    ask_response = requests.get(uta_ask, headers=header)
    if ask_response.status_code == 200:
        ask_soup = BeautifulSoup(ask_response.content, 'html.parser')
        ask_popular = ask_soup.find_all('div', {'class': 's-la-faq-listing-q'})
        ask_data = []
        for iterate in ask_popular:
            ask_title = iterate.find('a').text.strip()
            ask_link = iterate.find('a')['href']
            answer_response = requests.get(ask_link, headers=header)
            if answer_response.status_code == 200:
                answer_soup = BeautifulSoup(answer_response.content, 'html.parser')
                answer_div = answer_soup.find_all('div', {'class': 's-la-faq-answer'})
                answer_html = "<html><body>"
                for div in answer_div:
                    answer_html += str(div)
                answer_html += "</body></html>"
                ask_data.append({
                    'question': ask_title,
                    'link': ask_link,
                    'answer': answer_html
                })
            else:
                print(f'Error {answer_response.status_code} while accessing the website.')
    else:
        print(f'Error {ask_response.status_code} while accessing the website.')

    # Store the scraped data in Firestore
    store_research_data(research_data)
    store_location_data(location_data)
    store_book_data(book_data)
    store_news_event_data(news_event_data)
    store_ask_data(ask_data)

if __name__ == '__main__':
    scrape_data()