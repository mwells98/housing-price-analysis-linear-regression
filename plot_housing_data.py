import matplotlib.pyplot as plt

def plot_housing_data(df, stats):

    #Scatter plot: Price vs Size
    plt.figure(figsize=(8,5))
    plt.scatter(df['Size'], df['Price'], color='blue', alpha=0.6)
    plt.xlabel('Size (sqft)')
    plt.ylabel('Price ($)')
    plt.title('Housing Price VS Size')
    plt.grid(True)
    plt.show()

    #Histogram: Price per sqft
    plt.figure(figsize=(8,5))
    plt.hist(df['avg_per_sqft'], bins=15, color='green', edgecolor='black', alpha=0.7)
    plt.xlabel('Price per Square Foot ($)')
    plt.ylabel('Number of Houses')
    plt.title('Distribution of Price per Square Foot')
    plt.grid(axis='y')
    plt.show()

    #Bar chart: Max, Min, Avg Price
    labels = ['Max Price', 'Min Price', 'Average Price']
    values = [stats['max_price'], stats['min_price'], stats['avg_price']]

    plt.figure(figsize=(8,5))
    plt.bar(labels, values, color=['red', 'blue', 'green'])
    plt.ylabel('Price ($)')
    plt.title('Housing Price Stats')
    plt.show()

    #Scatter plot: Price per sqft vs Size
    plt.figure(figsize=(8,5))
    plt.scatter(df['Size'], df['avg_per_sqft'], color='purple', alpha=0.6)
    plt.xlabel('Size (sqft)')
    plt.ylabel('Price per Square Foot ($)')
    plt.title('Price per Square Foot VS Size')
    plt.grid(True)
    plt.show()
