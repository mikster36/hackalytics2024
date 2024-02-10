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


def get_number(s):
    numerical_parts = []
    for segment in s.split('.'):
        numerical_part = ''.join(filter(str.isdigit, segment))
        if numerical_part:
            numerical_parts.append(numerical_part)

    numerical_string = '.'.join(numerical_parts)

    if '.' in numerical_string:
        return float(numerical_string)
    else:
        return int(numerical_string)


def count_schools(s):
    return len(re.findall(r'[A-Z][a-zA-Z\s]*\s\(', s))


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
                    text = row[i].get_text(strip=True).lower()
                    text_data = row[i + 1].get_text(strip=True)
                    if text == "bed/bath":
                        data["bed"], data["bath"] = parse_bed_bath(text_data)
                    elif text == "address":
                        data["zip"] = text_data[-5:]
                    elif text == "annual taxes:":
                        data["annual taxes"] = get_number(text_data[:-7])
                    elif text == "amenities":
                        data["amenities"] = len(text_data.split(","))
                    elif text == "schools":
                        data["schools"] = count_schools(text_data)
                    else:
                        if any(c.isdigit() for c in text_data):
                            text_data = get_number(text_data)
                        data[text] = text_data
                    i += 1

        return data

def main():
    url = "https://www.georgiamls.com/real-estate/search-detail.cfm?ln=10232084"
    print(parse_property(url))


if __name__=="__main__":
    main()