import random
chars = "Aa&@0123456789"
while 1:
	print("BY : </> DARK WEB")
	password_len=int(input("Enter Password Lenth (3,4,8):"))
	password_count=int( input ("Enter Number Password To Generate 1000  : "))
	for x in range(password_count) :
			password = ""
			for x in range(password_len) :
				password_char=random.choice(chars)
				password=password+password_char
				print(password)