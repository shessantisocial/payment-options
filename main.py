print("How much is your total purchase?")
reply = float(input())

print("Choose your payment option:\nA. Cash payment\nB. Bank transfer")
response = str(input(">> ")).upper()
if response == "A":
    deposit = float(input("How much are you depositing?\n>> "))
    change = deposit - reply
    print(change)
elif response == "B":
    confirmation = str(input("Please hold on while we confirm your bank transfer"))
    print("Your payment transfer has been confirmed. Your account has successfully been debited.")
else:
    print("Invalid payment choice. Please try again")