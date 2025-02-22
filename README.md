# Age Calculator

## Description
This is a simple Python program that calculates a user's age based on their birthdate. The user inputs their birthdate in the format **YYYY-MM-DD**, and the program determines their age by comparing it with the current date.

## Features
- Accepts user input for birthdate.
- Validates the input format (**YYYY-MM-DD**).
- Ensures that the birthdate is not in the future.
- Calculates and displays the correct age.
- Handles incorrect inputs gracefully.

## Prerequisites
- Python 3.x installed on your system.

## Installation
1. Clone this repository or download the `age_calculator.py` file.
2. Ensure Python is installed by running:
   ```sh
   python --version
   ```
3. Navigate to the directory where the script is saved.

## Usage
1. Open a terminal or command prompt.
2. Run the script using:
   ```sh
   python age_calculator.py
   ```
3. Enter your birthdate when prompted (format: `YYYY-MM-DD`).
4. The program will output your current age.

## Example
```
Enter your birthdate (YYYY-MM-DD): 2000-05-15
You are 24 years old.
```

## Error Handling
- If an incorrect format is entered, the program will prompt the user to try again.
- If the user enters a future date, an error message will appear.
