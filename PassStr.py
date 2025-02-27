import hashlib
import re
import os

# Function to check password strength
def check_password_strength(password):
    score = 0

    # Check for length
    if len(password) >= 8:
        score += 1
    elif len(password) >= 6:
        score += 0.5

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1

    # Check for digits
    if re.search(r'\d', password):
        score += 1

    # Check for special characters
    if re.search(r'[\W_]', password):
        score += 1

    return score

# Function to assess password strength based on score
def assess_password_strength(score):
    if score > 4:
        return "Very Strong"
    elif score > 3:
        return "Strong"
    elif score > 2:
        return "Moderate"
    elif score > 1:
        return "Weak"
    else:
        return "Very Weak"

# Function for binary search in sorted file
def binary_search(file_path, target):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            left, right = 0, len(lines) - 1
            while left <= right:
                mid = (left + right) // 2
                current = lines[mid].strip()
                if current == target:
                    return True
                elif current < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

# Main program
if __name__ == "__main__":
    # Local file path
    file_path = "Password_Hashes.txt"

    # Prompt user for input
    password = input("Enter the password to check: ").strip()

    # Hash the password using SHA-1
    hashed_password = hashlib.sha1(password.encode()).hexdigest()

    # Check if the file exists
    if os.path.exists(file_path):
        # Perform binary search in the sorted file
        is_leaked = binary_search(file_path, hashed_password)
        if is_leaked is True:
            print("❌ Password is already leaked (Not Safe).")
            exit()  # Exit the program if the password is leaked
        elif is_leaked is None:
            print("⚠️ Skipping leak check due to file error.")
        else:
            print("✅ Password not leaked (Safe).")
    else:
        print(f"⚠️ File '{file_path}' not found. Skipping leak check.")

    # Check the score of password strength
    score = check_password_strength(password)

    # Assess and print password strength
    strength = assess_password_strength(score)
    print(f"Password Strength: {strength}")
