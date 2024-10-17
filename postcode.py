import re
def is_valid_uk_postcode(postcode):
    # Regex pattern for UK postcodes
    pattern = r'^[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}$'
    return re.match(pattern, postcode) is not None

# Test cases
test_cases = [
    "M1 1AA",
    "M60 1NW",
    "CR2 6XH",
    "DN55 1PT",
    "W1A 1HQ",
    "EC1A 1BB",
    # Additional test cases
    "SW1A 0AA",  # Valid: Buckingham Palace
    "B33 8TH",   # Valid: Birmingham
    "CR0 2YR",   # Valid: Croydon
    "DN551PT",   # Valid: No space
    "W1A1HQ",    # Valid: No space
    "EC1A1BB",   # Valid: No space
    "M11AA",     # Invalid: No space in short postcode
    "M601NW",    # Invalid: No space in long postcode
    "1AA 2BB",   # Invalid: Doesn't start with letters
    "AM1 1AA",   # Invalid: Area code too long
    "A1A 1AA",   # Invalid: Wrong format
    "AA1A 1AA",  # Invalid: Wrong format
    "A11 1AA",   # Invalid: Wrong format
    "AA11 1A",   # Invalid: Wrong format
    "AA1 1A",    # Invalid: Wrong format
]

# Test the regex
for postcode in test_cases:
    result = "Valid" if is_valid_uk_postcode(postcode) else "Invalid"
    print(f"{postcode}: {result}")
