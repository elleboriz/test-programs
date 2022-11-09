balance = 0
currency = '$'
passcode = "0000"
print("Welcome to MyATM. ")
for i in range(1,4):
      code = input("Enter your PIN: ")
      i = 3 -i
      if code != passcode:
            print(f"you have {i} try left")
            if i == 0:
                  print("Too many incorrect passwords,Your account has been blocked"
                        " \nContact client support")
            else:continue
      else:
            print("Which transaction do you want make"
                  "\n1)Deposit\n2)Withdraw\n3)Consult my balace ")
            trasaction = int(input("-->: "))

            while trasaction in range(1,4):
                  if trasaction == 3:
                        print(f"Your balance is {balance}{currency}")
                        break
                  elif trasaction == 2:
                        w_amnt = int(input("How much do you want to withdraw?: "))
                        if w_amnt > balance:
                              print("You don't have sufficient balance")
                              break
                        else:
                            print(balance - w_amnt)
                            break
                  elif trasaction == 1:
                        dp_amnt = int(input("Enter amount you want to deposit: "))
                        balance = balance + dp_amnt
                        print(f"You have successfully deposited {dp_amnt}{currency}")
                        break
            else:print("Error!!Choose the opreation you want to perform amongs the following"
                       "\n1)Deposit\n2)Withdraw\n3)Consult my balace")
      break
print("Thanks for using MyATM ")
