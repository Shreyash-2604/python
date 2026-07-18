def calculate_average(numbers):
    # Check if the list is emty before calculating the averge
    if not numbers:
        return 0

    # Add all the number togather
    total = sum(numbers)

    # Devide the total by the lenght of the list
    average = total / len(numbers)

    # Return the finel result
    return average


def find_max(numbers):
    # Return None if no values are avalible
    if not numbers:
        return None

    # Find the largest number in the collecion
    return max(numbers)


def main():
    # Sample data for demostration
    scores = [85, 90, 78, 92, 88]

    # Print the averge score
    print(f"Average Score: {calculate_average(scores)}")

    # Print the highest score
    print(f"Highest Score: {find_max(scores)}")


if __name__ == "__main__":
    # Start the programe
    main()
