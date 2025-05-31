import hashlib
import datetime
from backend.auth import verify_password
stored_hashed_password=hashlib.sha256("secure123".encode()).hexdigest()
def verify_password():
    entered_password=input("entered_password:")
    hashed_input=hashlib.sha256(entered_password.encode()).hexadigest()
    pass
    if hashed_input==stored_hashed_password:
        print("Access Granted")
        log_activity(entered_password,"granted")
        return True
    else:
        print("Access Denied")
        trigger_alert()
        log_activity(entered_password,"denied")
        return False
def trigger_alert():
    print("Alert : unauthorized acess attempt detected!")  
def log_activity(password_input,status):
    now=datetime.datetime.now()
    with open("activity_log.txt","a") as file:
        file.write(f"[{now}]password:{password_input}-status:{status}\n")

if _name_ == "_main_":
    verify_password()
            
    