import pandas as pd
from google.cloud import bigquery

def run_pipeline():
    client = bigquery.Client()
    query = 'SELECT name, SUM(number) as total FROM `bigquery-public-data.usa_names.usa_1910_current` GROUP BY name ORDER BY total DESC LIMIT 10'
    df = client.query(query).to_dataframe()
    print(df)

if __name__ == "__main__":
    run_pipeline()
