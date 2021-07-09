def fibonacci(number):
    if number < 2:
        return number
    else:
        return (fibonacci(number - 1) + fibonacci(number - 2))


def main():
    while True:
        try:
            number = int(input("Enter a memeber in Fibonacci series, # "))
            if number <= 0:
                print("Enter a positive number.")
            else:
                print(fibonacci(number - 1))
                break
        except ValueError:
            print("Char is not a digit")


if __name__ == "__main__":
    main()
