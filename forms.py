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
            parsed_html += str(tag)
            if "declension" in str(tag).lower() and "noun" in query:
                break
            elif "main forms" in str(tag).lower() and ("verb" in query or "adjective" in query):
                break
            elif "gender" in str(tag).lower() and "pronoun" in query:
                break
            
            

    table = html.find_all("table", {"class": "wiki-content-table"})
    for tag in table:
        parsed_html += str(tag)

    return parsed_html