import re
def is_email_valid(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

print(is_email_valid("example@example.com"))  # True
print(is_email_valid("invalid-email"))        # False