import os
from requests_html import HTMLSession

def update_keywords():
    with HTMLSession() as s:
        r = s.get('https://raw.githubusercontent.com/dontna/Random-YouTube-Video/main/keywords.txt')

    keywords = r._content

    with open(f"{os.path.dirname(os.path.abspath(__file__))}/keywords.txt", "wb") as f:
        f.write(keywords)

    print("Keywords have been updated!")
