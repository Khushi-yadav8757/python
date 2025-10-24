import re

def check_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if re.fullmatch(pattern, password):
        return "Strong Password"
    else:
        return "Weak Password"

# Test
print(check_password("Khushi@123"))
print(check_password("khushi123"))
