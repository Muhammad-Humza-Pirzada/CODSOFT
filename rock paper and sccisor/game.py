import random
import string

print("""
      ~~~~~Welcome to Rock Paper And Sccisor Game~~~~~
      ''''''''''''''''''''''''''''''''''''''''''''''''
      """)

user_score = 0
comp_score = 0
ties = 0
# alpha = string.ascii_letters
# print(alpha)
name = input("""
        ~~~~~Enter your name:~~~~~ 
        ``````````````````````````
        """)

print("""
        ~~~~~~~Winning Rules~~~~~~~
        1. Paper vs Rock ---> Paper
        2. Rock vs Scissors ---> Rock
        3. Scissors vs Paper ---> Scissor
    """)

print("""
        ~~~~~~~~Choices Are~~~~~~~~
        1. Rock
        2. Paper
        3. Scissors
    """)

while True:
    userChoices = input("""
        ~~~~~Enter your choice from 1 to 3 --> ~~~~~~
        `````````````````````````````````````````````
        """)
    
    while userChoices not in ['1', '2', '3']:
        userChoices = input("""
        ~~~~~~Enter a valid choice (1 to 3):--> ~~~~~~
        ```````````````````````````````````````
        """)

    userChoices = int(userChoices)
        
    if userChoices == 1:
        userChoices = "Rock"
    elif userChoices == 2:
        userChoices = "Paper"
    else:
        userChoices = "Scissors" 
    
    print()  
    print(
        f"""
        ~~~~~You choosed: {userChoices}~~~~~
        `````````````````````````````````````
        """
        )

    # print("Now turn of Second player ")   

    computer_choice = random.randint(1,3)

    if computer_choice == 1:
        computer_choice = "Rock"
    elif computer_choice == 2:
        computer_choice = "Paper"
    else:
        computer_choice = "Scissors"   
        
    print(
        f"""
        ~~~~~Computer choosed {computer_choice}~~~~~
        ````````````````````````````````````````````
        """
        ) 

    if ((userChoices == "Paper" and computer_choice == "Rock") or (userChoices == "Rock" and computer_choice =="Paper")):
        # print("""
        #       ~~~~~~Paper Win~~~~~~
        #       `````````````````````\n
        #       """) 
        result = "Paper"
    elif ((userChoices == "Rock" and computer_choice == "Scissors") or (userChoices == "Scissors" and computer_choice == "Rock")):
        # print("""
        #       ~~~~~~Rock Win~~~~~~
        #       ````````````````````\n
        #       """)
        result = "Rock "
    elif userChoices == computer_choice:
        print("""
            ~~~~~~Game Tie~~~~~ \n
            ```````````````````
              """)
        result = "Tie"    
    else:
        # print("Scissors \n")
        result = "Scissors"
        
    if result == "Tie":
        ties += 1
    elif result == userChoices:
        print("""
        ~~~~~~You Win~~~~~~
        ```````````````````
              """)
        user_score += 1
    else:
        print("""
        ~~~~~~Computer Wins~~~~~~
        `````````````````````````
              """)
        comp_score += 1
        
    print(
        f"""
        ~~~~~~~Score are~~~~~~~
        ```````````````````````
        _____________________________
        | {name}\'s scores are {user_score}      |
        | Computer\'s scores are {comp_score}   |
        | Ties are {ties}                |
        `````````````````````````````
    """)

    repeat_game = input("""
        ~~~~~~Do you want to play againe?~~~~~~            
            """)
    if repeat_game == 'no' or repeat_game == "No":
        break
    elif repeat_game == 'yes' or repeat_game == "Yes":
        continue
    elif repeat_game not in ['yes', 'no', 'Yes', 'No']:
        repeat_game = input("""
        ~~~~~~Please type yes or no~~~~~~~
        """)
        if repeat_game == 'yes' or repeat_game == "Yes":
            continue
        else:
            break
        


print("""
         _______________________ 
        |                       |
        |       Game Over       |
        |       Thank You       |
        |_______________________|
    
    """)
    
    

    
     
    

