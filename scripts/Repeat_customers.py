import pandas as pd
import numpy as np

from db.connections import get_db_engine_pos
from db.common_helpers import get_data
from db.queries import REPEAT_CUSTOMERS_QUERY

repeat_category_values = {
    '0_To_3_Lacs': 30,                  
    '3_To_6_Lacs': 40,
    'Greater_Than_6_Lacs': 40
}


def get_repeat_customers_data():
    """Read the repeat customers data from the database using the query."""

    engine = get_db_engine_pos()
    data = get_data(REPEAT_CUSTOMERS_QUERY, engine)
    return data


def assign_category(data, store_category_data):
    """Assigns the category from the store_category_data to the data"""

    data = pd.merge(data, store_category_data, on='store_id', how='left')
    return data


def filter_based_on_category(data):
    """Filters the data based on the category and removes the remaining data"""
    
    conditions = [
        (data['category'] == '0_To_3_Lacs') & ((data['bill_count'] > 5) | (data['LTV'] > 500)),
        (data['category'] == '3_To_6_Lacs') & ((data['bill_count'] > 5) | (data['LTV'] > 750)),
        (data['category'] == 'Greater_Than_6_Lacs') & ((data['bill_count'] > 5) | (data['LTV'] > 1000))
    ]

    filtered_data = data[conditions[0] | conditions[1] | conditions[2]]
    return filtered_data


def final_data_limited(filtered_data):
    filtered_data = filtered_data.sort_values(['category', 'LTV'], ascending=[True, False])

    final_data = pd.DataFrame()
    for category in repeat_category_values.keys():
        final_data = pd.concat([final_data, filtered_data[filtered_data['category'] == category].head(repeat_category_values[category])])

    return final_data


def main():
    new_customers_data = get_repeat_customers_data()
    # new_customers_data = assign_category(new_customers_data)
    # filtered_data = filter_based_on_category(new_customers_data)
    # final_data = final_data_limited(filtered_data)
    #return final_data
    print(new_customers_data)


