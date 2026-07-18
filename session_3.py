player_1_score = 0
player_2_score = 0
round_number = 1

while round_number <= 3:
    print("Round", round_number)

    player_1 = input("Player 1 (r, p, s): ")
    player_2 = input("Player 2 (r, p, s): ")

    if (
        (player_1 != "r" and player_1 != "p" and player_1 != "s")
        or
        (player_2 != "r" and player_2 != "p" and player_2 != "s")
    ):
        print("Invalid choice")
        print("Please enter r, p, or s.")

    else:
        if (
            (player_1 == "r" and player_2 == "r")
            or (player_1 == "p" and player_2 == "p")
            or (player_1 == "s" and player_2 == "s")
        ):
            print("Draw")

        elif (
            (player_1 == "r" and player_2 == "s")
            or (player_1 == "p" and player_2 == "r")
            or (player_1 == "s" and player_2 == "p")
        ):
            print("Player 1 is victorious")
            player_1_score = player_1_score + 1

        elif (
            (player_2 == "r" and player_1 == "s")
            or (player_2 == "p" and player_1 == "r")
            or (player_2 == "s" and player_1 == "p")
        ):
            print("Player 2 is victorious")
            player_2_score = player_2_score + 1

        print("--------------------")
        round_number = round_number + 1


print("Player 1 score:", player_1_score)
print("Player 2 score:", player_2_score)

if player_1_score > player_2_score:
    print("Player 1 wins the game")

elif player_2_score > player_1_score:
    print("Player 2 wins the game")

else:
    print("The game is a draw")