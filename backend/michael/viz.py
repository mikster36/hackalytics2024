import seaborn as sns
import matplotlib.pyplot as plt
import data_cleanup
import pandas as pd


def main():
    sns.set_theme(style='ticks')
    df = data_cleanup.get_data()
    print(df)
    sns.pairplot(df, hue='county')
    plt.show()


if __name__ == "__main__":
    main()