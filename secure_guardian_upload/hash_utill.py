import datetime
import hashlib
def hash_password(password:str)->str:
    return hashlib.sha256(password.encode()).hexdigest()
STORED_HASH_PASSWORD=hashlib.sha256("gurdian123".encode()).hexadigest()
# create a function to get input and verfiy password
def verify_password():
    entered_password=input("enter the password to access:")
    hashed_input=hashlib.sha256(entered_password.encode()).hexadigest()
    if hashed_input==STORED_HASH_PASSWORD:
        print("Access Granted")
        return True
    else:
        print("Access Denied")
        trigger_alert()
        return False
    # Trigger an alert if password is wrong
def trigger_alert():
    trusted_contanct_name="mom"
    trusted_contanct_phone="xxxxxxxxxx"
    message=f"""
    ALERT:unauthorized access attempt is detected!
    TIME:{datetime.datetime.now()}
    NOTIFY:{trusted_contanct_name}  at {trusted_contanct_phone}
    """
    with open ("alert_log.txt","a") as alert_file:
        alert_file.write(message)
    print(message)    





        