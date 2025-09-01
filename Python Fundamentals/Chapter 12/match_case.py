# Function to return message based on HTTP status code
def http_status(status):
    # Using 'match-case' (introduced in Python 3.10) for pattern matching
    match status:
        case 200:   # If status is 200
            return "OK"   # Return success message
        case 404:   # If status is 404
            return "Not Found"   # Return not found message
        case 500:   # If status is 500
            return "Internal Server Error"   # Return server error message
        case _:     # Default case (like 'else' in if-else)
            return "Unknown status"   # Return this if no case matches

# Usage examples
print(http_status(200))  # Output: OK
print(http_status(404))  # Output: Not Found
print(http_status(500))  # Output: Internal Server Error
print(http_status(403))  # Output: Unknown status (because 403 is not matched above)
