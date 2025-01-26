# PassStr: Password Leak Checker

**PassStr** is a Python-based tool that checks if a given password is part of a known leaked password dataset and evaluates its strength. It provides feedback to help users create stronger, safer passwords.

---

## Features

### 🔒 Password Leak Detection
- Verifies if the password’s **SHA-1 hash** is present in a sorted file of leaked passwords (`Password_Hashes.txt`) using binary search.

### 📊 Password Strength Assessment
- Evaluates password strength based on:
  - **Length**: Scores higher for passwords 8 characters or longer.
  - **Uppercase Letters**: Checks for the presence of at least one uppercase letter.
  - **Lowercase Letters**: Checks for the presence of at least one lowercase letter.
  - **Digits**: Ensures the inclusion of numeric characters.
  - **Special Characters**: Looks for symbols like `@`, `#`, `$`, etc.

### ⚡ Efficient Search Algorithm
- Utilizes **binary search** for quick detection in large datasets of leaked passwords.

---

## Included Password Dataset

The repository includes a **comprehensive dataset** of leaked passwords in **SHA-1 hash** format. The following files are part of the dataset:

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

The full dataset is available as a single file: [`Password_Hashes.txt`](https://drive.google.com/file/d/1BJGlnfY-mxGxUYHdx_apUZFAZ4eA3lzb/view?usp=sharing). Download this file and place it in the **same directory as the script** before running the program.

---

## Installation

### Prerequisites
- Python 3.7 or higher

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/basimnawaz6/PassStr.git
   cd PassStr
   ```
2. Download the [`Password_Hashes.txt`](https://drive.google.com/file/d/1BJGlnfY-mxGxUYHdx_apUZFAZ4eA3lzb/view?usp=sharing) file and place it in the **same folder** as the script.
3. Run the program:
   ```bash
   python PassStr.py
   ```

---

## Usage

### Running the Program
1. Run the script:
   ```bash
   python PassStr.py
   ```
2. Enter the password to check when prompted.

### Output
The program will:
1. Indicate if the password is leaked or safe.
2. If safe, assess the password's strength and provide feedback.

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

1. **Password Hashing**:
   - The entered password is hashed using **SHA-1**.
2. **Leak Detection**:
   - The hashed password is checked against a pre-sorted list of leaked SHA-1 hashes using **binary search**.
3. **Strength Assessment**:
   - The password’s strength is calculated based on its length, complexity, and character variety.
   - Feedback on strength is displayed to the user.

---

## License
This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## Disclaimer
This tool is for **educational purposes only**. Do not use it for malicious or illegal activities.
```

---

### Key Changes Made:
1. **Organized Structure**: Used headings, subheadings, and emojis for a more structured and visually appealing layout.
2. **Simplified Instructions**: Clarified how to download and place `Password_Hashes.txt`.
3. **Improved Examples**: Added formatted input and output examples.
4. **Consistent Formatting**: Unified the style of bullet points and code snippets.

This version is clean, professional, and easy to follow. Let me know if you need further adjustments!
