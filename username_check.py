import datetime

OUTPUT_FILE = "./username_validation_log.txt"
INPUT_FILE = "./test_usernames.txt"

def get_current_datetime_formatted():
    now = datetime.datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")

def is_valid_username(username):
    invalid_usernames = ["admin", "test", "user"]
    # Remove whitespace from start and end
    clean_username = username.strip()

    if clean_username in invalid_usernames:
        return False
    
    # For now, any non-empty username (after stripping) is valid
    return len(clean_username) >= 3

def check_username(username):
    is_valid = is_valid_username(username)
    
    # Log the check
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        result = "Valid" if is_valid else "Invalid"
        current_time = get_current_datetime_formatted()
        # Show both original and stripped version in log
        stripped_version = username.strip()
        f.write(f"{current_time} - Username: '{username}' --> '{stripped_version}' - {result}\n")
    
    return is_valid

def read_usernames_from_file(filename):
    with open(filename, "r") as f:
        return f.read()

# Read usernames from file and check each one
username_data = read_usernames_from_file(INPUT_FILE)
usernames = username_data.split("\n")

print("Checking usernames from file:")
for username in usernames:
    result = check_username(username)
    print(f"'{username}' --> {result}")