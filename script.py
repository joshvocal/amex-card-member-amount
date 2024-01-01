import argparse
import pandas as pd


def process_excel(filename):
    amex_df = pd.read_excel(filename, index_col=None)
    amex_df["Amount"] = amex_df["Amount"].str.replace(",", "", regex=False)
    amex_df["Amount"] = (
        amex_df["Amount"].str.replace("$", "", regex=False).astype(float)
    )
    result = amex_df.groupby(["Cardmember"])["Amount"].sum()
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Determines the balance for each cardholder."
    )
    parser.add_argument(
        "filename", help="Amex statement balance. Takes in a .xlsx file."
    )
    args = parser.parse_args()

    filename = args.filename
    result = process_excel(filename)
    print(result)
