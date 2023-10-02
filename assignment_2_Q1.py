# 28-9-23
# CSC461 – Assignment2 – Regular Expressions
# Muhammad Sarmad Aslam
# Fa21-BSE-093
# Write regular expressions to accomplish 10 tasks

import re

# read the content of example-text.txt
with open("example-text.txt", "r") as file:
    text = file.read()

# task 1. extract list of all words.
words = re.findall(r'\b\w+\b', text)

# task 2. extract list of all words starting with a capital letter.
capital_words = re.findall(r'\b[A-Z]\w*\b', text)

# task 3. extract list of all words of length 5.
words_length_5 = re.findall(r'\b\w{5}\b', text)

# task 4. extract list of all words inside double quotes.
words_in_double_quotes = re.findall(r'"(.*?)"', text)

# task 5. extract list of all vowels.
vowels = re.findall(r'[aeiouAEIOU]', text)

# task 6. extract list of 3 letter words ending with letter 'e'.
three_letter_words_ending_with_e = re.findall(r'\b\w{3}e\b', text)

# task 7. extract list of all words starting and ending with letter 'b'.
words_starting_and_ending_with_b = re.findall(r'\b\w*b\w*\b', text)

# task 8. remove all the punctuation marks from the text.
text_without_punctuation = re.sub(r'[^\w\s]', '', text)

# task 9. replace all words ending 'n't' to their full form 'not'.
text_with_full_form_not = re.sub(r'\b(\w+)n\'t\b', r'\1 not', text)

# task 10. replace all the new lines with a single space.
text_without_newlines = re.sub(r'\n', ' ', text)

# Printing
print("1. List of all words:", words)
print("\n2. List of all words starting with a capital letter:", capital_words)
print("\n3. List of all words of length 5:", words_length_5)
print("\n4. List of all words inside double quotes:", words_in_double_quotes)
print("\n5. List of all vowels:", vowels)
print("\n6. List of 3 letter words ending with 'e':", three_letter_words_ending_with_e)
print("\n7. List of words starting and ending with 'b':", words_starting_and_ending_with_b)
print("\n8. Text without punctuation marks:", text_without_punctuation)
print("\n9. Text with 'n't' replaced by 'not':", text_with_full_form_not)
print("\n10. Text with new lines replaced by a single space:", text_without_newlines)