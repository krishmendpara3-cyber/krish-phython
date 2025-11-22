
import re

# Function to validate an Indian Permanent Account Number (PAN)
# PAN format: 5 Uppercase Letters (AAAAA) + 4 Digits (9999) + 1 Uppercase Letter (A)
def validate_pan(pan):
    """
    Validates the format of an Indian PAN card number using a regular expression.
    """
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$' 
    if re.match(pattern, pan):
        return True
    return False
def validate_email(email):
    """
    Validates the format of an email address using a standard regular expression.
    """

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        return True
    return False

# --- Main execution block ---
if __name__ == "__main__":
    
    print("--- PAN Card Validation ---")
    pan_number = input("Enter PAN card number: ").strip().upper()
    if validate_pan(pan_number):
        print(f"'{pan_number}' is a VALID PAN card number.")
    else:
        print(f"'{pan_number}' is an INVALID PAN card number.")
        
    print("\n--- Email ID Validation ---")
    email_id = input("Enter email ID: ").strip() # Clean input
    if validate_email(email_id):
        print(f"'{email_id}' is a VALID email ID.")
    else:
        print(f"'{email_id}' is an INVALID email ID.")