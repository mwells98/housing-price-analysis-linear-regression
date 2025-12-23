import pandas as pd

def load_data(file_path='housing_data.csv'):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f'File not found: {file_path}')
        return None
