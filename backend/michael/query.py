import requests as re
from bs4 import BeautifulSoup as BS


def get_url(url:str, data: dict):
    out = url
    for key, item in data.items():
        if type(item) is str:
            item = item.replace(',', '%2C')
        out += f"{key}={item}&"
    return out[:-1]


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
        'orderBy': 'a',
        'dbk': 0,
        'scat': 1,  # only available listings
        'submit': 'Search',
    }
    opt_data = {
        'hb': '',  # has basement
        'wf': '',  # has waterfront
        'hp': '',  # has pool
    }
    for key, value in opt_data.items():
        if len(value) > 0:
            data[key] = value

    r = re.get(url=get_url(url, data))
    soup = BS(r.content, 'html.parser')
    print(soup.prettify())


if __name__=="__main__":
    main("https://www.georgiamls.com/real-estate/search-action.cfm?")