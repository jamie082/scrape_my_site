#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests

#http://blog.fixnter.com/python-beautifulsoup-examples
#http://blog.logrocket.com/build-python-webscraper-beautiful-soup/
# Verifying tables and their classes

# check for 200 status of web page

def check_http_status():
    response = requests.get("http://bindfix.net/site/temp_site/frame_good.html")
    webpage = response.content
    soup = BeautifulSoup(webpage, "html.parser")
    if response.status_code == 200:
        # if the request is successful return the HTML content
        return response.text
    else:
        raise Exception("an error occured while fetching html")

response = requests.get("http://bindfix.net/site/temp_site/frame_good.html")
webpage = response.content
soup = BeautifulSoup(webpage, "html.parser")

for counter in soup.find_all('section', class_='column'):
    class_counter = [a for a in counter.find_all('h1')]
    for n, tag in enumerate(counter.find_all('div', class_='body_element')):
        p_element = [x for x in tag.find_all('p', class_='body_element')] # paragraph element
        print("Paragraph #1", class_counter[n].text.strip())
        #print("Class Section", p_element[3].text.strip())
        print()
