from  backend.auth import verify_password
from backend.log_activity import log_activity
from backend.alert import trigger_alert

user_input=input("enter password:")
if verify_password(user_input):
    print("Access Granted")
    log_activity(user_input,"granted")
else:
    print("Access denied")
    log_activity(user_input,"denied")
    trigger_alert()   
     