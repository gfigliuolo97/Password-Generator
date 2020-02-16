import sys
import string
import random

lower = string.ascii_lowercase
upper = string.ascii_uppercase
punc = string.punctuation
digits = string.digits

def random_psw(lower_num, upper_num, punc_num, digits_num):
	psw = ""
	for i in range(lower_num):				#generates certain number of lowercase characters
		psw += random.choice(lower)			

	for i in range(upper_num):				#generates certain number of uppercase characters
		psw += random.choice(upper)			

	for i in range(punc_num):				#generates certain number of punctuation characters
		psw += random.choice(punc)			

	for i in range(digits_num):				#generates certain number of digits
		psw += random.choice(digits)

	#conversion from string to list, used to run shuffle() method
	s = list(psw)
	random.shuffle(s)
	return ''.join(s)


#User Choices
lower_input = int(input("How many lowercase characters do you want?"))
upper_input = int(input("How many uppercase characters do you want?"))
punct_input = int(input("How many punctuation characters do you want?"))
digit_input = int(input("How many digits characters do you want?"))

print(random_psw(lower_input,upper_input,punct_input,digit_input))