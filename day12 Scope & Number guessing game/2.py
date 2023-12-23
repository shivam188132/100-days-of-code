import random
from art import logo
easy_level_turn=10
hard_level_turns=5
def check_answer(guess,selected_number,turns):
    '''checks the answer and return no. of turns remaninig'''
    if guess>selected_number:
        print("to high")
        return turns-1
    elif guess <selected_number:
        print("to low")
        return turns-1 
    else:
        print(f"you got it !. the answer is {selected_number}")
def set_difficulty ():
    level=input("choose your difficulty level 'easy' or 'hard' ")
    if level=="easy":
        return easy_level_turn
    else:
        return hard_level_turns

def game():
    print("welcome to the number guessing game ")
    print(logo)
    no_collection=[]
    for i in range(101):
        no_collection.append(i)
    
    selected_number=random.choice(no_collection)
    
    turns=set_difficulty()
    

    guess=0
    while guess!=selected_number:
        print(f"you have {turns} attempts remaining ")
        guess=int(input("make a guess: "))
        turns=check_answer(guess, selected_number, turns)
        if turns==0:
            print("you run out of the guess . You loose")
            return
        elif guess!=selected_number:
            print("guess again")
game()                
     
            
                
    
