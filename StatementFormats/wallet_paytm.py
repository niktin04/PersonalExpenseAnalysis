import pandas as pd


def wallet_paytm_analysis(file_directory):
    df = pd.read_csv(file_directory)
    print(df)
