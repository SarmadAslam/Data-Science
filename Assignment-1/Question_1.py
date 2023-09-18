# 18-9-23
# CSC461 – Assignment1 – Web Scraping
# Sarmad Aslam
# Fa21-BSE-093
# Create a web scraper in Python to extract the ‘title’ and ‘rating’ for 5 of your
# most favorite movies from the IMDB website

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

movie_urls = [
    'https://www.imdb.com/title/tt0120338/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt0079116/?ref_=nv_sr_srsg_0_tt_6_nm_0_q_Escape%2520from%2520alcetraz',
    'https://www.imdb.com/title/tt0126029/?ref_=nv_sr_srsg_0_tt_7_nm_1_q_Shrek',
    'https://www.imdb.com/title/tt0864835/?ref_=nv_sr_srsg_0_tt_8_nm_0_q_mr%2520pea',
    'https://www.imdb.com/title/tt0099785/?ref_=nv_sr_srsg_0_tt_8_nm_0_q_Home%2520al'
]

titles = []
ratings = []

for url in movie_urls:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)

    time.sleep(1)

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('h1').text.strip()

    script_text = soup.find('script', string=re.compile('aggregateRating'))
    match = re.search(r'"ratingValue": "([\d.]+)"', script_text.string)
    rating = match.group(1) if match else "N/A"

    titles.append(title)
    ratings.append(rating)

movie_data = pd.DataFrame({
    'Title': titles,
    'Rating': ratings
})

movie_data.to_excel('D:\\Python\\Favourite Movies.xlsx', index=False)

print("Data extraction and export completed successfully!")