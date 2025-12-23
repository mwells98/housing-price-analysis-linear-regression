from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

def train_regression(df):
    X = df['Size'].values.reshape(-1, 1)
    y = df['Price'].values
    model = LinearRegression()
    model.fit(X, y)

    print('Coefficient:', model.coef_[0])
    print('Intercept:', model.intercept_)

    #Train-test split for R2
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print('R2 Score:', r2_score(y_test, y_pred))

    return model

def predict_price(model, size):
    price = model.predict([[size]])[0]
    return price
