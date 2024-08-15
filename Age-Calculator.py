from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year

    # Check if the birthday has occurred yet this year
    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        age -= 1

    return age

def get_birthdate():
    # Get user input for birthdate
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        return birthdate
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None

def main():
    birthdate = get_birthdate()
    if birthdate:
        age = calculate_age(birthdate)
        print(f"You are {age} years old.")

if __name__ == "__main__":
    main()
