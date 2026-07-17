

player_1 = input("Player 1 (r, p, s): ")
player_2 = input("Player 2 (r, p, s): ")

if (player_1 != 'r' and player_1 != 'p' and player_1 != 's') or (player_2 != 'r' and player_2 != 'p' and player_2 != 's'):
    print("Invalid choice")
    exit()

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

elif (
        (player_2 == "r" and player_1 == "s")
        or (player_2 == "p" and player_1 == "r")
        or (player_2 == "s" and player_1 == "p")
    ):
        print("Player 2 is victorious")

else:
    print("Invalid choice")