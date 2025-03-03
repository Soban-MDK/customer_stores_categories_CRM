from sqlalchemy.orm import sessionmaker
from utils.logger import logging,logger
import pandas as pd
from sqlalchemy.sql import text

def get_data(query,engine):
    try:
        engine_mre_read = engine
        with engine_mre_read.connect() as conn:
            result = conn.execute(text(query))
            rows = result.fetchall()
            columns = result.keys()
            df = pd.DataFrame(rows, columns=columns)
            return df
    except Exception as e:
       logging()
       return pd.DataFrame()