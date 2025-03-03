# id, order_no, order_date, customer_code, customer_name, customer_mobile, store_name, total_amt, created_at2, store_category, asm_mail, manager, territory, sales_owner_email, LTV, NoOfBills
import pandas as pd
import numpy as np

from db.common_helpers import get_data
from db.connections import get_db_engine_pos
from db.queries import NEW_CUSTOMERS_QUERY

repeat_categroy_values = {
    '0_To_3_Lacs': 30,                  
    '3_To_6_Lacs': 40,
    'Greater_Than_6_Lacs': 40
}


def get_new_customers_data():
    engine = get_db_engine_pos()
    data = get_data(NEW_CUSTOMERS_QUERY, engine)
    return data

def assign_category(data, store_category_data):
    data = pd.merge(data, store_category_data, on='store_id', how='left')
    return data




def main():
    new_customers_data = get_new_customers_data()
    # new_customers_data = assign_category(new_customers_data)
    print(new_customers_data)

