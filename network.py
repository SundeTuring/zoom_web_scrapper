from bs4 import BeautifulSoup
import requests


class Networker:
    @staticmethod
    def get_data(url):
        response = requests.get(url)
        response.raise_for_status()
        data = response.text

        soup = BeautifulSoup(data, "html.parser")
        return soup
