import os
import math
import random
import smtplib

digits = "0123456789"
OTP = "".join(digits[math.floor(random.random() * 10)] for _ in range(6))
otp = f"{OTP} is your OTP"
msg = otp

s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()

# gmail account and password that send the opt code to user gmail
s.login("Your Gmail Account", "You app password")

emailid = input("Enter your email: ")
s.sendmail("&&&&&&&&&&&", emailid, msg)

a = input("Enter Your OTP >>: ")
# verify the code
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")
