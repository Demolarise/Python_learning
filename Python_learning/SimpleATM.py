correct_pin = "1234"
attempts = 0

while attempts < 3:
    user_input = input("please enter your PIN: ")
    if correct_pin == user_input:
        print("Access Granted! You're welcome!!")
        break
    else:
        attempts += 1
        rem = 3 - attempts
        if rem > 0:
         print(f"PIN incorrect, you have {rem} attempts left")
if attempts == 3:
        print("Account Locked! Please contact your bank.")
