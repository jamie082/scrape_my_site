#!/usr/bin/python3
from bs4 import BeautifulSoup
import pandas as pd
import requests

# check for 200 status of web page

def check_http_status():
    response = requests.get("http://bindfix.net/site/temp_site/frame_good.html")

    print("\nStatus of HTML Document")
    if response.status_code == 200:
        # if the request is successful return the HTML content
        print("> accessed document fine\n\n")
    else:
        raise Exception("an error occured while fetching html")

#check_http_status()
def start_program():
    response = requests.get("http://bindfix.net/site/temp_site/frame_good.html")
    webpage = response.content
    soup = BeautifulSoup(webpage, "html.parser")

    for counter in soup.find_all('section', class_='column'):
        class_counter = [a for a in counter.find_all('h1')]
        for n, tag in enumerate(counter.find_all('div', class_='body_element')):
            p_element = [x for x in tag.find_all('p')] # paragraph element
            print("Class Section: ", class_counter[n].text.strip())
            print("Paragraph Section: ", p_element[0].text.strip())
            print()

check_http_status()
start_program()