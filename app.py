import pandas as pd
import numpy as np
# Databases
import sqlite3

try:
    con = sqlite3.connect('./data/score.db')
except Exception as err:
    print(f"Connection error:\n{err}")

# Extract data as pd.DataFrame
cur = con.cursor()
raw_df = pd.read_sql_query('SELECT * FROM score', con)

# Close db connection
con.close()