import requests
from bs4 import BeautifulSoup

LA_TO_EN_URL = "https://archives.nd.edu/cgi-bin/wordz.pl?keyword="
EN_TO_LA_URL = "https://archives.nd.edu/cgi-bin/wordz.pl?english="

def latin_to_english(query="") -> str:
    page = requests.get(LA_TO_EN_URL + query)
    html = BeautifulSoup(page.content, "html.parser")
    defin = html.find("pre")
    return defin.text

def english_to_latin(query="") -> str:
    page = requests.get(EN_TO_LA_URL + query)
    html = BeautifulSoup(page.content, "html.parser")
    defin = html.find("pre")
    return defin.text