import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
    chamber_position = spin_chamber()
    if chamber_position == bullet_position :
        return "The heavy is dead"
    else :
        return "Lararara"
	# YOUR CODE HERE




print(fire_gun())