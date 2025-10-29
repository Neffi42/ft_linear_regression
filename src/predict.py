import sys


def estimate_price(theta0, theta1, mileage):
    return theta0 + theta1 * mileage


def get_mileage():
    while True:
        mileage = input("Enter a mileage: ")
        try:
            f_mileage = float(mileage)
            return f_mileage
        except ValueError:
            print("Wrong input, try again.")


def set_thetas():
    argc = len(sys.argv)

    if argc == 3:
        try:
            return float(sys.argv[1]), float(sys.argv[2])
        except ValueError:
            print("Wrong arguments.")
    elif argc != 1:
        print("Wrong arguments")

    return 0.0, 0.0


def main():
    theta0, theta1 = set_thetas()
    mileage = get_mileage()
    prediction = estimate_price(theta0, theta1, mileage)
    print(f"Estimated price for {mileage} km: {prediction}.")


if __name__ == "__main__":
    main()
