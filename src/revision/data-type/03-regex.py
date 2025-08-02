# This file demonstrates basic regex operations in Python.
import re

# Example string
text = "The rain in Spain stays mainly in the plain."

# Find all words that start with 'S'
pattern = r'\bS\w+'
matches = re.findall(pattern, text, re.IGNORECASE)
print("Words that start with 'S':", matches) # Output: Words that start with 'S': ['Spain', 'stays']

# Find all words in the text
all_words = re.findall(r'\b\w+\b', text)
print("All words in the text:", all_words) # Output: All words in the text: ['The', 'rain', 'in', 'Spain', 'stays', 'mainly', 'in', 'the', 'plain']

# Find all occurrences of 'in' with word boundaries
in_word_matches = re.findall(r'\bin\b', text)
print("Occurrences of 'in' with word boundaries:", in_word_matches) # Output: Occurrences of 'in' with word boundaries: ['in', 'in']

# Find all occurrences of 'in'
in_matches = re.findall(r'in', text)
print("Occurrences of 'in':", in_matches) # Output: ccurrences of 'in': ['in', 'in', 'in', 'in', 'in', 'in']

# Search for the first occurrence of 'rain'
match = re.search(r'rain', text)
if match:
    print("Found 'rain' at position:", match.start()) # Output: Found 'rain' at position: 4
else:
    print("'rain' not found.") 

# Replace 'rain' with 'sunshine'
new_text = re.sub(r'rain', 'sunshine', text)
print("Modified text:", new_text) # Output: Modified text: The sunshine in Spain stays mainly in the plain.

# Find all uppercase words
uppercase_words = re.findall(r'\b[A-Z]+\b', text)
print("Uppercase words in the text:", uppercase_words) # Output: Uppercase words in the text: []

# Find all lowercase words
lowercase_words = re.findall(r'\b[a-z]+\b', text)
print("Lowercase words in the text:", lowercase_words) # Output: Lowercase words in the text: ['the', 'rain', 'in', 'stays', 'mainly', 'in', 'the', 'plain']

# Find all words with exactly 4 letters
four_letter_words = re.findall(r'\b\w{4}\b', text)
print("Words with exactly 4 letters:", four_letter_words) # Output: Words with exactly 4 letters: ['rain']

# Find all words that contain 'ain'
words_with_ain = re.findall(r'\b\w*ain\w*\b', text)
print("Words that contain 'ain':", words_with_ain)  # Output: Words that contain 'ain': ['rain', 'Spain', 'mainly', 'plain']

# Find all words that end with 'ain'
words_ending_with_ain = re.findall(r'\b\w*ain\b', text)
print("Words that end with 'ain':", words_ending_with_ain)  # Output: Words that end with 'ain': ['rain', 'Spain', 'plain']

# Find all words that start with a consonant
consonant_words = re.findall(r'\b[b-df-hj-np-tv-z]\w*', text)
print("Words that start with a consonant:", consonant_words) # Output: Words that start with a consonant: ['rain', 'stays', 'mainly', 'the', 'plain']

# Find all words that start with a vowel
vowel_words = re.findall(r'\b[aeiouAEIOU]\w*', text)
print("Words that start with a vowel:", vowel_words) # Output: Words that start with a vowel: ['in', 'in']

# Find all words that contain digits
words_with_digits = re.findall(r'\b\w*\d\w*\b', text)
print("Words that contain digits:", words_with_digits) # Output: Words that contain digits: []

# Find all words that contain 'ain' and are followed by a word
words_with_ain_followed_by_word = re.findall(r'\b\w*ain\b \w+', text)
print("Words that contain 'ain' followed by another word:", words_with_ain_followed_by_word)  # Output: Words that contain 'ain' followed by another word: ['rain in', 'Spain stays']

# Find all words that contain 'ain' and are followed by a punctuation mark
words_with_ain_followed_by_punctuation = re.findall(r'\b\w*ain\b[.,;:!?]', text)
print("Words that contain 'ain' followed by punctuation:", words_with_ain_followed_by_punctuation) # Output: Words that contain 'ain' followed by punctuation: ['plain.']

# Find all words that contain 'ain' and are followed by a digit
words_with_ain_followed_by_digit = re.findall(r'\b\w*ain\b \d+', text)
print("Words that contain 'ain' followed by a digit:", words_with_ain_followed_by_digit) # Output: Words that contain 'ain' followed by a digit: []

# Find all digits in the text
digits = re.findall(r'\d+', text)
print("Digits in the text:", digits) # Output: Digits in the text: []

# Split the text into sentences
sentences = re.split(r'\. ', text)
print("Sentences:", sentences) # Output: Sentences: ['The rain in Spain stays mainly in the plain.']

# Check if the text contains 'Spain'
if re.search(r'Spain', text):
    print("The text contains 'Spain'.") # Output: The text contains 'Spain'.
else:
    print("The text does not contain 'Spain'.")

# Check if the text starts with 'The'
if re.match(r'The', text):
    print("The text starts with 'The'.") # Output: The text starts with 'The'.
else:
    print("The text does not start with 'The'.")


# Example of using regex to validate an email address
email = "example@example.com"
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
if re.match(email_pattern, email):
    print("Valid email address.") # Output: Valid email address.
else:
    print("Invalid email address.")

# Example of using regex to validate a phone number
phone_number = "+1-234-567-8900"
phone_pattern = r'^\+\d{1,3}-\d{3}-\d{3}-\d{4}$' 
if re.match(phone_pattern, phone_number):
    print("Valid phone number.") # Output: Valid phone number.
else:
    print("Invalid phone number.")

# Example of using regex to validate a URL
url = "https://www.example.com/path/to/resource"
url_pattern = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'
if re.match(url_pattern, url):
    print("Valid URL.") # Output: Valid URL.
else:
    print("Invalid URL.")

# Example of using regex to extract a date in the format YYYY-MM-DD
date_text = "Today's date is 2023-10-01."
date_pattern = r'\b\d{4}-\d{2}-\d{2}\b'
date_matches = re.findall(date_pattern, date_text)
if date_matches:
    print("Extracted date:", date_matches[0]) # Output: Extracted date: 2023-10-01
else:
    print("No date found in the text.")

# Example of using regex to extract a time in the format HH:MM
time_text = "The meeting is scheduled for 14:30."
time_pattern = r'\b\d{2}:\d{2}\b'
time_matches = re.findall(time_pattern, time_text)
if time_matches:
    print("Extracted time:", time_matches[0]) # Output: Extracted time: 14:30
else:
    print("No time found in the text.")

# Split a string using a regex pattern
text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result) # Output: Split result: ['apple', 'banana', 'orange', 'grape']
