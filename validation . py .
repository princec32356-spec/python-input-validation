
def validate_age(age):
    """Validate an age supplied by a user."""
    if age is None:
        raise ValueError("Age is required")

    age = int(age)

    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120")

    return age


def validate_username(username):
    """Validate a username."""
    if not username:
        raise ValueError("Username is required")

    return username.strip()
