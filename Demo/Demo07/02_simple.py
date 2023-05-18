import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status() # throw HTTPError if not 200
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "HTTPError"


if __name__ == "__main__":
    url = "www.google.com"
    print(getHTMLText(url))