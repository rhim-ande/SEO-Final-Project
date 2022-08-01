import random

form = AnswerForm()
def correct_answer():
	flash('Correct!')
	#continue 

def incorrect_answer():
	flash('Incorrect. The correct answer is:', + #database + 
	'Retype correct answer.')
	if user.data ==

if user.answer == #database:
	 correct_answer()
if user.answer != #database: 
	flash('Incorrect. The correct answer is:', + #database + 
	'Retype correct answer.')
	if user.data ==
	




class matching_game:
	def __init__(self):
	
		self.asl={'img1':'sour',
				    'img2':'eat',
					'img3':'food'}
		
	def quiz(self):
		while (True):
		
			asl, definition = random.choice(list(self.asl.items()))
			
			print("What is the english translation of {}".format(asl))
			user_answer = input()
			
			if(user_answer.lower() == definition):
				print("Correct answer")
			else:
				print("Wrong answer")
				
			option = int(input("enter 0 , if you want to play again : "))
			if (option):
				break

print("welcome to your ASL quiz ")
fc=flashcard()
fc.quiz()
