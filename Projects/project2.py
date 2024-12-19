gamer_points = 0
outside_points =0

answer = input("On a weekend would you rather A) stay inside playing fortnite all day, or B) go outside and take a walk?\n")
if answer == "A":
        gamer_points += 1
elif answer == "B":
        outside_points += 1

answer = input("On a schoolday would you rather A) play fortnite, or B) go do your homework?\n")
if answer == "A":
        gamer_points += 1
elif answer == "B":
        outside_points += 1

answer = input("during a gaming session would you rather A) keep playing fortnite, or B) do your chores?\n")
if answer == "A":
        gamer_points += 1
elif answer == "B":
        outside_points += 1

answer = input("while on a walk would you rather A) go back home and buy Vbucks, or B) keep walking?\n")
if answer == "A":
        gamer_points += 1
elif answer == "B":
        outside_points += 1

answer = input("while eating dinner would you rather A) go back to playing fortnite, or B) keep enjoying your meal?\n")
if answer == "A":
        gamer_points += 1
elif answer == "B":
        outside_points += 1

if gamer_points > outside_points:
        print("you are a person with no life")
elif outside_points > gamer_points:
        print("you have a life")
elif gamer_points == outside_points:
        print("you have a pretty good life")