def sum_of_divisors(number):
    divisor_sum = 0
    for i in range(1, number + 1):
        if number % i == 0:
            divisor_sum += i
    return divisor_sum

def main():
    num = int(input("Enter a number: "))
    result = sum_of_divisors(num)
    print(f"The sum of divisors of {num} is: {result}")

if __name__ == "__main__":
    main()
