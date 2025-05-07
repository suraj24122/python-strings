# python-strings
Here are some programs demonstrate the strings in python
String Manipulation Programs
This repository contains a collection of Python programs demonstrating various string manipulation techniques. Each program focuses on a different operation, from reversing strings to counting vowels and checking for palindromes.

Programs Included
1. program_1.py - String Reversal
Description: Reverses a given string using a loop.

Usage:

python
print(reverse_string("Suraj"))  # Output: "jaruS"
Key Concept: Builds the reversed string by prepending each character.

2. program_2.py - Palindrome Checker
Description: Checks if a user-input string is a palindrome (reads the same backward as forward).

Usage:

python
Enter the value = madam  # Output: "The value entered by user is palindrome"
Key Concept: Uses slicing ([::-1]) to reverse the string and compares it with the original.

3. program_3.py - Vowel Counter
Description: Counts the occurrences of each vowel in a user-input string (case-insensitive).

Usage:

python
Enter a string value = Hello World
# Output: 
# Total vowels = 3
# a => 0
# e => 1
# i => 0
# o => 2
# u => 0
Key Concept: Uses a dictionary to track vowel counts and iterates through the string.

4. program_4.py - Space Remover
Description: Removes all spaces from a given string.

Usage:

python
Input: "Hello World" → Output: "HelloWorld"
Key Concept: Uses the replace() method to eliminate spaces.

How to Run
Clone the repository:

bash
git clone https://github.com/your-username/string-manipulation.git
Navigate to the directory:

bash
cd string-manipulation
Run any program using Python:

bash
python program_1.py
Dependencies
Python 3.x

Contributing
Feel free to contribute by opening issues or submitting pull requests. Suggestions for additional string manipulation programs are welcome!

License
This project is open-source and available under the MIT License. See the LICENSE file for details.
