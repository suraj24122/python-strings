# count vowles in a string

input_string = input("Enter a string value = ")
input_string = input_string.casefold() # or caseFold or lower

vowels = "aeiou"

vowels_data = {}.fromkeys(vowels,0)
totalVowelCount = 0

for character in input_string:
    if character in vowels:
        vowels_data[character] += 1
        totalVowelCount += 1

print("Total vowels = ",totalVowelCount)
for vowel in vowels_data:
    print(vowel,"=>", vowels_data[vowel])






