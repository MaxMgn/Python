from random import randint


def player_move ():   
    number_to_take = 0
    while (number_to_take < 1 or number_to_take > 28 or number_to_take > candies):
        number_to_take = input("insert candies number to take: ")
    return number_to_take

def computer_move (candies):
    number_to_take = candies %  29
    if (number_to_take == 0):
        number_to_take = randint(1, 28)
    print ("computer took: " + str(number_to_take))
    return number_to_take

candies = 221
while True:
    print ("candies left: " + str(candies))
    candies = candies - player_move ()
    if candies == 0:
        print ("player win")
        break
    print ("candies left: " + str(candies))
    candies = candies - computer_move (candies)
    if candies == 0:
        print ("computer win")
        break