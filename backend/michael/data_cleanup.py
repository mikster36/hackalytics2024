import query
import pandas as pd
import os

def generate_dataset():
    csv_path = os.path.join(os.getcwd(), "data.csv")
    data = pd.read_csv(csv_path)
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

    data.to_csv(os.path.join(os.getcwd(), "data1.csv"))


def cleanup():
    csv_path = os.path.join(os.getcwd(), "data.csv")
    df = pd.read_csv(csv_path)
    df = df.iloc[:, 2:]  # drop whatever weird stuff was going on in the first two columns
    df.dropna(subset=['bed', 'bath', 'sqft'], inplace=True)  # listings with bed/bath or sqft missing
    df.drop(columns=['schools'], inplace=True)  # it's 2 for all listings so this isn't important
    df = df.reset_index(drop=True)
    df.to_csv(os.path.join(os.getcwd(), "data1.csv"))
    return df

if __name__ == "__main__":
    main()