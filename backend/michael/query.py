import requests as re
from bs4 import BeautifulSoup as BS
import regex
import parse


def get_url(url:str, data: dict):
    out = url
    for key, item in data.items():
        if type(item) is str:
            item = item.replace(',', '%2C')
        if type(item) is list:
            for i in item:
                out += f"{key}={i}&"
            continue
        out += f"{key}={item}&"
    return out + "start=1"


def main(url: str):
    data = {
        'gtyp': 'loc',
        'styp': 'sale',
        'sid': 0,
        'city': 'Atlanta',
        'cnty': 'Fulton',
        'zip': '',
        'subd': '',
        'sch': '',
        'br': 0,  # any count
        'baf': 0,  # any count
        'lpl': '10,000',
        'lph': '1,000,000',
        'sqftl': 10,
        'sqfth': 1000,
        'acresL': 0,
        'arcesH': 10,
        'ybl': 1990,
        'ybh': 2024,
        'typ': ['sd', 'sa', 'mf'],
        'orderBy': 'a',
        'dbk': 0,
        'scat': 1,  # only available listings
        'submit': 'Search',
    }
    opt_data = {
        'hb': 0,  # has basement
        'wf': 0,  # has waterfront
        'hp': 0,  # has pool
    }
    for key, value in opt_data.items():
        if value == 1:
            data[key] = value

    base_info_url = "https://www.georgiamls.com/real-estate/search-detail.cfm?ln="

    u = get_url(url, data)
    r = re.get(url=u)
    soup = BS(r.content, 'html.parser')
    count = soup.find("div", {"class": "listing-pagination-count"}).get_text(strip=True)
    count = int(count[:count.index(" ")])
    all = list()

    i = 1
    while i < 12:
        u = u[0:u.rfind("=") + 1] + str(i)
        r = re.get(url=u)
        soup = BS(r.content, 'html.parser')
        listings = soup.find_all("div", {"class": 'listing-gallery'})
        for listing in listings:
            text = listing.get_text(strip=True)
            mls = regex.search(r'(?<=\s)\d{8}(?=\s*[a-zA-Z])', text).group(0)
            d = parse.parse_property(base_info_url + str(mls))
            all.append(d)
        i += 12

    print(all[0])

if __name__=="__main__":
    main("https://www.georgiamls.com/real-estate/search-action.cfm?")