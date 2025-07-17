import re

# text =  "Contact us at info@example.com or support@domain.org. or t-_est@test.eu"

# pattern = re.compile(r"\b[a-zA-Z0-9._%+-]+@\w*.\w{2,}")
# for match in re.findall(pattern, text):
#     print(match)


text = 'testse Atets the data etty1'
pattern = re.compile(r'\bA.*\d$')
match = re.match(pattern, text)
print(match)
match = re.search(pattern, text)
print(match)

text = "123-456-7889"
pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
for match in re.finditer(pattern, text):
    print(match)