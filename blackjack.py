import art
import random


def draw(d_card, lis):
    """ Pick random cards from cards array """
    for card in range(1, d_card + 1):
        rand_c = random.randint(0, len(cards) - 1)
        lis.append(cards[rand_c])


def addCards(lis: list) -> int:
    ''' Add total of cards in list '''
    return sum(lis)

def decision(num1: int, num2: int) -> str:
    """ Returns game winning scenario based on drawed cards"""

    if player_sum == comp_sum:
        return f"Equal Score! Draw"
    elif comp_sum == 21:
        return "Com wins! 21"
    elif player_sum == 21:
        return "Player wins! 21"
    elif comp_sum < player_sum and comp_sum <= 21:
        return f"You Lose! Your card total is {player_sum}"
    elif player_sum < comp_sum  and player_sum <= 21:
        return f"You Win! Your card total is {player_sum}"
    elif comp_sum > 21 and player_sum > 21:
        return f"Fold! Both over 21"

eoh = False
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
yon = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

player = []
comp = []
player_sum = 0
comp_sum = 0

while yon == 'y':
    print(art.logo)
    draw(2, player)
    draw(1, comp)
    print(f"Player cards: {player}")
    print(f"Computer first card: {comp}")
    another_card = input("Type 'y' to get another card, type 'n' to pass ")

    if another_card == 'y':
        draw(1, player)
        draw(1, comp)
        player_sum = addCards(player)
        comp_sum = addCards(comp)

        # Loop to draw cards if less than 17
        while comp_sum < 17:
            draw(1, comp)
            comp_sum = addCards(comp)

        # Outputting player and comp hand
        print(f"{player} = {player_sum}")
        print(f"{comp}   = {comp_sum}")

        # Getting decision
        dec_output = decision(player_sum, comp_sum)

        print(dec_output)

        # End game or player new one
        yon = input("Do you want to play again 'y' or 'n' ")
        player = []
        comp = []
    elif another_card == 'n':
        draw(1, comp)
        comp_sum = addCards(comp)
        while comp_sum < 17:
            draw(1, comp)
            comp_sum = addCards(comp)

        player_sum = addCards(player)

        print(f"Player: {player}")
        print(f"Comp    {comp}")

        dec_output = decision(player_sum, comp_sum)
        print(dec_output)

        # End game or player new one
        yon = input("Do you want to play again 'y' or 'n' ")
        player = []
        comp = []

print("Thanks for coming")
