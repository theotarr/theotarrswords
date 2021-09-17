import requests
from bs4 import BeautifulSoup
from requests.api import get

def get_forms(query):
    page = requests.get(f"http://latindictionary.wikidot.com/{query}")
    html = BeautifulSoup(page.content, "html.parser")
    html = str(html)
    start = html.find("<table class=\"wiki-content-table\">")
    end = html.find("</table>") + 8
    return html[start:end]
    


if __name__ == "__main__":
    print(get_forms("verb:amare"))