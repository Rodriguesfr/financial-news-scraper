import requests
from bs4 import BeautifulSoup

# This code fetches the HTML content of the New York Times homepage, parses it using BeautifulSoup, and extracts the title of the page, 
# all article headlines (assuming they are in <h2> tags), and all links on the page.
url = 'https://www.nytimes.com/'

try:
    print(f'Fetching the page: {url}')    
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    print(f'Page fetched successfully!: {response.status_code}')
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extracting the title of the page
    title = soup.title.string if soup.title else 'No title found'
    print(f'Title of the page: {title}')
    # Extracting all the article headlines
    headlines = soup.find_all('h2')
    print(f'Article Headlines (len): {len(headlines)}')
    for i,headline in enumerate(headlines, 1):
        text = headline.get_text(strip=True)
        if text:
            print(f'{i}. {text}')
    #Extracting all the links on the page
    links = soup.find_all('a')
    print(f'\nLinks on the page (len): {len(links)} found:')
    for link in links:
        href = link.get('href')
        if href:
            print(href)  
except requests.exceptions.HTTPError as e:
    print(f'Failed to fetch the page. Error HTTP: {e}')
except requests.exceptions.ConnectionError as e:
    print(f'Failed to fetch the page. Error Connection: {e}')
except requests.exceptions.Timeout as e:
    print(f'Failed to fetch the page. Error Timeout: {e}')
except requests.exceptions.RequestException as e:
    print(f'Failed to fetch the page. Error: {e}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')