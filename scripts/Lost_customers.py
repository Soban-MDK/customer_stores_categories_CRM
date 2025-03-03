# id, order_no, order_date, customer_code, customer_name, customer_mobile, store_name, total_amt, created_at2, store_category, asm_mail, manager, territory, sales_owner_email, LTV, NoOfBills
import pandas as pd
import numpy as np

from db.common_helpers import get_data
from db.connections import get_db_engine_pos
from db.queries import LOST_CUSTOMERS_QUERY
from utils.logger import logger, logging


lost_categroy_values = {
    '0_To_3_Lacs': 15,                  
    '3_To_6_Lacs': 10,
    'Greater_Than_6_Lacs': 15
}

def get_new_customers_data():
    """Read the new customers data from the database using the query."""

    engine = get_db_engine_pos()
    data = get_data(LOST_CUSTOMERS_QUERY, engine)
    return data


def assign_category(data, store_category_data):
    """Assigns the category from the store_category_data to the data"""

    ## IF it is required to read store categories then do it here

    data = pd.merge(data, store_category_data, on='store_id', how='left')
    return data


def filter_based_on_categroy(data):
    """Filters the data based on the category and removes the remaining data"""
    try:
        conditions = [
            (data['category'] == '0_To_3_Lacs') & ((data['bill_count'] > 5) | (data['LTV'] > 500)),
            (data['category'] == '3_To_6_Lacs') & ((data['bill_count'] > 5) | (data['LTV'] > 750)),
            (data['category'] == 'Greater_Than_6_Lacs') & ((data['bill_count'] > 5) | (data['LTV'] > 1000))
        ]

        filtered_data = data[conditions[0] | conditions[1] | conditions[2]]
        return filtered_data

    except Exception as e:
        logging()
        return


def final_data_limited(filtered_data):
    try:
        filtered_data = filtered_data.sort_values(['category', 'LTV', 'bill_count'], ascending=[True, False, False])

        final_data = pd.DataFrame()
        for category in lost_categroy_values.keys():
            final_data = pd.concat([final_data, filtered_data[filtered_data['category'] == category].head(lost_categroy_values[category])])

        return final_data

    except Exception as e:
        logging()
        return


def main():
    try:
        new_customers_data = get_new_customers_data()
        # new_customers_data = assign_category(new_customers_data)
        # filtered_data = filter_based_on_categroy(new_customers_data)
        # final_data = final_data_limited(filtered_data)
        #return final_data
        logger.info("Lost customers task done successfully")


    except Exception as e:
        logging()
        return