''' ----BANK MANAGEMENT SYSTEM-----
    1. opening new account(current/saving account)
    2. deposit amount
    3. withdraw amount
    4. balance enquiry
    5. all account holders list
    6. close bank account
    7.modify bank account '''


import mysql.connector as msc

bank_database = msc.connect(
    host= "localhost",
    user= "root",
    password= "SireshM@123"
)

cursor = bank_database.cursor()

''' creating the database. once you create a database, comment the line to run a program for next time.'''
# cursor.execute("CREATE DATABASE BANKDATA")

cursor.execute("USE BANKDATA")
''' creating the table. once you create a table, comment the line to run a program for next time.'''
# create_data = "CREATE TABLE CUSTOMER (ACCOUNTNUMBER INT AUTO_INCREMENT, ACCOUNTTYPE VARCHAR(30), NAME VARCHAR(200), BALANCE INT, MOBILE INT, GENDER VARCHAR(50), PRIMARY KEY(ACCOUNTNUMBER))"
# cursor.execute(create_data)

print("-"*60)
print("*"*10,"Welcome to Smart Bank-Your Bank Your Choice","*"*10)
print("-"*60)

class bank():
    def __init__(self,operation):
        self.operation = operation

    def select(self):

        if self.operation == 1:

                account_type = input("select the account type (sb for savings or ca for current):")
                number = cursor.execute("SELECT * FROM CUSTOMER ORDER BY ACCOUNTNUMBER DESC LIMIT 1")    #to fetch the last account number from database
                account_number = cursor.fetchone()[0]
                account_number+=1   #increment the account number to get consecutive number
                balance = 0 
                

                if account_type == "sb":
                    name = input("enter your name: ")
                    mobile_number = int(input("enter your mobile number: "))
                    gender = input("enter gender male/female: ")
                    intial_amount = int(input("enter the initial deposit amount(more than or equal to 500): "))
                    balance += intial_amount
                    print("your savings account has been created successfully and your account number is ", account_number)
                    entry = "INSERT INTO CUSTOMER (ACCOUNTNUMBER, ACCOUNTTYPE, NAME, BALANCE, MOBILE, GENDER) VALUES (%s, %s, %s, %s, %s, %s)"
                    values = (account_number, account_type, name, balance, mobile_number, gender)
                    cursor.execute(entry,values)
                    bank_database.commit()
                    

                elif account_type == "ca":
                    name = input("enter your name: ")
                    mobile_number = int(input("enter your mobile number: "))
                    gender = input("enter your gender: ")
                    intial_amount = int(input("enter the initial deposit amount(more than or equal to 1000): "))
                    balance += intial_amount
                    print("your current account has been created successfully and your account number is ", account_number)
                    entry = "INSERT INTO CUSTOMER (ACCOUNTNUMBER, ACCOUNTTYPE, NAME, BALANCE, MOBILE, GENDER) VALUES (%s, %s, %s, %s, %s, %s)"
                    values = (account_number, account_type, name, balance, mobile_number, gender)
                    cursor.execute(entry,values)
                    bank_database.commit()
                    
                else:    
                    print("invalid, please try again. ")


        elif self.operation == 2:

            account_type = input("please enter the type of account sb/ca : ")
            account_number = (int(input("please enter the account number: ")), )    #assign the variable accountnumber in a tuple form to concatenate to the sql query 
            balance_fetch = "SELECT BALANCE FROM CUSTOMER WHERE ACCOUNTNUMBER = %s"
            bal = cursor.execute(balance_fetch,account_number)
            balance = cursor.fetchone()[0]
            amount = int(input("please enter the amount to deposit: "))
            balance += amount
            entry = "UPDATE CUSTOMER SET BALANCE = %s WHERE ACCOUNTNUMBER = %s"
            values = (balance, account_number[0])
            cursor.execute(entry, values)
            bank_database.commit()
            print("amount deposited successfully. Available balance is ", balance)

            
        elif self.operation == 3:
             
            account_type = input("please enter the type of account sb/ca : ")
            account_number = (input("please enter the account number: "), )
            balance_fetch = "SELECT BALANCE FROM CUSTOMER WHERE ACCOUNTNUMBER = %s"
            bal = cursor.execute(balance_fetch,account_number)
            balance = cursor.fetchone()[0]
            amount = int(input("please enter the amount to withdrawl: "))
            balance -= amount
            entry = "UPDATE CUSTOMER SET BALANCE = %s WHERE ACCOUNTNUMBER = %s"
            values = (balance, account_number[0])
            cursor.execute(entry, values)
            bank_database.commit()
            print("amount debited successfully. Avaialable balance is ", balance)

        elif self.operation == 4:
             
            account_type = input("please enter the type of account sb/ca : ")
            account_number = (input("please enter the account number: "), )
            balance_fetch = "SELECT BALANCE FROM CUSTOMER WHERE ACCOUNTNUMBER = %s"
            bal = cursor.execute(balance_fetch,account_number)
            balance = cursor.fetchone()[0]
            bank_database.commit()
            print("Available Balance is ", balance)



        elif self.operation == 5:
             
            print("ACCOUNTNUMBER", "ACCOUNTTYPE", "NAME", "BALANCE", "MOBILENO", "GENDER")
            cursor.execute("SELECT * FROM CUSTOMER")
            my_list = cursor.fetchall()
            for i in my_list:
                 print(i)

        elif self.operation == 6:
             
            account_type = input("please enter the type of account sb/ca : ")
            account_number = (input("please enter the account number: "), )
            entry = "DELETE FROM CUSTOMER WHERE ACCOUNTNUMBER = %s "
            cursor.execute(entry,account_number)
            bank_database.commit()
            print("your {} account number {} has been closed successfully.".format(account_type, account_number[0]))

        elif self.operation == 7:
             
            account_type = input("please enter the type of account sb/ca : ")
            account_number = (input("please enter the account number: "), )
            edit_option = int(input("please enter choice 1.edit name 2.edit mobile number 3.edit gender: "))
            
            if edit_option == 1:
                 edit_name = (input("please enter the modified name: "), )
                 entry = "UPDATE CUSTOMER SET NAME = %s WHERE ACCOUNTNUMBER = %s"
                 values = (edit_name[0],account_number[0])
                 cursor.execute(entry,values)
                 bank_database.commit()
                 print("Your name has been modified successfully.")
            elif edit_option == 2:
                 edit_mobile = (input("please enter the mobile number to be modified: "), )
                 entry = "UPDATE CUSTOMER SET MOBILE = %s WHERE ACCOUNTNUMBER = %s"
                 values = (edit_mobile[0],account_number[0])
                 cursor.execute(entry,values)
                 bank_database.commit()
                 print("Your mobile number has been modified successfully.")
            elif edit_option == 3:
                 edit_gender = (input("please enter gender to be modified: "), )
                 entry = "UPDATE CUSTOMER SET GENDER = %s WHERE ACCOUNTNUMBER = %s"
                 values = (edit_gender[0],account_number[0])
                 cursor.execute(entry,values)
                 bank_database.commit()
                 print("Your gender has been modified successfully. ")
            else:
                 print("invalid,please enter valid option.")


        else:
             print("invalid, please enter correct choice: ")



    
obj_1= bank(int(input("please enter your choice 1.open account 2.deposit 3.withdrawl 4.balance enquiry 5.all account holders list 6.close account 7.modify account: ")))
obj_1.select()

print("-"*10, "Thank You for choosing Smart Bank", "-"*10)












