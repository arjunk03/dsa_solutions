# import re

# text = "The quick brown fox jumps over the lazy dog."

# # Example 1: Search for a simple word
# match_obj = re.search(r'fox', text)
# if match_obj:
#     print(f"1. Found '{match_obj.group(0)}' at index {match_obj.start()} to {match_obj.end()}")
#     # Output: 1. Found 'fox' at index 16 to 19
# else:
#     print("1. Pattern not found.")


import re

def validate_email(email):
    # Pattern: username@domain.tld
    # ^[a-zA-Z0-9._%+-]+ : Matches the username part, allowing alphanumeric characters, dots, underscores, percent signs, plus signs, or hyphens.
    # @ : Matches the literal '@' symbol.
    # [a-zA-Z0-9.-]+ : Matches the domain name part, allowing alphanumeric characters, dots, or hyphens.
    # \. : Matches a literal dot (escaped because '.' is a metacharacter).
    # [a-zA-Z]{2,}$ : Matches the top-level domain (TLD), requiring at least two alphabetic characters at the end of the string.
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Test cases [2]
# print(f"'user@example.com' is valid: {validate_email('user@example.com')}") # True
# print(f"'invalid_email' is valid: {validate_email('invalid_email')}")       # False
# print(f"'user@subdomain.example.co.uk' is valid: {validate_email('user@subdomain.example.co.uk')}") # True

# email = "user@example.com"
# pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# print(re.match(pattern, email))


# def extract_phone_numbers(text):
#     # Pattern designed to match phone numbers in various formats:
#     # \b : Word boundary to ensure whole words are matched.
#     # (?:+\d{1,2}\s?)? : Optional non-capturing group for country code (e.g., +1, +91) followed by an optional space.
#     # (?:\(?\d{3}\)?|\d{3}) : Matches a 3-digit area code, allowing for optional parentheses around it or just three digits.
#     # [-.s]? : Optional separator (dash, dot, or space).
#     # \d{3} : Matches the next 3 digits.
#     # [-.s]? : Optional separator.
#     # \d{4} : Matches the last 4 digits.
#     # \b : Word boundary.
#     pattern = r'\b(?:\+?\d{1,2}\s?)?(?:\(?\d{3}\)?|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}\b'
#     return re.findall(pattern, text)

# # Test case [2]
# text = "Contact us at +1 (555) 123-4567 or 123-456-7890 for assistance. My office is 987.654.3210."
# phone_numbers = extract_phone_numbers(text)
# print(f"Extracted Phone Numbers: {phone_numbers}") # ['+1 (555) 123-4567', '123-456-7890', '987.654.3210']

# text = "<p>First paragraph</p><p>Second paragraph</p>"
# greedy_pattern = r"<p>.*</p>"
# greedy_matches = re.findall(greedy_pattern, text)
# print(greedy_matches)


# text = "<p>First paragraph</p><p>Second paragraph</p>"
# non_greedy_pattern = r"<p>.*?</p>"
# non_greedy_matches = re.findall(non_greedy_pattern, text)
# print(non_greedy_matches)


# text = "apple pie and cherry pie"

# # Using a capturing group
# pattern_capturing = r"(\w+)\s(pie)"
# match_capturing = re.search(pattern_capturing, text)
# if match_capturing:
#     print(f"Capturing group match: {match_capturing.groups()}") # Output: ('apple', 'pie')

# # Using a non-capturing group for 'pie'
# pattern_non_capturing = r"(\w+)\s(?:pie)"
# match_non_capturing = re.search(pattern_non_capturing, text)
# if match_non_capturing:
#     print(f"Non-capturing group match: {match_non_capturing.groups()}") # Output: ('apple',)




# text = "Visit example.com or www.test.org"

# # Using a capturing group for "www."
# pattern_capturing = re.compile(r"(www\.)?(\w+\.\w+)")
# for match in pattern_capturing.finditer(text):
#     print(f"Capturing group 0: {match.group(0)}, group 1: {match.group(1)}, group 2: {match.group(2)}") 
# # Output:
# # Capturing group 0: example.com, group 1: None, group 2: example.com
# # Capturing group 0: www.test.org, group 1: www., group 2: test.org

# # Using a non-capturing group for "www."
# pattern_non_capturing = re.compile(r"(?:www\.)?(\w+\.\w+)") 
# for match in pattern_non_capturing.finditer(text):
#     print(f"Non-capturing group 0: {match.group(0)}, group 1: {match.group(1)}")
# # Output:
# # Non-capturing group 0: example.com, group 1: example.com
# # Non-capturing group 0: www.test.org, group 1: test.org




# text = "apple pie and cherry pie"

# # Using a capturing group for "www."
# pattern_capturing = re.compile(r"(\w+)\s(pie)")
# for match in pattern_capturing.finditer(text):
#     print(f"Capturing group 0: {match.group(0)}, group 1: {match.group(1)}, group 2: {match.group(2)}") 
# # Output:
# # Capturing group 0: example.com, group 1: None, group 2: example.com
# # Capturing group 0: www.test.org, group 1: www., group 2: test.org

# # Using a non-capturing group for "www."
# pattern_non_capturing = re.compile(r"(\w+)\s(?:pie)") 
# for match in pattern_non_capturing.finditer(text):
#     print(f"Non-capturing group 0: {match.group(0)}, group 1: {match.group(1)}")
# # Output:
# # Non-capturing group 0: example.com, group 1: example.com
# # Non-capturing group 0: www.test.org, group 1: test.org




# text = "Name: Alice Wonderland"
# pattern = r"Name: (?P<first_name>\w+)\s(?P<last_name>\w+)"

# match = re.search(pattern, text)

# if match:
#     first_name = match.group("first_name")
#     last_name = match.group("last_name")

#     print(f"First Name: {first_name}")
#     print(f"Last Name: {last_name}")

# # Output:
# # First Name: Alice
# # Last Name: Wonderland