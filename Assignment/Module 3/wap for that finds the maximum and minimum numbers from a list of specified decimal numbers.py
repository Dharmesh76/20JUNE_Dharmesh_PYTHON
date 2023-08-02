def find_max_min(numbers):
    if not numbers:
        return None, None

    max_num = min_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num

def main():
    num_str = input("Enter a list of decimal numbers separated by spaces: ")
    num_list = [float(num) for num in num_str.split()]

    max_number, min_number = find_max_min(num_list)

    if max_number is None or min_number is None:
        print("No numbers entered.")
    else:
        print(f"The maximum number is: {max_number}")
        print(f"The minimum number is: {min_number}")

if __name__ == "__main__":
    main()
