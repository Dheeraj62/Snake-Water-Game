"""This is a snake- water - gun game"""
import random
game_counter=10
cpu=0
player=0
list = ["S","W","G"]

print("ENter your choice from the following: ")
print("Snake - S")
print("Water - W")
print("Gun - G")

while game_counter>0:
    p_choice = input("ENter = ")
    cpu_choice = random.choice(list)
    print("CPU choice: ",cpu_choice)
    if cpu_choice == p_choice :
        print("Tie !!\nTry again")
        game_counter = game_counter - 1
        print("No. of turns left : {}\n".format(game_counter))
    else:
        if cpu_choice=="S" and p_choice == "W":
            cpu=cpu+1
            print("CPU points:{}".format(cpu))
            print("Your points: {}".format(player))
            game_counter=game_counter-1
            print("No. of turns left : {}\n".format(game_counter))

        elif cpu_choice=="S" and p_choice=="G":
            player = player+1
            game_counter=game_counter-1
            print("CPU points:{}".format(cpu))
            print("Your points: {}".format(player))
            print("No. of turns left : {}\n".format(game_counter))

        elif cpu_choice=="W" and p_choice=="G":
            cpu = cpu + 1
            print("CPU points:{}".format(cpu))
            print("Your points: {}".format(player))
            game_counter = game_counter - 1
            print("No. of turns left : {}\n".format(game_counter))
        elif cpu_choice == "W"  and p_choice == "S":
            player = player + 1
            print("CPU points:{}".format(cpu))
            print("Your points: {}".format(player))
            game_counter = game_counter - 1
            print("No. of turns left : {}\n".format(game_counter))
        elif cpu_choice == "G" and p_choice == "S":
            cpu = cpu + 1
            game_counter = game_counter - 1
            print("CPU points:{}".format(cpu))
            print("Your points: {}".format(player))
            print("No. of turns left : {}\n".format(game_counter))
        elif cpu_choice=="G" and p_choice=="W":
            player = player + 1
            print("CPU points:{}".format(cpu))
            print("Your points: {}".format(player))
            game_counter = game_counter - 1
            print("No. of turns left : {}\n".format(game_counter))
        else:
            print("You entered a wrong choice")
            exit()
print("\nPlayer points: ",player)
print("CPU points: ",cpu)
if player>cpu:
    print("\nYou win!!")
elif player == cpu:
    print("\nNobody won the game")
else:
    print("\nYou lose!!!")
