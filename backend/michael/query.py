import pandas as pd
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


def query(url: str, features=None, **kwargs):
    if features:
        col_set = set(features)
        df = pd.DataFrame(columns=features)
    else:
        col_set = ('zip', 'county', 'bed', 'bath', 'sqft', 'lot size', 'year built', 'amenities', 'annual assoc. fee:',
                   'annual taxes', 'schools', 'list price')
        df = pd.DataFrame(columns=['zip', 'county', 'bed', 'bath', 'sqft', 'lot size', 'year built', 'amenities',
                                   'annual taxes', 'annual assoc. fee:', 'schools', 'list price'])
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
    for key, arg in kwargs.values():
        data[key] = arg
    base_info_url = "https://www.georgiamls.com/real-estate/search-detail.cfm?ln="

    u = get_url(url, data)
    r = re.get(url=u)
    soup = BS(r.content, 'html.parser')
    count = soup.find("div", {"class": "listing-pagination-count"}).get_text(strip=True)
    count = int(count[:count.index(" ")])

    i = 1
    while i < count:
        u = u[0:u.rfind("=") + 1] + str(i)
        r = re.get(url=u)
        soup = BS(r.content, 'html.parser')
        listings = soup.find_all("div", {"class": 'listing-gallery'})
        for j, listing in enumerate(listings):
            text = listing.get_text(strip=True).lower()
            mls = regex.search(r'(?<=\s)\d{8}(?=\s*[a-zA-Z])', text).group(0)
            d = parse.parse_property(base_info_url + str(mls))
            filtered_d = {key: value for key, value in d.items() if key in col_set}
            df.loc[j + i - 1] = filtered_d
        i += 12

    return df


if __name__ == "__main__":
    query("https://www.georgiamls.com/real-estate/search-action.cfm?")