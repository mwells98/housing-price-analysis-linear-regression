def explore_data(df):
    df['avg_per_sqft'] = df['Price'] / df['Size']
    stats = {
        'max_price': df['Price'].max(),
        'min_price': df['Price'].min(),
        'avg_price': df['Price'].mean(),
        'max_sqft': df['Size'].max(),
        'min_sqft': df['Size'].min(),
        'avg_sqft': df['Size'].mean()
    }
    return df, stats
