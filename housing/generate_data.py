import pandas as pd
import numpy as np

def generate_random_data(file_path='housing_data.csv', n=100, seed=42):
    np.random.seed(seed)

    #Random house sizes between 500 and 3500 sqft
    sizes = np.random.randint(500, 3500, n)

    #Prices roughly correlated with size, with some variance
    prices = 50000 + (sizes * 150) + np.random.randint(-30000, 30000, n)

    df = pd.DataFrame({
        'Size': sizes,
        'Price': prices
    })

    df.to_csv(file_path, index=False)
    print(f"Random dataset with {n} rows saved to {file_path}")
    return df

if __name__ == "__main__":
    generate_random_data()
