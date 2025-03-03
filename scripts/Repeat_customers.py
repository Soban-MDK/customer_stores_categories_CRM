import pandas as pd
import numpy as np

from db.connections import get_db_engine_pos
from db.common_helpers import get_data
from db.queries import REPEAT_CUSTOMERS_QUERY

def get_repeat_customers_data():
    engine = get_db_engine_pos()
    data = get_data(engine, REPEAT_CUSTOMERS_QUERY)
    return data

def assign_category(data):
    