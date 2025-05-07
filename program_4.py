# Function to remove all spaces from a string
def remove_spaces(input_string):
    return input_string.replace(" ", "")

# Example usage
if __name__ == "__main__":
    input_string = "Hello World"
    result = remove_spaces(input_string)
    print(f"Input: \"{input_string}\" → Output: \"{result}\"")
