import datetime
import hashlib
# Hardecoded hashed password for demo
# you can use SHA_256 to store hashed password securely
stored_password_hash=hashlib.sha256("secure123".encode()).hexdigest()
def verify_login(input_password):
    input_hash=hashlib.sha256(input_password.encode()).hexdigest()
    if input_hash==stored_password_hash:
      print("login successful!")
      return True
    else:
       print("invalid password.Try again.")
       return False
def login_activity(user_input,status):
    with open("activity_log.txt","a") as log_file:
       log_file.write(f"{datetime.datatime.now()}-Attempt:{user_input}-{status}\n")
def login_activity(user_input,status):
   with open("activity_log.txt","a") as file:
      file.write(f"User_Input: {user_input} | {status}\n")
def login_system(password):
   correct_password="1234"
   return password==correct_password     
          
          
    
