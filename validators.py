from datetime import datetime

def is_valid_date(value):
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def valid_status(value):
    return value.strip().upper() in {"P", "F", "N"}
