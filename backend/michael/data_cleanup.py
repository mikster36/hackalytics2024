import query
import pandas as pd

def main():
    df = pd.DataFrame.from_dict(query.query("https://www.georgiamls.com/real-estate/search-action.cfm?"))
    df = df.rename(columns={'lot size': 'lot_size', 'year built': 'year_built', 'annual taxes': 'annual_taxes',
                            'annual assoc. fee:': 'annual_assoc_fee'})
    df['annual_assoc_fee'] = df['annual_assoc_fee'].fillna(0)
    for i in range(10):
        print(df.loc[i])


if __name__ == "__main__":
    main()