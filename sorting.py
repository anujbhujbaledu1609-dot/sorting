# Program: Sort numbers entered by the user

# Step 1: Take input from user
# Example input: 5 2 9 1 7
numbers_input = input("Enter numbers separated by spaces: ")

# Step 2: Convert input string into a list of integers
try:
    numbers = list(map(int, numbers_input.split()))
except ValueError:
    print("❌ Invalid input! Please enter only numbers separated by spaces.")
    exit()

# Step 3: Sort the list in ascending order
numbers.sort()

# Step 4: Display the result
print("\n✅ Sorted numbers (ascending):")
print(numbers)

# Optional: Descending order
numbers.sort(reverse=True)
print("\n⬇️ Sorted numbers (descending):")
print(numbers)
