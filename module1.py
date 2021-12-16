#def Kolmnurga_pindala(külg:float,kõrgus:float):
#	"""Leiab kolmnurga pindalat. On antud kõrgus ja külje pikkus.Tagastab S float formaadis
#	:param float külg:Kolmnurga külje pikkus
##	:param float kõrgus:Kõrgus vasta küljele
#	:rtype:var
##	"""
#	if külg<0 or kõrgus<0:
#		S="valed andmed!"
#	else:
#		S=0,5*külg*kõrgus
#	return S 


#def arithmetic(a:float,b:float,tehe:str):
	#"""Liitmine , lahutamine, korrutamine ja jagamine.Tagastab arv, kui vastus on arv ja "Tundmatu tehe",kui ei saa vastuat  #  #leida või sisestatud teh ei ole ["+","-","*","/"].
#	:param float a:Esimine arv 
#	:param float b:Teine arv 
#	:param str tehe :Aritmeetilise tehe 
#	:rtype:var	
#	"""
#	if tehe in ["+","-","*","/"]:
#		if tehe=="/" and b==0:
#			vastus="Div/0"
#		else:
#			vastus=eval(str(a)+tehe+str(b))
#	else:
#		vastus="Tundmatu tehe!"
#	return vastus

#from math import *

#def square(side:float):
	#"""gives the P,S and diagonaal
	#:param float side:One and only side of a square
	#:rtype:var
	#"""
	#d=side*sqrt(2)
	#P=side*4
	#S=side*side
	#print(f"Diagonal {d}")
	#print(f"Perimetr {P}")
	#print(f"Ploshad {S}")

def season(month:int):
	"""tells which season month belongs to
	:param int month: number of the month
	:rtype:var
	"""
	if month>=1 and month<=12:
		if month in [12,1,2]:
			print("winter")
		elif month in [3,4,5]:
			print("spring")
		elif month in [6,7,8]:
			print("summer")
		elif month in [9,10,11]:
			print("autumn")
		else:
			print("there is only 12 months!")
		

def bank(euro:float,years:int):
	"""s4itaet skolko euro u tebja budet posle dannogo koli4estva mesjatsev
	:param float euro:amount of money u got
	:param int years:amount of years that passed
	:rtype:var
	"""
	m=euro*(0.1*years)
	d=euro+m
	print(d)

def is_prime(a:int)->bool:
	"""govorit prostoe 4islo ili net
	:param float a:vvedenoe 4islo
	:rtype:var
	"""
	v=0
	for i in range(1,a+1):
		if a%i==0:
			v+=1
	if v==2:
		v=True
	else:
		v=False
	return v

