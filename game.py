human_turn = "Rock"
computer_turn = "Rock"

if human_turn == computer_turn :
    print("Draw")
elif human_turn == "Rock" and  computer_turn == "Scissors":
    print("Humans_win!")
elif human_turn == "Paper" and computer_turn == "Rock" :
     print("Humans_win!")
elif human_turn == "Scissors" and computer_turn == "Paper" :
     print("Humans_win!")
else:
    print("computyer win!")
