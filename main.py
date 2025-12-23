import os
from housing.generate_data import generate_random_data
from housing.data import load_data
from housing.explore import explore_data
from housing.visualize import plot_housing_data
from housing.model import train_regression, predict_price

def main():
    if not os.path.exists('housing_data.csv'):
        print("Data file not found so I will generate a random dataset!")
        generate_random_data()

    df = load_data()
    if df is None:
        return

    df, stats = explore_data(df)

    #Display stats
    print(f"The most expensive house is ${stats['max_price']}")
    print(f"The cheapest house is ${stats['min_price']}")
    print(f"The largest house is {stats['max_sqft']} sqft")
    print(f"The smallest house is {stats['min_sqft']} sqft")
    print(f"The average cost for all houses is ${stats['avg_price']:.2f}")
    print(f"The average cost per square foot is ${df['avg_per_sqft'].mean():.2f}")

    #Visualizations
    plot_housing_data(df, stats)

    #Train regression model
    model = train_regression(df)

    #Prediction input
    while True:
        try:
            size = float(input('Enter the size of house in sqft to predict cost: '))
            if size <= 0:
                print('Please enter a positive number.')
                continue
            price = predict_price(model, size)
            print(f'The estimated price for a house of {size} sqft is ${price:.2f}')
            break
        except ValueError:
            print('Invalid input, try again.')

if __name__ == "__main__":
    main()
