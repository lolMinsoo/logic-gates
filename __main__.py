import math
import random as rand
import sys


characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_!@#$%^&*()_+"

def binary_check(binary_code):
	check = set(binary_code)
	binary_check = {'0', '1'}
	
	if check == binary_check or binary_check == {'0'} or binary_check == {'1'}:
		print("Input good: " + binary_code)
	else:
		print("Invalid binary entered")
		exit()	

def randomCharacter():
	return characters[math.floor(rand.random() * len(characters))] 

def create_seeds():
	same_character_check = ""
	
	binary_code = input("Binary to random AND: ")

	binary_check(binary_code)
		
	s1 = ""
	s2 = ""
	for it in binary_code:
		if it == "0":
			s1 = s1 + randomCharacter()
			same_character_check = randomCharacter()
			while(s1[-1] == same_character_check[-1]):
				same_character_check = randomCharacter()
			s2 = s2 + same_character_check
		else:
			same_character_check = randomCharacter()
			s1 = s1 + same_character_check
			s2 = s2 + same_character_check
		
	return ("s1 = "+s1, "s2 = "+s2)
	
def andgate():
	s3 = input("AND 1: ")
	s4 = input("AND 2: ")
	
	if len(s3) != len(s4):
		print("Lengths of two strings are not the same.")
		exit()
	decoded_binary = ""
	for index, it in enumerate(s3):
		if s3[index] == s4[index]:
			decoded_binary = decoded_binary + "1"
		else:
			decoded_binary = decoded_binary + "0"
	return decoded_binary

def xorgate():
	s3 = input("XOR 1: ")
	s4 = input("XOR 2: ")
	
	if len(s3) != len(s4):
		print("Lengths of two strings are not the same.")
		exit()
	
	decoded_binary = ""
	for index, it in enumerate(s3):
		if s3[index] == s4[index]:  #XOR same means 0 different means 1
			decoded_binary = decoded_binary + "0"
		else:
			decoded_binary = decoded_binary + "1"
	return decoded_binary
		
def createxorbinary():
	s3 = input("XOR 1: ")
	s4 = input("XOR 2: ")
	
	binary_check(s3)
	binary_check(s4)
	
	if len(s3) != len(s4):
		return "Lengths of two binaries are different"
	
	xor_binary = ""
	
	for index, it in enumerate(s3):
		if s3[index] == s4[index]:
			xor_binary = xor_binary + "0"
		else:
			xor_binary = xor_binary + "1"
	
	return "XOR Output: " + xor_binary
	
if '--createseeds' in sys.argv:
	print(create_seeds())
elif '--andgate' in sys.argv:
	print(andgate())
elif '--xorgate' in sys.argv:
	print(decoded_binary())
elif '--createxorbinary' in sys.argv:
	print(createxorbinary())