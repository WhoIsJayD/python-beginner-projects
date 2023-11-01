# create a timer

# from time module import sleep
from time import sleep

# get the duration from user
duration = int(input("Enter the duration in seconds: "))

# This loop run until the test condition is false
for count in range(duration):
    # prints the current duration
    print(count, end="\r")
    # sleep for 1 second
    sleep(1)
# prints if the time is up
print("Your time is up!")
