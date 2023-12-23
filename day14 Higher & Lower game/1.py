from art import logo,vs
from game_data import data
import random
import os


def format_data(account):

    '''format the accout data into a printable forrmat.'''
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return (f" {account_name} , a {account_descr} from  {account_country}")


def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
#display art 
def game():

  print(logo)
  score=0
  should_game_continue= True
  account_a=random.choice(data)
  account_b= random.choice(data)
  while should_game_continue:
    #generate a random account from game data
    account_a = account_b
    account_b =random.choice(data) 
    if account_a==account_b:
        accont_b=random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    #ask a user for a guess
    guess= input("who has more folowers ? Type 'A' or 'B'. ").lower()
    #get the follower count for each account

    a_follower_count=int(account_a["follower_count"])
    b_follower_count=int(account_b["follower_count"])

    #clear
    os.system('cls')
    print(logo)

    # give the user feedback on their guess 
    is_correct= check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        score+=1
        print( f"you are right now your score is  {score}")
    else:
        should_game_continue=False
        print(f"sorry thats wrong! .Your final score is  {score}")
game()       
      

#make the game repetable
