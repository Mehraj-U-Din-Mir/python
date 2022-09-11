from random import random


import random
words= input("Enter the elements separated with commas  :")
word_input=words.split(',')
# print(word_inpuut)
score=0
for i in word_input:
    print("Arrange the letters to form a valid word: ")
    word=random.choice(word_input)
    temp=list(word)
    random.shuffle(temp)
    display=''.join(temp)
    print(display)
    user_guess=input()
    if(word==user_guess):
        score=score+1
        print("Correct")
    else:
        score=score-1
        print("Wrong")
print("Net Score is :", score)