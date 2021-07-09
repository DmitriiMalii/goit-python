def fibonacci(number):
    if number < 2:
        return number
    else:
        return (fibonacci(number - 1) + fibonacci(number - 2))


def main():
    while True:
            number = input("Enter a memeber in Fibonacci series, # ")
            if number.isdigit:
                number = int(number)
                if number > 0:
                    print(fibonacci(number - 1))
                    break
                else:
                    print("Enter a positive number.")
            else:
                print("Char is not a digit. Try again, please.")

if __name__ == "__main__":
    main()
