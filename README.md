# PassStr: Password Leak Checker

**PassStr** is a Python-based tool that checks if a given password is part of a known leaked password dataset and evaluates its strength. It provides feedback to help users create stronger, safer passwords.

---

## Features

### Password Leak Detection
- Verifies if the password’s SHA-1 hash is present in a sorted file of leaked passwords (`Password_Hashes`) using binary search.

### Password Strength Assessment
- Evaluates the password’s strength based on:
  - **Length**: Scores higher for passwords 8 characters or longer.
  - **Uppercase Letters**: Checks for the presence of at least one uppercase letter.
  - **Lowercase Letters**: Checks for the presence of at least one lowercase letter.
  - **Digits**: Ensures the inclusion of numeric characters.
  - **Special Characters**: Looks for symbols like `@`, `#`, `$`, etc.

### Efficient Search Algorithm
- Utilizes binary search for quick detection in large datasets of leaked passwords.

### Password Dataset Included
- The repository includes a comprehensive dataset of leaked passwords named `Password_Hashes`, which contains entries compiled from various breaches. The following files are part of the dataset:
  - `10k-most-common.txt`
  - `10-million-password-list-top-1000000 (1).txt`
  - `100k-most-used-passwords-NCSC.txt`
  - `1900-2020.txt`
  - `bt4-password.txt`
  - `common_corporate_passwords.txt`
  - `common-passwords-win.txt`
  - `darkc0de.txt`
  - `days.txt`
  - `medical-devices.txt`
  - `months.txt`
  - `Most-Popular-Letter-Passes.txt`
  - `mssql-passwords-nansh0u-guardicore.txt`
  - `openwall.net-all.txt`
  - `probable-v2-top12000.txt`
  - `rockyou.txt`
  - `scraped-JWT-secrets.txt`
  - `seasons.txt`
  - `unkown-azul.txt`
  - `UserPassCombo-Jay.txt`
  - `xato-net-10-million-passwords.txt`

---

## Installation

### Prerequisites
- Python 3.7 or higher

### Steps
1. Clone or download this repository.
2. Ensure the `Password_Hashes` folder with the above files exists in the same directory as the script.
3. Generate a sorted file of SHA-1 hashes from the dataset using a provided script or hashing tool.
4. Place the generated `Password_Hashes` file in the same directory as the script.
5. Run the program using:
   ```bash
   python PassStr.py
   ```

---

## Usage

1. Run the script:
   ```bash
   python PassStr.py
   ```
2. Enter the password to check when prompted.
3. The program will:
   - Indicate if the password is leaked or safe.
   - Assess the password’s strength and display feedback.

### Example

#### Input:
```plaintext
Enter the password to check: password123
```
#### Output:
```plaintext
❌ Password is already leaked (Not Safe).
```

#### Input:
```plaintext
Enter the password to check: My$tr0ngP@ssword
```
#### Output:
```plaintext
✅ Password not leaked (Safe).
Password Strength: Very Strong
```

---

## How It Works

1. **Password Hashing**: The entered password is hashed using SHA-1.
2. **Leak Detection**: The hashed password is checked against a pre-sorted list of leaked SHA-1 hashes using binary search.
3. **Strength Assessment**:
   - The password’s strength is calculated based on its length, complexity, and character variety.
   - The program provides feedback on the strength level.


---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Disclaimer

This tool is for educational purposes only. Do not use it for malicious or illegal activities.

