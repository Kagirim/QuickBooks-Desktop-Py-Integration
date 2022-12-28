import pandas as pd

# Read the excel file with pandas
data = pd.read_excel("item_list.xlsx", sheet_name=None)
data = data["Sheet1"]

# split the subcategories
def format_categories(data) -> pd.core.frame.DataFrame:
    """ 
        Receive the whole dataframe as an argument and 
        return a dataframe of individual subcategories as columns
    """

    sub_category_df = data["Item"].str.split(pat=":", expand=True)

    # Create an item list dataframe with all required columns
    return pd.concat([sub_category_df, data["VAT"], data["Cost"], data["Gross Price"]], axis=1)
print(format_categories(data))