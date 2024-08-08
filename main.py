import requests
from bs4 import BeautifulSoup

try:
    URL = input("URL: ")
    raw = requests.get(URL)
    readable = ""
    soup = BeautifulSoup(raw.content, "html.parser")
    for element in soup.find_all(["p", "strong", "li", "code", "title", "a", "h1", "h3", "h4", "h5", "h6", "span", "div", "img"], recursive = True):
        if element.name == "img":
            alt = str(element.get("alt"))
            if alt == "None":
                alt = "ALT NOT AVAILABLE"
            readable += "IMAGE [ALT]-> "+alt+"\n"
        else:
            readable += element.text+"\n"
    print("GOT READABLE DATA")
    action = input("[s]ave to file\n[p]rint to the console\n[CleanGet]>> ").lower()
    if action == 'p':
        print(readable)
    elif action == 's':
        path = input("File Path: ")
        with open(path, 'w') as f:
            f.write(readable)
    else:
        print("INCORRECT CHOICE")
except Exception as e:
    print('ERROR:', e)
