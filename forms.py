import requests
from bs4 import BeautifulSoup

def get_forms(query):
    page = requests.get(f"http://latindictionary.wikidot.com/{query}")
    html = BeautifulSoup(page.content, "html.parser")

    parsed_html = ""
    page_content = html.find_all("div", {"id": "page-content"})

    for tag in page_content:
        p_tags = tag.find_all("p")
        for tag in p_tags:
            if tag == p_tags[-3]:
                break
            parsed_html += str(tag)

    table = html.find_all("table", {"class": "wiki-content-table"})
    for tag in table:
        parsed_html += str(tag)

    return parsed_html