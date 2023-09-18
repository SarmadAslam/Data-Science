# 18-9-23
# CSC461 – Assignment1 – Web Scraping
# Sarmad Aslam
# Fa21-BSE-093

""" Write a web scraper in Python (preferably a Jupyter Notebook) to extract the below mentioned
information.
1. From the ‘timeanddate’ website, find out who you share your birthdate with?
2. From the ‘britannica’ website, find out which important event(s) happened on your birthdate? """

import requests
from bs4 import BeautifulSoup

birthdate = "2000-09-18"

timeanddate_url = f"https://www.timeanddate.com/on-this-day/{birthdate}"
britannica_url = f"https://www.britannica.com/on-this-day/{birthdate}"

def scrape_timeanddate(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    shared_birthdate_info = ""

    shared_birthdate_element = soup.find("section", class_="otd-main-section")
    if shared_birthdate_element:
        shared_birthdate_info = shared_birthdate_element.text.strip()

    return shared_birthdate_info

def scrape_britannica(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    event_list = []

    events = soup.find_all("p", class_="m-article-card__description")

    for event in events:
        event_text = event.text.strip()
        event_list.append(event_text)

    return event_list

timeanddate_data = scrape_timeanddate(timeanddate_url)
britannica_data = scrape_britannica(britannica_url)

with open("birth_info.txt", "w", encoding="utf-8") as file:
    file.write("Shared Birthdate:\n")
    if timeanddate_data:
        file.write(timeanddate_data)
    else:
        file.write("No shared birthdate information found.")
    file.write("\n\n")

    file.write("Important Events:\n")
    if britannica_data:
        for event in britannica_data:
            file.write(f"- {event}\n")
    else:
        file.write("No important events found.")

print("Data scraped and saved to birth_info.txt")
