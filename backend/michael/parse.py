from bs4 import BeautifulSoup as BS
import requests
import regex as re

req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

def parse_bed_bath(s: str):
    a, b, c = map(int, re.match(r'(\d+)\D+(\d+)\D+(\d+)', s).groups())
    return a, b + 0.5 * c


def parse_property(url: str) -> dict:

    with requests.Session() as s:
        r = s.get(url, headers=req_headers)
        data = {}
        soup = BS(r.content, 'html.parser')
        table = soup.find("table")
        if table:
            for r in table.find_all('tr'):
                row = r.find_all('td')
                i = 0
                while i < len(row) - 1:
                    text = row[i].get_text(strip=True)
                    if text == "Bed/Bath":
                        data["Bed"], data["Bath"] = parse_bed_bath(row[i + 1].get_text(strip=True))
                    elif text == "Address":
                        data["Zip"] = row[i + 1].get_text(strip=True)[-5:]
                    else:
                        data[text] = row[i + 1].get_text(strip=True)
                    i += 1

        return data

def main():
    url = "https://www.georgiamls.com/real-estate/search-detail.cfm?ln=10232084"
    print(parse_property(url))


if __name__=="__main__":
    main()