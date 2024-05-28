import re

def normalize_email(email):
    """ Normalize the email address by removing periods from the username and converting to lowercase. """
    parts = email.split('@')
    username = parts[0].replace('.', '').lower()
    domain = parts[1].lower()
    return f"{username}@{domain}"

def is_valid_email(email):
    """ Validate the email address based on the specified rules. """
    if email.count('@') != 1:
        return False

    username, domain = email.split('@')

    # Validate username length (6 to 30 characters)
    if len(username) < 6 or len(username) > 30:
        return False

    # Validate domain parts
    domain_parts = domain.split('.')
    if any(len(part) == 0 or len(part) > 30 for part in domain_parts):
        return False

    # Regular expression to match valid domain part
    domain_regex = re.compile("^[A-Za-z0-9-]+$")
    username_regex = re.compile("^[A-Za-z0-9_\.]+$")

    if not all(domain_regex.match(part) for part in domain_parts):
        return False
    if not username_regex.match(username):
        return False

    return True

def count_valid_emails(emails):
    """ Count distinct valid email addresses from a list of emails. """
    normalized_emails = set()

    for email in emails:
        if is_valid_email(email):
            normalized_emails.add(normalize_email(email))

    return len(normalized_emails)

# Example usage
emails = [
    "John.Doe@example.com",
    "john.doe@EXAMPLE.com",
    "inva@lid@-example-.com",
    "valid_email@example.co",
    "duplicate@example.com",
    "Duplicate@example.com"
]

count = count_valid_emails(emails)
print(count)
