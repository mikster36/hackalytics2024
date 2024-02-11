import pandas as pd
import os

def get_data():
    csv_path = os.path.join(os.getcwd(), "data.csv")
    df = pd.read_csv(csv_path)
    df = df.iloc[:, 1:]  # first column is unnamed, second column is address
    df.dropna(subset=['bed', 'bath', 'sqft'], inplace=True)  # listings with bed/bath or sqft missing
    df.drop(columns=["schools", "lot_size"], inplace=True)  # schools = 2 for all, lot_size has little to no impact
    df = df.reset_index(drop=True)

    return df

df = get_data()
print(df)