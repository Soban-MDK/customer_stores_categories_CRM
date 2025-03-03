# id, order_no, order_date, customer_code, customer_name, customer_mobile, store_name, total_amt, created_at2, store_category, asm_mail, manager, territory, sales_owner_email, LTV, NoOfBills
import pandas as pd
import numpy as np

from db.common_helpers import get_data
from db.connections import get_db_engine_pos
from db.queries import LOST_CUSTOMERS_QUERY

def get_new_customers_data():
    engine = get_db_engine_pos()
    data = get_data(engine, LOST_CUSTOMERS_QUERY)
    return data

