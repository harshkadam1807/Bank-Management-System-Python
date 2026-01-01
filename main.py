import json 
import random
import string 
from pathlib import Path 

class Bank:
    database = 'data.json'
    data = []
    
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exist ")
    except Exception as error:
        print(f"an exception occured as {error}")
    
    @classmethod
    def __updating(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgeneration(cls):
        letters = random.choices(string.ascii_letters,k = 3)
        numbers = random.choices(string.digits,k= 2)
        splchar = random.choices("!@#$%^&*",k = 1)
        acnum = letters + numbers + splchar
        random.shuffle(acnum)
        return "".join(acnum)

    
    def Createaccount(self):
        information = {
            "name": input("Enter your name: "),
            "age" : int(input("Enter your age: ")),
            "email": input("Enter your email: "),
            "pin": int(input("Enter your 4 digits pin: ")),
            "accountNo." : Bank.__accountgeneration(),
            "balance" : 0
        }
        if information['age'] < 18  or len(str(information['pin'])) != 4:
            print("Sorry you cannot create your account")
        else:
            print("Your Account has been successfully created")
            for i in information:
                print(f"{i} : {information[i]}")
            print("Please verify your account number")

            Bank.data.append(information)
            Bank.__updating()
        

    def depositmoney(self):
        accnum = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("Sorry, no data found")
        
        else:
            amount = int(input("Enter amount you want to deposit: "))
            if amount  > 10000 or amount < 0:
                print("Sorry the amount your enter is too much, you can deposit above 0 and below 10000")

            else:
                userdata[0]['balance'] += amount
                Bank.__updating()
                print("Amount deposited successfully ")


    def withdrawmoney(self):
        accnum = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("Sorry, no data found")
        
        else:
            amount = int(input("Enter amount you want to withdraw: "))
            if userdata[0]['balance']  < amount:
                print("Sorry you dont have that much amount to withdraw")
            else:
                userdata[0]['balance'] -= amount
                Bank.__updating()
                print("Your Amount has been Successfully withdrawn")
                
                
    def showdetails(self):
        accnum = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnum and i['pin'] == pin]
        print("Your Bank Acccount details are displayed below \n\n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")


    def updatedetails(self):
        accnum = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("Sorry, no data found")
        
        else:
            print("You can only update your name,email and pin and not account number,age and balanced")
            print("So,fill the new details for updating your data or leave empty if no changes needed")

            updated_data = {
                "name": input("Enter your new name or press enter to skip: "),
                "email":input("Enter your new email or press enter to skip: "),
                "pin": input("Enter your new pin or press enter to skip: ")
            }

            if updated_data["name"] == "":
                updated_data["name"] = userdata[0]['name']
            if updated_data["email"] == "":
                updated_data["email"] = userdata[0]['email']
            if updated_data["pin"] == "":
                updated_data["pin"] = userdata[0]['pin']
            
            updated_data['age'] = userdata[0]['age']
            updated_data['accountNo.'] = userdata[0]['accountNo.']
            updated_data['balance'] = userdata[0]['balance']
            
            if type(updated_data['pin']) == str:
                updated_data['pin'] = int(updated_data['pin'])
            

            for i in updated_data:
                 if updated_data[i] == userdata[0][i]:
                     continue
                 else:
                     userdata[0][i] = updated_data[i]

            Bank.__updating() 
            print("Your Bank details are updated Successfully")    


    def Delete(self):
        accnum = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnum and i['pin'] == pin]
        if userdata == False:
            print("Sorry, no data found")
        else:
            check = input("Do you really want to delete your account details: \nEnter Yes or No: ")
            if check.lower() == 'no':
                pass
            else:
                Bank.data.remove(userdata[0])
                print("Your Account has been deleted Successfully ")
                Bank.__updating()

user = Bank()

print("press 1 for creating an account: ")
print("press 2 for Depositing the money in the bank: ")
print("press 3 for withdrawing the money: ")
print("press 4 to see your account details: ")
print("press 5 for updating your details: ")
print("press 6 for deleting your account: ")

check = int(input("tell your choice: "))

if check == 1:
    user.Createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.Delete()

