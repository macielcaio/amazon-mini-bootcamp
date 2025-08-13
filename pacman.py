def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    if power_pellet_active == False and touching_ghost == False:
        print("You didn't eat the ghost")
    elif power_pellet_active == False and touching_ghost == True:
        print("Congrats! You have eaten the ghost")
    elif power_pellet_active == True and touching_ghost == False:
        print("You ate a ghost, but you didn't activate the power pellet")
    else:
        print("You ate a ghost and activated the power pellet, you are invincible!")

def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    if touching_power_pellet == False and touching_dot == False:
        print("Continue, you didn't score")
    elif touching_power_pellet == False and touching_dot == True:
        print("You scored 10 points")
    elif touching_power_pellet == True and touching_dot == False:
        print("You score 50 points")

def lose(power_pellet_active: bool, touching_ghost: bool) -> bool:
    if power_pellet_active == False and touching_ghost == True:
        print("You lose")
    elif power_pellet_active == True and touching_ghost == True:
        print("Try again")
    elif power_pellet_active == True and touching_ghost == False:
        print("Play again")

def win(has_eaten_all_dots: bool, power_pellet_active: bool, touching_ghost: bool) -> bool:

    if has_eaten_all_dots == True and power_pellet_active == False and touching_ghost == True:
        print("You lose!")
    elif has_eaten_all_dots == False and power_pellet_active == True and touching_ghost == True:
        print("Try again!")
    elif has_eaten_all_dots == True and power_pellet_active == True and touching_ghost == True:
        print("U Won!")
    elif has_eaten_all_dots == True and power_pellet_active == False and touching_ghost == False:
        print("U Won!")
    else:
        print("Game over")

win(True, True, False)
score(True, False)
lose(False, True)
eat_ghost(True, True)