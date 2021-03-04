from bs4 import BeautifulSoup
import requests

URL = 'https://www.timeout.com/newyork/movies/best-movies-of-all-time'

response = requests.get(url=URL)
response.raise_for_status()
movies_data = response.text

soup = BeautifulSoup(movies_data, 'html.parser')

titles = soup.find_all(name='h3', class_='card-title')
title_text = [title.getText().strip().replace('\xa0', ' ') for title in titles]

with open('great_movies', 'w') as file:
    for title in title_text:
        file.write(f'{title}\n')

print(title_text)