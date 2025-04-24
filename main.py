import random

player_score = 0
computer_score = 0


def select_card():
    player_choice = input("Make your choice: rock, scissors, paper: ")
    options = ["rock", "scissors", "paper"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices 

def check_win(player, computer):
    print(f"You select {player}, your enemy chose {computer}")
    if player == computer:
        return "It's a tie. Try again!"
    elif player == "rock": 
        if computer == "scissors":
            return "Rock smashes scissors! You Win!"
        else:
            return "Paper covers rock! You lose."
        
    elif player == "paper": 
        if computer == "rock":
            return "Paper covers rock! You Win!"
        else:
            return "Scissors cuts paper! You lose. "

    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You Win!"
        else:
            return "Rock smashes scissors! You lose. "
  


while player_score < 5 and computer_score < 5:     
    choices = select_card()
    result = check_win(choices["player"], choices["computer"])
    print(result)

    player_options = [
        "Boom! That’s how legends are made!",
        "You crushed it like a pro wrestler on a bad day!",
        "Winner winner, digital chicken dinner!",
        "Not even luck — just pure skill. Admit it!",
    ]

    computer_options = [
        "You can't even beat me!", 
        "Go play Minecraft", 
        "Too bad, you lost again.",
        "Oops... you're such a donut!",
        "Don't go crying to mama."
        ]
    
    if "You Win!" in result:
        player_score += 1
        print(random.choice(player_options))
    elif "You lose" in result:
        computer_score += 1
        print(random.choice(computer_options))

    

    print(f"\033[93mYour score is: {player_score}    Computer score is: {computer_score}\033[0m")
        


