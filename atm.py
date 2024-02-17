class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        # Implement deposit functionality 
        self.balance = self.balance + int(amount)
        self.transaction_history.append("Deposited money:"+str(amount))
        print("Deposited money",amount)
        

    def withdraw(self, amount):
        # Implement withdraw functionality
        if self.balance == 0 :
            print("Balance is zero can not be withdraw")
            
        elif self.balance < amount :
            print("Available balance is withdraw amount")
        else:
            self.balance = self.balance - int(amount)
            self.transaction_history.append("Withdrawn money :"+str(amount))
            print("Withdrawn money",amount)

    def transfer(self, recipient, amount):
        # Implement transfer functionality
        if self.balance >= int(amount):
            self.balance = (self.balance - int(amount))
            recipient.balance = (recipient.balance + int(amount))
            self.transaction_history.append("Transfer ammount:"+amount)
            recipient.history.append("Added money!")
            
        else :
            print("Insufficient balance in account.")
            
        
        

    def display_transaction_history(self):
        # Implement displaying transaction history
        print("Your transaction history is :",self.transaction_history)   
    

class ATM:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.user_id] = user

    def authenticate_user(self, user_id, pin):
        user = self.users.get(user_id)
        if user and user.pin == pin:
            return user
        else:
            print("Authentication failed. Please check your user ID and PIN.")
            return None

    def start_atm(self, user):
        while True:
            print("\nATM Menu:")
            print("1. Transactions History")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Quit")

            choice = input("Enter your choice (1-5): ")
            
            if choice == "1" :
                user.display_transaction_history()
                
            elif choice == "2" :
                self.withdraw_menu(user)
                
            elif choice == "3" :
                self.deposit_menu(user)
                
            elif choice == "4" :
                self.transfer_menu(user)
                
            elif choice == "5" :
                self.quit_atm
                break

            else :
                print("Invalid choice. Please enter a number between 1 and 5.")

    def withdraw_menu(self,user):
        #Implement the withdraw functionality
        amount=input("Enter the amount of withdraw :")
        user.withdraw(amount)

    def deposit_menu(self,user):
        #Implement the deposit functionality
        amount=input("Enter the amount to deposit :")
        user.deposit(amount)

    def transfer_menu(self,fromUser):
        # Implement the transfer functionality
        transferToUserId=input("Enter the user id of account to transfer:")
        toUser = self.users.get(transferToUserId)
        if toUser :
            amount=input("Enter amount to transfer:")
            fromUser.transfer(toUser,amount)
        else:
            print(transferToUserId,"Is not exits.")
        
            
        
        

    def quit_atm(self):
        print("Thank you for using the ATM. Goodbye!")
        # Optionally, you may want to save user data or perform other cleanup tasks
        exit()

# Example usage:
atm_instance = ATM()
user_instance = User(user_id="111", pin="6789")
user1 = User(user_id="222",pin="7777")
atm_instance.add_user(user1)
atm_instance.add_user(user_instance)

authenticated_user = atm_instance.authenticate_user(user_id="222", pin="7777")

if authenticated_user:
    atm_instance.start_atm(authenticated_user)
