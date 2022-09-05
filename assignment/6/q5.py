#Write a python script to print two given words in dictionary order
print("Enter two words")
word1,word2=input(),input()
print(word1, word2, sep=' ') if(word1<=word2) else print(word2, word1, sep=' ')