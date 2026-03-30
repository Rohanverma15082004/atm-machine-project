mini_Project="STRING PROJECT"
print(mini_Project.center(60,"-"))

print()
program="Program Number [1]:"
print(program)
print()

a="___________ATM_MACHINE_PROJECT__________"
print(a.center(60))

balance=float(input("enter amount :"))
print('''
[i].Check balance For Press '1' :
[ii].Deposit For Press '2' :
[iii].Withdraw For Press '3' :
[iv].Exit For Press '4' :''')



while True:
	
	choice=int(input("enter your choice :"))
	if choice==1:
		print(f"your balance,{balance}")
	elif choice==2:
		user_ask=input("do you want deposit").lower()
		if user_ask=="yes":
			deposit=float(input("enter deposit amount :"))
			balance+=deposit
			print(f"Deposit successful! Total balance: {balance}")
		else:
			print(f"your balance :{balance}")

	elif choice==3:
		user=input("do you want withdraw :").lower()
		if user=="yes":
			withdrawal=float(input("enter withdrawal amount :"))
			if  withdrawal<=balance:
				balance-=withdrawal
				print(f"withdrawal  successful ,remaining_Balance : {balance}")
			else:
				print(f"insufficient balance :{balance}")
			
		else:
			print("Transaction cancelled")
			
	elif choice==4:
		print(f"Thank you for using ATM!")
		break
	else:
		print(f"invalid choice")
	repeat=input("do you want repeat (yes/No) :").lower()
	if repeat=="no":
		break


