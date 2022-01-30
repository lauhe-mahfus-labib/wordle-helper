import random

w = open("word.txt", "r")
word = w.read().split("\n")
valid_word = set()

def gray(s):
	"""this function search entire list and remove words which has gray letter"""
	global word,valid_word

	if s in valid_word:
		return 

	new_list = []
	for i in word:
		if s not in i:
			new_list.append(i)

	word = new_list.copy()

def yellow(s):
	"""this function search entire list and if any word doesn't have any yellow letter this function will remove those words"""
	global word, valid_word
	valid_word.add(s)

	new_list = []
	for i in word:
		if s in i:
			new_list.append(i)

	word = new_list.copy()

def green(w, pos):
	"""this function search entire list and if green letter in the right position this function will keep those words anything else will be removed"""
	global word,valid_word
	valid_word.add(w)

	new_list = []
	for i in word:
		x = list(i)
		if x[pos-1] == w:
			new_list.append(i)

	word = new_list.copy()



print(f"Welcome to Wordle helper")
count = 0
while count <7:

	x = input("Do you want us to choose word randomly?(type y for yes and if you want to choose then type anything else) : ")
	if x == "y":
		r = random.randint(0, len(word)-1)
		print(f"we have guess - [{word[r]}] for you")
	else:
		print("You can choose word form here: ")
		for i in word:
			print(i)

	x = input("Did you find your ans (y/n): ")
	if x == "y":
		break

	n = input("How many green letter did you find: ")
	for i in range(int(n)):
		w,pos = input("Green letter(example input: a 0) : ").split()
		green(w, int(pos))

	n = input("How many yellow letter did you find : ")
	for i in range(int(n)):
		val = input("Yellow letter (example input: a) : ")
		yellow(val)

	n = input("How many gray letter did you find : ")
	for i in range(int(n)):
		inv = input("gray letter (example input: a) : ")
		gray(inv)

	
	if len(word) == 0:
		print("Sorry your desire word isn't in our database.")
		break
	count +=1

print("Congratulations!")
