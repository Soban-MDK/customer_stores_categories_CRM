# id, order_no, order_date, customer_code, customer_name, customer_mobile, store_name, total_amt, created_at2, store_category, asm_mail, manager, territory, sales_owner_email, LTV, NoOfBills
import pandas as pd
import numpy as np

from db.common_helpers import get_data
from db.connections import get_db_engine_pos
from db.queries import NEW_CUSTOMERS_QUERY

new_category_values = {
    '0_To_3_Lacs': 15,                  
    '3_To_6_Lacs': 10,
    'Greater_Than_6_Lacs': 5
}


def get_new_customers_data():
    """Read the new customers data from the database using the query."""

    engine = get_db_engine_pos()
    data = get_data(NEW_CUSTOMERS_QUERY, engine)
    return data


def assign_category(data, store_category_data):
    """Assigns the category from the store_category_data to the data"""

    data = pd.merge(data, store_category_data, on='store_id', how='left')
    return data


def filter_based_on_category(data):
    """Filters the data based on the category and removes the remaining data"""
    
    conditions = [
        (data['category'] == '0_To_3_Lacs') & ((data['bill_count'].between(1, 5)) | (data['AOV'] > 50)),
        (data['category'] == '3_To_6_Lacs') & ((data['bill_count'].between(1, 5)) | (data['AOV'] > 100)),
        (data['category'] == 'Greater_Than_6_Lacs') & ((data['bill_count'].between(1, 5)) | (data['AOV'] > 200))
    ]

    filtered_data = data[conditions[0] | conditions[1] | conditions[2]]
    return filtered_data


def final_data_limited(filtered_data):
    filtered_data = filtered_data.sort_values(['category', 'LTV'], ascending=[True, False])

    final_data = pd.DataFrame()
    for category in new_category_values.keys():
        final_data = pd.concat([final_data, filtered_data[filtered_data['category'] == category].head(new_category_values[category])])

    return final_data


def main():
    new_customers_data = get_new_customers_data()
    # new_customers_data = assign_category(new_customers_data)
    # filtered_data = filter_based_on_category(new_customers_data)
    # final_data = final_data_limited(filtered_data)
    #return final_data

