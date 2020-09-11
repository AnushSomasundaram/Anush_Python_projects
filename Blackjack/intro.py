#"""this is the first block of code for the black jack game also known as 21
# this block of code will introduce the player to the game....and also make sure that the player
# knows the rules to the game"


def intro():
    print("-----Blackjack---------Blackjack---------Blackjack---------Blackjack----")
    
    print("\nWelcome to textbased BLACKJACK")
    
    print("\nI am casinotron...I'll most probably be your dealer for tonight")
    
    player_name = str(input("\nWhat is your name:-\t "))
    
    print("\nWell hello there",player_name)
    
    know=input("\nBefore we start do you know how to play black jack?\n..y or n\t")
    
    
    if know=="y":
        print("\nLet's play Blackjack")
    
    
    elif know=="n":
        print("\nAlright here are the rules:\n")
        print("""\n\t\t0.The goal of blackjack is to beat the dealer's hand without going over 21.\n
                1.Face cards are worth 10. Aces are worth 1 or 11, whichever makes a better hand.\n
                2.Each player starts with two cards, one of the dealer's cards is hidden until the end.\n
                3.To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.\n
                4.If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.\n
                5.If you are dealt 21 from the start (Ace & 10), you got a blackjack.\n
                6.Blackjack usually means you win 1.5 the amount of your bet.\n
                7.Dealer will hit until his/her cards total 17 or higher.\n
                8.Doubling is like a hit, only the bet is doubled and you only get one more card.\n
                9.Split can be done when you have two of the same card - the pair is split into two hands.\n
                10.Splitting also doubles the bet, because each new hand is worth the original bet.\n
                11.You can only double/split on the first move, or first move of a hand created by a split.\n
                12.You cannot play on two aces after they are split.\n
                13.You can double on a hand resulting from a split, tripling or quadrupling you bet.""")
    
    
    elif know!="n" or "y":
        print("\nAlright because you  clearly did not type y or n...here are the rules:\n")
        print("""\n\t\t0.The goal of blackjack is to beat the dealer's hand without going over 21.\n
                1.Face cards are worth 10. Aces are worth 1 or 11, whichever makes a better hand.\n
                2.Each player starts with two cards, one of the dealer's cards is hidden until the end.\n
                3.To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.\n
                4.If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.\n
                5.If you are dealt 21 from the start (Ace & 10), you got a blackjack.\n
                6.Blackjack usually means you win 1.5 the amount of your bet.\n
                7.Dealer will hit until his/her cards total 17 or higher.\n
                8.Doubling is like a hit, only the bet is doubled and you only get one more card.\n
                9.Split can be done when you have two of the same card - the pair is split into two hands.\n
                10.Splitting also doubles the bet, because each new hand is worth the original bet.\n
                11.You can only double/split on the first move, or first move of a hand created by a split.\n
                12.You cannot play on two aces after they are split.\n
                13.You can double on a hand resulting from a split, tripling or quadrupling you bet.""")
        


