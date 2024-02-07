# #Write program to design a game of jumble words. Create a list with few words.
# Then generate a jumble word from any randomly chosen word. Create your own
# algorithm to jumble the word.
# Create it as two player game. Each player will get 2 opportunities, point will be 2 for
# correct answer in first attempt, point will be 1 for correct answer in first attempt and 0
# otherwise.

import random
words=["mango","grapes","rat","sat"]
user1=0
user2=0
x=1
flag=0
round=1
while(round<=3):
        chose_word = random.choice(words)
        print("Round",round)
        give_word=input("User 1 Guess the word : ")
        if(give_word==chose_word):
            user1+=2
            print("Right!!")
        else:
            give_word=input("anotehr chance for user1: ")
            if(give_word==chose_word):
                user1+=1
                print("Right!!")
            else:
                print("Sorry Guess Word is wrong")

      
        give_word = input("User 2 Guess the word : ")
        if (give_word == chose_word):
            user2 += 2
            print("Right!!")
        else:
            give_word = input("anotehr chance for user2: ")
            if (give_word == chose_word):
                user2+=1
                print("Right!!")
            else:
             print("Wrong")
        round+=1

if(user1>user2):
    print("Congratulation !! User1 Wins")
else:
    print("Congratulations !! User2 Wins")
