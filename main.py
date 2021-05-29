import os
import pandas as pd

from StatementFormats import wallet_paytm

DATA_DIRECTORY = os.getcwd() + "/Data/"


def send_to_analyse_file(file_name, file_directory):
    file_name = file_name.lower()

    # Wallet Statements
    if "wallet" in file_name:
        if "paytm" in file_name:
            wallet_paytm.wallet_paytm_analysis(file_directory)

    # Bank Statements

    # Not aligned to any format


for root, directory, files in os.walk(DATA_DIRECTORY):
    print(root)
    print(directory)
    for file in files:
        print(file)
        send_to_analyse_file(file.title(), root + file)
