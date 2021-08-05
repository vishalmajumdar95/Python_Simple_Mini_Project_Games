import random

def ran():
    random_number = random.randint(1, 3)
    # print(random_number)
    if random_number == 1:
        c_n = "rock"
        return c_n
    elif random_number == 2:
        c_n = "paper"
        return c_n
    elif random_number == 3:
        c_n = "scissors"
        return c_n

# ASCII ART
rock_image = """
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)"""

paper_image = """
            _______
        ---'   ____)____
                  ______)
                  _______)
                 _______)
        ---.__________)"""

scissors_image = """
            _______
        ---'   ____)____
                  ______)   
             __________)   
              (____)
        ---.__(___)"""
    
        

def RockPaperScissors(username):
    while True:
        computer_action=ran()
        print("\n\t\t1. \U0001FAA8 - ROCK\n\n\t\t2. \U0001F4DD - PAPER\n\n\t\t3. ✂️ - SCISSORS\n\n")
        user_action=input(f"\t{username} Choose your any one option :=> ").lower()        
        if user_action == computer_action:
            print(f"\t\t\nBoth players selected {user_action}. It's a tie!\n")
            if user_action == rock_image:
                print("user_action =>\n\t",rock_image)
                print("computer_action =>\n\t",rock_image)
            elif user_action == paper_image:
                print("user_action =>\n\t",paper_image)
                print("computer_action =>\n\t",paper_image)
            else:
                print("user_action =>\n\t",scissors_image)
                print("computer_action =>\n\t",scissors_image)
        elif user_action == "rock":
            if computer_action == "scissors":
                print("user_action =>\n\t",rock_image)
                print("computer_action =>\n\t",scissors_image)
                print("\n\tRock smashes scissors! You win! \U0001f607\U0001f607\n")
            else:
                print("user_action =>\n\t",rock_image)
                print("computer_action =>\n\t",paper_image)
                print("\n\tPaper covers rock! You lose! \U0001F62D\U0001F62D\n")
        elif user_action == "paper":
            if computer_action == "rock":
                print("user_action =>\n\t",paper_image)
                print("computer_action =>\n\t",rock_image)
                print("\n\tPaper covers rock! You win! \U0001f607\U0001f607\n")
            else:
                print("user_action =>\n\t",paper_image)
                print("computer_action =>\n\t",scissors_image)
                print("\n\tScissors cuts paper! You lose! \U0001F62D\U0001F62D\n")
        elif user_action == "scissors":
            if computer_action == "paper":
                print("user_action =>\n\t",scissors_image)
                print("computer_action =>\n\t",paper_image)
                print("\n\tScissors cuts paper! You win! \U0001f607\U0001f607\n")
            else:
                print("user_action =>\n\t",scissors_image)
                print("computer_action =>\n\t",rock_image)
                print("\n/tRock smashes scissors! You lose! \U0001F62D\U0001F62D\n")
        else:
            print("\nYou enter invaild and please check then enter....\n")
            continue
            # user_action=input(f"\t{user_name} Choose your any one option :=> ").lower()
            
        # It will we run again the loop 
        # if the user want play again the game...
        user=input("\tDo you play again (Y/N) :=> ").lower()
        if user == "y":
            continue
        else:
            break

print("*********|->>>> Welcome in the Rock_Paper_Scessior Game <<<<-|*********** \n")
print("\t\t\t \U0001F64F\U0001F64F\U0001F64F\U0001F64F\U0001F64F\n")
user_name=input("\tEnter your name :=> ")

RockPaperScissors(user_name)