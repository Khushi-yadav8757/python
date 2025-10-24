import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.fullmatch(pattern, email):
        return "Valid Email"
    else:
        return "Invalid Email"

# Test
print(validate_email("example123@gmail.com"))
print(validate_email("example@.com"))
