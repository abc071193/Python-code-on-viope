The second exercise in this chapter continues with random selection. 
In this exercise the objective is to develop a game called nuke-foot-cockroach,
which is pretty similar to the more popular variant, paper-rock-scissors. 
The rules are simple: both players select either nuke, foot or cockroach, and the winner is determined in the following way: 
Foot beats cockroach, nuke beats foot and cockroach beats nuke. 
If both the player and the AI select the same, it's a tie, except if both choose nuke, then both lose.
def valitse():
    import random
    selection = random.randint(1,3)
    if selection == 1: selection = "Foot"
    if selection == 2: selection = "Nuke"
    if selection == 3: selection = "Cockroach"
    return selection

def main():
    wins = 0
    tied = 0
    laps = 0
    while True:
        selection = input("Foot, Nuke or Cockroach? (Quit ends): ")
        if selection not in ["Foot","Nuke","Cockroach","Quit"]:
            print("Incorrect selection.")
            continue
        computer = valitse()
        if selection == "Quit":
            break
        laps = laps + 1
        print("You chose:",selection)
        print("Computer chose:",computer)
        if (selection == computer) and (computer != "Nuke"):
            print("It is a tie!")
            tied = tied + 1
        elif selection == computer and computer == "Nuke":
            print("Both LOSE!")

        elif selection == "Foot" and computer == "Cockroach":
            print("You WIN!")
            wins = wins + 1

        elif selection == "Foot" and computer == "Nuke":
            print("You LOSE!")

        elif selection == "Nuke" and computer == "Foot":
            print("You WIN!")
            wins = wins + 1
        elif selection == "Nuke" and computer == "Cockroach":
            print("You LOSE!")
            
        elif selection == "Cockroach" and computer == "Nuke":
            print("You WIN!")
            wins = wins + 1
        elif selection == "Cockroach" and computer == "Foot":
            print("You LOSE!")

            
    print("You played ",laps," rounds, \
and won ",wins," rounds, playing tie in ",tied," rounds.", sep ="")

if __name__ == "__main__":
    main()
