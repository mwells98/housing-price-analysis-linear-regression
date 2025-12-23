# Housing Price Predictor

A Python project that predicts housing prices based on house size using linear regression. The project includes **data generation, exploration, visualization**, and **predictive modeling**, making it a complete example of a beginner-friendly data science workflow.

---

## **Features**

- Generates a random dataset of houses if none exists.
- Computes basic statistics: min, max, and average price and size.
- Visualizes data with scatter plots, histograms, and bar charts.
- Trains a linear regression model to predict house prices.
- Allows user input to predict the price of a house of a given size.
- Fully modular and organized for learning and portfolio purposes.

---

## **Project Structure**

```
housing-price-predictor/
├── README.md 
├── main.py 
├── housing_data.csv # Optional dataset (auto-generated if missing)
└── housing/
├── data.py 
├── explore.py 
├── visualize.py 
├── model.py 
└── generate_data.py 

---

## Requirements

System Requirements:

- Python 3.8 or higher  
- Compatible with Windows, macOS, or Linux  

---

## **Installation**

1. Clone the repository:

```bash
git clone <your-repo-url>
cd housing-price-predictor```

2. Install the required packages:

```bash
pip install -r requirements.txt```

---

## Usage

Run the project

```bash
python main.py```

- If housing_data.csv does not exist, the program will automatically generate 100 random rows of housing data.
- The program will print key statistics about the dataset.
- It will show four visualizations:
	- Scatter plot: Price vs Size  
	- Histogram: Price per Square Foot  
	- Bar chart: Min, Max, and Average Price  
	- Scatter plot: Price per Square Foot vs Size  
- After visualizations, the program trains a linear regression model and allows you to input a house size to predict the price.

---

## Dependencies

The project uses the following Python libraries:  

- pandas  
- numpy  
- matplotlib  
- scikit-learn  

All dependencies can be installed using:

```bash
pip install -r requirements.txt```

---

## Example Output

The most expensive house is $482500
The cheapest house is $80000
The largest house is 3490 sqft
The smallest house is 520 sqft
The average cost for all houses is $236750.42
The average cost per square foot is $85.32

Followed by plots and regression results:  
**Coefficient:** 150.23  
**Intercept:** 50234.50  
**R2 Score:** 0.92  

Then you can enter a size:
Enter the size of house in sqft to predict cost: 1500
The estimated price for a house of 1500 sqft is $227,500.00

---

## Why This Project is Useful

- Demonstrates data exploration, visualization, and regression modeling.
- Shows modular Python programming and clean project structure.
- Includes dataset generation, allowing anyone to run it without external files.
- Perfect for a beginner data science portfolio to showcase Python and analytical skills.

---
