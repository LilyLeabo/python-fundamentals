# Function that tests if a user enters a number
def test_number():
    # Get user's number
    number = input("Enter a number: ")
    # Test if the user entered a number
    if number.isdigit():
        print("You entered a number!")
    else:
        print("You did not enter a number!")
# Call the function
test_number()