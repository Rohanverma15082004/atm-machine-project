print("----------Functions----------")
def checkBalance(balance):
print(f"your balance is :{balance}")
def depositAmount(balance):
amt=float(input("enter deposit amount :"))
balance+=amt
print(f"Deposit successful! Total balance: {balance}")
return (balance)
def withdrawAmount(balance):
amount=float(input("enter withdrawal amount :"))
if  amount<=balance:
balance-=amount
print(f"Withdrawal successful! Remaining balance: {balance}")		
else:
print(f"insufficient balance :{balance}")
return (balance)

def verifyPin():
real_pin="1234"
pin=input("enter your pin :")
if pin==real_pin:
print("valid pin")
return True
else:
print("invalid pin")
return False

mini_Project="STRING PROJECT"
print(mini_Project.center(60,"-"))

print()
program="Program Number [1]:"
print(program)
print()

a="_ATM_MACHINE_PROJECT"
print(a.center(60))

balance=float(input("enter amount :"))
print()
print("""FEACTURES""")
print('''
[i].Check balance For Press '1' :
[ii].Deposit For Press '2' :
[iii].Withdraw For Press '3' :
[iv].Exit For Press '4' :''')

while True:

choice=int(input("enter your choice :"))    
if choice==1:    
	if verifyPin():    
		checkBalance(balance)    
elif choice==2:    
	balance=depositAmount(balance)    

elif choice==3:    
	if verifyPin():    
		balance=withdrawAmount(balance)    
	    
	    
		    
elif choice==4:    
	print(f"Thank you for using ATM!")    
	break    
else:    
	print(f"invalid choice")    
repeat=input("do you want repeat (yes/No) :").lower()    
if repeat=="no":    
	break


