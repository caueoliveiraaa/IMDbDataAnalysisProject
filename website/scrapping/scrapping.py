import requests
from bs4 import BeautifulSoup


class Scrapper:
    def main():
        url = 'http://www.imdb.com/chart/top'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup 

