import sys
import pandas as pd
from predict import estimate_price

DEFAULT_DATA = "data.csv"
LEARNING_RATE = 0.001
LIMIT = 0.00001


def gradient_descent(df: pd.DataFrame):
    data_len = len(df.index)

    theta0 = 0.0
    theta1 = 0.0

    while True:
        old_theta0 = theta0
        old_theta1 = theta1
        sum0 = 0.0
        sum1 = 0.0

        for _, row in df.iterrows():
            km = row["km"]
            price = row["price"]
            prediction = estimate_price(theta0, theta1, km)
            error = prediction - price
            sum0 = sum0 + error
            sum1 = sum1 + error * km

        theta0 = theta0 - LEARNING_RATE * (1 / data_len) * sum0
        theta1 = theta1 - LEARNING_RATE * (1 / data_len) * sum1

        if abs(theta0 - old_theta0) < LIMIT and abs(theta1 - old_theta1) < LIMIT:
            break

    return theta0, theta1


def main():
    file = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DATA
    df_raw = pd.read_csv(file)

    df_norm = df_raw.apply(lambda x: (x - x.mean()) / x.std())
    theta0_norm, theta1_norm = gradient_descent(df_norm)

    price_mean = df_raw["price"].mean()
    price_std = df_raw["price"].std()
    km_mean = df_raw["km"].mean()
    km_std = df_raw["km"].std()

    theta0_raw = (
        price_mean
        + price_std * theta0_norm
        - (price_std * theta1_norm * km_mean / km_std)
    )
    theta1_raw = theta1_norm * (price_std / km_std)

    print(f"From the data in {file}:\n\ttheta0 = {theta0_raw}\n\ttheta1 = {theta1_raw}")


if __name__ == "__main__":
    main()
