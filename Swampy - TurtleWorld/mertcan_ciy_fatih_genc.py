from swampy.TurtleWorld import *
import random
#REFERENCES:
#https://www.pythonforbeginners.com/lists/python-lists-cheat-sheet

def func_for_another_round():
    print("***** Welcome to Sehir Minesweeper *****")
    print("------- First Turtle -------")
    while True:
        name1 = input("Please type the name of the first Turtle: ")
        if name1 == "":
            print("ERROR! Name can't be empty!")
            continue
        else:
            break
    color1 = "red"
    color2 = "blue"
    color3 = "green"
    ask_for_color1 = input("Please choose turtle color for " + name1 + " red, blue, or green): ")
    while ask_for_color1 != color1 or ask_for_color1 != color2 or ask_for_color1 != color3:
        if ask_for_color1 == color1 or ask_for_color1 == color2 or ask_for_color1 == color3:
            print("------ " + name1 + " IS READY TO GO :) ------")
            break
        else:
            print("ERROR! " + ask_for_color1 + " is not a valid color")
            ask_for_color1 = input("Please choose turtle color for " + name1 + " red, blue, or green): ")
    print("------- Second Turtle -------")
    while True:
        name2 = input("Please type the name of the second Turtle: ")
        if name2 == "":
            print("ERROR! Name can't be empty!")
        elif name2 == name1:
            print("ERROR! " + name1 + " is already taken, please enter another name !")
        else:
            break
    ask_for_color2 = input("Please choose turtle color for " + name2 + " red, blue, or green): ")
    while ask_for_color2 != color1 or ask_for_color2 != color2 or ask_for_color2 != color3:
        if ask_for_color2 == ask_for_color1:
            print("ERROR! " + ask_for_color1 + " is already taken, select another color!")
            ask_for_color2 = input("Please choose turtle color for " + name2 + " red, blue, or green): ")
        elif ask_for_color2 == color1 or ask_for_color2 == color2 or ask_for_color2 == color3:
            print("------ " + name2 + " IS READY TO GO :) ------")
            break
        else:
            print("ERROR! " + ask_for_color2 + " is not a valid color")
            ask_for_color2 = input("Please choose turtle color for " + name2 + " red, blue, or green): ")


    def bombs(start_point, start_point_2):
        global used_steps
        used_steps = []
        counter = 1
        while counter <= 5:
            steps = random.randrange(120, 841, 30)
            if steps in used_steps:
                continue
            bomb_name = "bombline1" + str(counter)
            bomb_name_2 = "bombline2" + str(counter)
            bomb_name = Turtle()
            bomb_name_2 = Turtle()
            bomb_name.set_color("black")
            bomb_name_2.set_color("black")
            pu(bomb_name)
            lt(bomb_name, 90)
            fd(bomb_name, start_point)
            rt(bomb_name, 90)
            fd(bomb_name, 15)
            pd(bomb_name)
            pu(bomb_name_2)
            lt(bomb_name_2, 90)
            fd(bomb_name_2, start_point_2)
            rt(bomb_name_2, 90)
            fd(bomb_name_2, 15)
            pd(bomb_name_2)
            used_steps.append(steps)
            pu(bomb_name)
            fd(bomb_name, steps)
            pd(bomb_name)
            pu(bomb_name_2)
            fd(bomb_name_2, steps)
            pd(bomb_name_2)
            counter += 1
    start_input_bombs = input("Enter 1 to draw the game area and deploy bombs randomly: ")
    while start_input_bombs != "1":
        print("Please, just click to ENTER 1 :)")
        start_input_bombs = input("Enter 1 to draw the game area and deploy bombs randomly: ")

    world = TurtleWorld().geometry("1200x300")
    drawer_of_frame = Turtle()
    drawer_of_road1 = Turtle()
    drawer_of_road2 = Turtle()


    def making_frame():
        for i in range(2):
            Turtle.set_delay(drawer_of_frame, 0.01)
            fd(drawer_of_frame, 900)
            lt(drawer_of_frame, 90)
            fd(drawer_of_frame, 150)
            lt(drawer_of_frame, 90)
        drawer_of_frame.die()
    making_frame()
    def making_squares(roads,start_point):
        Turtle.set_delay(roads, 0.001)
        pu(roads)
        lt(roads, 90)
        fd(roads, start_point)
        rt(roads, 90)
        fd(roads, 15)
        pd(roads)
        for i in range(30):
            for i in range(4):
                fd(roads, 5)
                lt(roads, 90)
            pu(roads)
            fd(roads, 30)
            pd(roads)
        roads.die()
    making_squares(drawer_of_road1, 30)
    making_squares(drawer_of_road2, 120)
    bombs(30, 120)

    def start_of_turtles(starts, start_point):
        pu(starts)
        lt(starts, 90)
        fd(starts, start_point)
        rt(starts, 90)
        fd(starts, 15)
        pd(starts)

    print("Let's start the game with a coin toss.")
    users = [name1, name2]
    result = random.choice(users)
    t_1 = name1
    t_2 = name2
    if result == name1:
        player = t_1
        print(str(name1) + " won the toss, " + str(name1) + " starts first.")
    else:
        player = t_2
        print(str(name2) + " won the toss, " + str(name2) + " starts first.")
    def game_time(player):
        name1 = Turtle()
        name1.set_color(ask_for_color1)
        name2 = Turtle()
        name2.set_color(ask_for_color2)
        start_of_turtles(name1, 30)
        start_of_turtles(name2, 120)
        traps = []
        score1 = 0
        score2 = 0
        for_turn_1 = 0
        for_turn_2 = 0
        for i in used_steps:
            trap_step = i / 30
            traps.append(trap_step)
        while score1 not in traps or score2 not in traps:
            roll = input("Please press ENTER to roll the dice " + player + "!")
            step = random.randint(1, 6)
            if roll != "":
                print("Please press ENTER! We can start the game then(:")
            if roll == "":
                print("Dice Result: " + str(step))
                if player == t_1 and score1 not in traps:
                    if (30 - score1) <= step:
                        print(t_1 + "' Score: " + str(score1 + step))
                        step = 30 - score1 -1
                        pu(name1)
                        fd(name1, step * 30)
                        pd(name1)
                        print(t_2 + "' Score: " + str(score2))
                        end_of_game1 = "Hooorrayy !! " + t_1 + " has won."
                        print(end_of_game1)
                        question_for_restart = input(t_1 + " wins the game, would you like to play again?(yes/no) ")
                        if question_for_restart =="yes":
                            func_for_another_round()
                        elif question_for_restart == "no":
                            exit()
                    else:
                        pu(name1)
                        fd(name1, step * 30)
                        pd(name1)
                        score1 += step
                        print(t_1 + "' Score: " + str(score1))
                        print(t_2 + "' Score: " + str(score2))
                    if step == 6 and score1 not in traps:
                        print(t_1 + " will roll again!")
                        continue
                    if score1 in traps:
                        print(player + " stepped on bomb. BOOOM !!!\n" + player +" is eliminated")
                        for_turn_1 = 1
                    if for_turn_2 == 0:
                        player = t_2
                elif score2 not in traps:
                    if (30 - score2) <= step:
                        print(t_2 + "' Score: " + str(score2 + step))
                        step = 30 - score2 - 1
                        pu(name2)
                        fd(name2, step * 30)
                        pd(name2)
                        print(t_1 + "' Score: " + str(score1))
                        end_of_game1 = "Hooorrayy !! " + t_2 + " has won."
                        print(end_of_game1)
                        question_for_restart = input(t_2 + " wins the game, would you like to play again?(yes/no) ")
                        if question_for_restart =="yes":
                            func_for_another_round()
                        elif question_for_restart == "no":
                            exit()
                    else:
                        pu(name2)
                        fd(name2, step * 30)
                        pd(name2)
                        score2 += step
                        print(t_1 + "' Score: " + str(score1))
                        print(t_2 + "' Score: " + str(score2))
                    if step == 6 and score2 not in traps:
                        print(t_2 + " will roll again!")
                        continue
                    if score2 in traps:
                        print(player + " stepped on bomb. BOOOM !!!\n" + player + " is eliminated")
                        for_turn_2 = 1
                    if for_turn_1 == 0:
                        player = t_1
        both_died =input("No one could win this game, would you like to play again? (yes/no): ")
        if both_died == "yes":
            func_for_another_round()
        else:
            exit()
    game_time(player)
    wait_for_user()
func_for_another_round()

