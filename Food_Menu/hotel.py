print("welcome to Navgurukul campus")
name=('''
	a)Breakfast
	b)Lunce
	c)Dinner
	''')
print('''
	a)Breakfast
	b)Lunce
	c)Dinner
	''')
i=10
n=0

while True: 
	meal=input("enter your choice menu :")
	if meal=="a":
		print('''
			BREAKFAST MENU:-

			a)Poha
			b)Tea
			c)Coffie
			d)macroni
			e)Aloo parata
			f)Paw bhaji
			g)Momo
			''')
		c=input("inter your choice:")
		if c=="a":
			print("Price is Rs.10")
		elif c=="b":
			print("Price is Rs.10")
		elif c=="c":
			print("Price is Rs.20")
		elif c=="d":
			print("Price is Rs.50")
		elif c=="e":
			print("Price is Rs.80")
		elif c=="f":
			print("Price is Rs.30")
		elif c=="g":
			print("Price is Rs.60")

		elif c=="back":
			print(name)
			i-=1
		else:
			print("Sorry this is not heire")
		al=input("aap our kuch lena chaonge yes/no\n")
		if al=="yes":
			print(name)
		elif al=="no":
			print("Thanks for visit")
			break
	elif meal=="b":
		print('''
			a)Dal Rice
			b)Rajma Rice+Rayta
			c)Butter paneer+Rice
			d)Sinple Dal Roti
			''')
		x=input("enter your choice: ")
		if x=="a":
			print("Price is Rs.120")
		elif x=="b":
			print("Price is Rs.150")
		elif x=="c":
			print("Price is Rs.200")
		elif x=="d":
			print("Price is Rs.80")
		elif x=="back":
			print(name)
			i+=1
		al=input("aap our kuch lena chaonge yes/no\n")
		if al=="yes":
			print(name)
		elif al=="no":
			print("Thanks for visit")
			break
		else:
			print("Sorry this is not heire")
	elif meal=="c":
		print("""
			a)Chiken Roti
			b)Mattan kadi
			c)Panir
			d)Fish fry
			e)Anda Kadi
			f)Matan Roti
			g)chiken Roti
			""")
		xx=input("enter your choice: ")
		if xx=="a":
			print("Price is Rs.200 plate")
		elif xx=="b":
			print("Price is Rs.180 plate")
		elif xx=="c":
			print("Price is Rs.140 plate")
		elif xx=="d":
			print("Price is Rs.40 per pice")
		elif xx=="e":
			print("Price is Rs.80. 2 ege ")
		elif xx=="f":
			print("Price is Rs.220")
		elif xx=="g":
			print("Price is Rs.160")
		elif xx=="back":
			print(name)
			i-=1
		elif xx=="h":
			break
		al=input("aap our kuch lena chaonge yes/no\n")
		if al=="yes":
			print(name)
		elif al=="no":
			print("Thanks for visit")
			break

		else:
			print("not heire")
	n+=1