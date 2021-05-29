import pandas as pd


def wallet_paytm_analysis(file_directory):
    df = pd.read_csv(file_directory)

    # ---- FORMATTING DATA START
    # Format date and time to datetime object
    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y %H:%M:%S")

    # Fill empty cells with 0
    df["Debit"].fillna(0, inplace=True)
    df["Credit"].fillna(0, inplace=True)

    # Fill empty cells with ""
    df["Comment"].fillna("", inplace=True)
    df["Transaction Breakup"].fillna("", inplace=True)

    # Splitting "Source/Destination" into "Source/Destination Info" and "Source/Destination Order No."
    splitted_df = df["Source/Destination"].str.split(" Order #", n=1, expand=True)
    df.insert(3, "Source/Destination Information", splitted_df[0])
    df.insert(4, "Source/Destination Order No.", splitted_df[1])
    df.drop(columns=["Source/Destination"], inplace=True)
    # ---- FORMATTING DATA END

    print(df.head())

# ACTIVITY TYPES:
# Paid for order
# Added to wallet
# Cashback received
# Money sent
# Money moved across user toll wallet
# Transferred to Bank
# Payment received

# STATUS TYPES:
# SUCCESS

# Comment Types:
# From: Nitin Prakash To: Insha Ali
# From: Insha Ali To: Nitin Prakash
# From: Nitin Prakash To: Aayam Bhardwaj
# From: Nitin Prakash To: pdt.Sunil sharma

# Transaction Breakup Types:
# nan
# Paytm Wallet: 20
# Fastag: 20
# Paytm Wallet: 19.25
# Paytm Wallet: 55.75, Fastag: 19.25
