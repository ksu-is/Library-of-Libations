import os
import sqlite3
import pandas as pd

data_url = 'classic_cocktails.csv'
headers = ['drink_name','spirit','ingredient_1','ingredient_2','ingredient_3','garnish']
data_table = pd.read_csv(data_url, header=None, names=headers,)

# Clear example.db if it exists
if os.path.exists('drinks.db'):
     os.remove('drinks.db')

# Create a database
conn = sqlite3.connect('drinks.db')

# Add the data to our database
data_table.to_sql('data_table', conn, dtype={
    'drink_name':'VARCHAR(256)',
    'spirit':'VARCHAR(256)',
    'ingredient_1':'VARCHAR(256)',
    'ingredient_2':'VARCHAR(256)',
	'ingredient_3':'VARCHAR(256)',
	'garnish':'VARCHAR(556)',
})

conn.row_factory = sqlite3.Row

# Make a convenience function for running SQL queries
def sql_query(query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def sql_edit_insert(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()

def sql_delete(query,var):
    cur = conn.cursor()
    cur.execute(query,var)

def sql_query2(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    return rows
