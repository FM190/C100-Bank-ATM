class ATM:
  def __init__(self, cardnumber, pin):
    self.cardnumber = cardnumber
    self.pin = pin

  def checkbalance(self):
    print("Alert! Current Balance: $200")

  def withdrawcash(self, amount):
    newAmount = 200-amount
    print("Alert! You withdrew: $" + str(amount))
    print("Alert! Remaining balance: $" + str(newAmount))
  
def main():
  name = input("HI! What is you name?")
  print("Nice to meet you," + name)
  cardnumber = input("Please type your card number: ")
  pin = input("Enter Pin/Code: ")
  newUser = ATM(cardnumber, pin)

  print("What would you like to do today?")
  print("1) Check Balance")
  print("2) Withdraw Cash")
  activity = int(input("Please type your choice:"))

  if (activity == 1):
    newUser.checkbalance()
  elif (activity == 2):
    amount = int(input("Enter amount: "))
    newUser.withdrawcash(amount)
  else:
    print("Please double check and enter a valid number.")

if __name__ == "__main__":
  main()