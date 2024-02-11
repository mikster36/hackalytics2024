import query
import pandas as pd
import os
import requests
from api import api_key as key
import urllib.parse


def generate_dataset():
    csv_path = os.path.join(os.getcwd(), "data.csv")
    data = pd.DataFrame()  #pd.read_csv(csv_path)
    lpl = 0
    lph = 250000
    increment = 250000
    while lph < 50000000:
        df = pd.DataFrame.from_dict(query.query("https://www.georgiamls.com/real-estate/search-action.cfm?",
                                                lpl=lpl,
                                                lph=lph))
        df = df.rename(columns={'lot size': 'lot_size', 'year built': 'year_built', 'annual taxes': 'annual_taxes',
                                'annual assoc. fee:': 'annual_assoc_fee', 'list price': 'price'})
        if 'annual_assoc_fee' in df.columns:
            df['annual_assoc_fee'] = df['annual_assoc_fee'].fillna(0)
        data = pd.concat([data, df], ignore_index=True)
        data.to_csv(os.path.join(os.getcwd(), "data.csv"))
        lpl += increment
        lph += increment

    data.to_csv(os.path.join(os.getcwd(), "data.csv"))


def address_to_coords(s: str):
    r = requests.get(
        f"https://maps.googleapis.com/maps/api/geocode/json?address={urllib.parse.quote(s, safe='')}&key={key}")
    try:
        o = r.json()['results'][0]['geometry']['location']
        lat, long = o['lat'], o['lng']
        return lat, long
    except Exception:
        return None


def get_data():
    csv_path = os.path.join(os.getcwd(), "data.csv")
    df = pd.read_csv(csv_path)
    df = df.iloc[:, 2:]  # first column is unnamed, second column is address
    df.dropna(subset=['bed', 'bath', 'sqft'], inplace=True)  # listings with bed/bath or sqft missing
    df.drop(columns=["schools", "lot_size"], inplace=True)  # schools = 2 for all, lot_size has little to no impact
    df = df.reset_index(drop=True)

    return df


if __name__ == "__main__":
    get_data()